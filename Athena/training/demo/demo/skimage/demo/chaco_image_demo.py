
import numpy as np
from scipy.misc import imread
from skimage.filter import canny
from skimage.transform import probabilistic_hough

from traits.api import HasTraits, File, Array, Property, Instance, Any, \
                        Int, List, Tuple, Range, Color, \
                        DelegatesTo, \
                        cached_property, on_trait_change
from traitsui.api import View, UItem, Item, VGroup, HGroup
from chaco.api import Plot, ArrayPlotData, bone
from enable.api import ComponentEditor

# Local import
from segments_overlay import SegmentsOverlay


class ImageProcessor(HasTraits):

    original_image = Array

    canny_sigma = Range(value=1, low=0.0)

    canny_low_threshold = Range(value=0.1, low=0.0)

    canny_high_threshold = Range(value=0.2, low=0.0)

    canny_image = Property(Array, depends_on=['original_image',
                                              'canny_sigma',
                                              'canny_low_threshold',
                                              'canny_high_threshold'])

    hough_threshold = Int(10)
    hough_line_length = Int(50)
    hough_line_gap = Int(10)
    hough_segments = Property(List, depends_on=['canny_image',
                                                'hough_threshold',
                                                'hough_line_length',
                                                'hough_line_gap'])

    def _original_image_default(self):
        return np.array([[0]])

    @cached_property
    def _get_canny_image(self):
        ci = canny(self.original_image, sigma=self.canny_sigma,
                                        low_threshold=self.canny_low_threshold,
                                        high_threshold=self.canny_high_threshold)
        return ci

    @cached_property
    def _get_hough_segments(self):
        segs = probabilistic_hough(self.canny_image,
                                    threshold=self.hough_threshold,
                                    line_length=self.hough_line_length,
                                    line_gap=self.hough_line_gap)
        return segs


class Demo(HasTraits):

    # FIXME: simplify as much as possible the property dependencies

    filename = File

    image = Instance(ImageProcessor, ())
    
    shape = Property(Tuple, depends_on=['image'])
    width = Property(Int, depends_on=['shape'])
    height = Property(Int, depends_on=['shape'])

    original_image = DelegatesTo('image')
    canny_sigma = DelegatesTo('image')
    canny_low_threshold = DelegatesTo('image')
    canny_high_threshold = DelegatesTo('image')
    canny_image = DelegatesTo('image')

    hough_threshold = DelegatesTo('image')
    hough_line_length = DelegatesTo('image')
    hough_line_gap = DelegatesTo('image')
    hough_segments = DelegatesTo('image')

    segments_overlay = Any

    original_alpha = Range(value=1.0, low=0.0, high=1.0) 

    plot_data = Instance(ArrayPlotData)
    main_plot = Instance(Plot)

    canny_color = Color('red')
    canny_plot_image = Property(Array, depends_on=['image',
                                                   'canny_image',
                                                   'canny_sigma',
                                                   'canny_low_threshold',
                                                   'canny_high_threshold',
                                                   'canny_color'])
    canny_alpha = Range(value=1.0, low=0.0, high=1.0)

    hough_segments_alpha = Range(value=1.0, low=0.0, high=1.0) 
    hough_segments_color = Color('green')

    original_plot = Any
    canny_plot = Any

    background_color = Color('black')

    traits_view = \
        View(
            HGroup(
                VGroup(
                    Item('filename'),
                    HGroup(
                        Item('width', style='readonly', width=60),
                        Item('height', style='readonly', width=60),
                    ),
                    VGroup(
                        Item('canny_sigma', label='Sigma'),
                        HGroup(
                            Item('canny_low_threshold', label='Low', width=40),
                            Item('canny_high_threshold', label='High', width=40),
                            label="Threshold",
                            show_border=True,
                        ),
                        label="Canny Filter Parameters",
                        show_border=True,
                    ),
                    VGroup(
                        Item('hough_threshold', label='Threshold'),
                        Item('hough_line_length', label='Min line length'),
                        Item('hough_line_gap', label='Max line gap'),
                        label="Probabilistic Hough Transform Parameters",
                        show_border=True,
                    ),
                    VGroup(
                        Item('original_alpha', springy=True),
                        Item('canny_alpha', springy=True),
                        Item('canny_color', springy=True),
                        Item('hough_segments_alpha', label='Hough alpha', springy=True),
                        Item('hough_segments_color', label='Hough color', springy=True),
                        Item('background_color', label='Background', springy=True),
                        label="Display Parameters",
                        show_border=True,
                    ),
                ),
                UItem('main_plot', editor=ComponentEditor()),
            ),
            resizable=True,
            width=1200,
            height=1000,
            title="Image Processing Demo",
        )

    #-------------------------------------------------------------------
    # Trait defaults
    #-------------------------------------------------------------------

    def _plot_data_default(self):
        pd = ArrayPlotData(original_image=self.image.original_image,
                           canny_plot_image=self.canny_plot_image)
        return pd

    def _main_plot_default(self):
        p = Plot(self.plot_data, default_origin='top left')
        p.padding = 0
        self.original_plot = p.img_plot('original_image', colormap=bone,
                                        alpha=self.original_alpha,
                                        bgcolor=self.background_color_)[0]
        self.canny_plot = p.img_plot('canny_plot_image',
                                     alpha=self.canny_alpha)[0]
        p.x_axis = None
        p.y_axis = None
        self.segments_overlay = SegmentsOverlay(component=self.canny_plot,
                                                image_size=self.image.canny_image.shape)
        p.overlays.append(self.segments_overlay)
        return p

    #-------------------------------------------------------------------
    # Trait property methods
    #-------------------------------------------------------------------

    @cached_property
    def _get_shape(self):
        shape = self.image.original_image.shape
        return shape

    @cached_property
    def _get_width(self):
        width = self.shape[1]
        return width

    @cached_property
    def _get_height(self):
        height = self.shape[0]
        return height

    @cached_property
    def _get_canny_plot_image(self):
        # self.image.canny_image is an array of bools.
        # self.canny_plot_image is a 3D array (2D image with (r,g,b,a)
        # values).  The color (0,0,0,0) (transparent) is assigned where
        # canny_image is False, and (canny_color_, 255) is assigned where
        # canny_image is True.
        ci = self.image.canny_image
        x = np.zeros(ci.shape + (4,), dtype=np.uint8)
        x[ci, :3] = self.canny_color_
        x[ci, 3] = 255
        return x

    #-------------------------------------------------------------------
    # Trait change handlers
    #-------------------------------------------------------------------

    def _filename_changed(self):
        try:
            image_data = imread(self.filename, flatten=True).astype(np.float32)
            image_data /= image_data.max()
            image = ImageProcessor(original_image=image_data)
        except IOError:
            image = ImageProcessor(original_image=np.array([[0]]))
        self.image = image

        self.plot_data['original_image'] = self.image.original_image
        self.plot_data['canny_plot_image'] = self.canny_plot_image
        self.segments_overlay.image_size = self.image.canny_image.shape
        self.segments_overlay.segments = self.image.hough_segments

    @on_trait_change('canny_plot_image')
    def _canny_parameter_changed(self):
        self.plot_data['canny_plot_image'] = self.canny_plot_image

    def _original_alpha_changed(self):
        self.original_plot.alpha = self.original_alpha
        # Temporary hack...
        self.plot_data['original_image'] = self.image.original_image
        self.plot_data['canny_plot_image'] = self.canny_plot_image

    @on_trait_change('canny_alpha, canny_color')
    def _canny_display_parameters_changed(self):
        self.canny_plot.alpha = self.canny_alpha
        # Temporary hack...
        self.plot_data['original_image'] = self.image.original_image
        self.plot_data['canny_plot_image'] = self.canny_plot_image

    @on_trait_change('hough_segments_alpha, hough_segments_color')
    def _hough_display_parameters_changed(self):
        self.segments_overlay.line_color = self.hough_segments_color
        self.segments_overlay.alpha = self.hough_segments_alpha
        self.segments_overlay.request_redraw()

    def _background_color_changed(self):
        self.original_plot.bgcolor = self.background_color_
        self.original_plot.request_redraw()

    @on_trait_change('hough_segments')
    def _update_hough_segments_plot(self):
        print len(self.image.hough_segments), "segments"
        self.segments_overlay.segments = self.image.hough_segments
        self.canny_plot.request_redraw()



if __name__ == "__main__":
    d = Demo()
    d.configure_traits()
