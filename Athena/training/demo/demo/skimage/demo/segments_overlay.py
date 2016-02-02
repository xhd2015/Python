""" Defines the SegmentsOverlay class.
"""

from numpy import array

from enable.api import Component
from traits.api import Instance, List, Tuple, Color, Range

from chaco.api import AbstractOverlay


# XXX -- This code was copied from a more complicated overlay and pared
#        down to its current state.  There may still be some unecessary code.
#
# XXX -- Requires the padding of the component to be 0.

class SegmentsOverlay(AbstractOverlay):
    """
    Draw selectable line segments.
    """
    
    # The component that this tool overlays
    component = Instance(Component)
    
    # XXX Necessary?
    image_shape = Tuple

    # Color of the line segments.
    line_color = Color('green')
    
    alpha = Range(low=0.0, high=1.0, value=1.0)

    # The list of line segments.  Each segment is a tuple of the
    # form ((x0, y0), (x1, y1))
    # XXX Maybe use a numpy array?
    segments = List
    
    #------------------------------------------------------------------------
    # Object interface
    #------------------------------------------------------------------------
    
    def __init__(self, component=None, **kwtraits):
        if "component" in kwtraits:
            component = kwtraits["component"]
        super(SegmentsOverlay, self).__init__(**kwtraits)
        self.component = component
        return

    #------------------------------------------------------------------------
    # Drawing tool methods
    #------------------------------------------------------------------------

    def reset(self):
        """ Resets the tool in the current plot.
        """
        if self.component is not None:
            c1, c2 = self._data_corners()
            dx = c2[0] - c1[0]
            dy = c2[1] - c1[1]
            pt1 = (c1[0] + 0.05*dx, c1[1] + 0.05*dy)
            pt2 = (c2[0] - 0.05*dx, c2[1] - 0.05*dy)
            self.points = [pt1, pt2]
            self.event_state = "normal"
            self.line.points = list(self.component.map_screen(array(self.points)))
            self.request_redraw()
        return

    def _activate(self):
        """
        Called by a PlotComponent when this becomes the active tool.
        """
        pass

    def _deactivate(self, component=None):
        """
        Called by a PlotComponent when this is no longer the active tool.
        """
        # XXX  Is this the correct thing to do?  Do we even need to implement
        # this method?
        self.visible = False
        self.request_redraw()
        return


    #------------------------------------------------------------------------
    # override AbstractOverlay methods
    #------------------------------------------------------------------------

    def overlay(self, component, gc, view_bounds, mode="normal"):
        """ Draws this component overlaid on another component.
        
        Implements AbstractOverlay.
        """
        with gc:
            gc.clip_to_rect(component.x, component.y,
                            component.width-1, component.height-1)
            self._really_draw(gc)
        return
    
    def request_redraw(self):
        """ Requests that the component redraw itself. 
        
        Overrides Enable Component.
        """
        self.component.invalidate_draw()
        self.component.request_redraw()
        return

    #------------------------------------------------------------------------
    # Private methods
    #------------------------------------------------------------------------

    def _data_corners(self):
        """Get the dataspace points at the corners of the plot."""
        index_range = self.component.index_mapper.range
        value_range = self.component.value_mapper.range
        pts = [(index_range.low, value_range.low),
                (index_range.high, value_range.high)]
        return pts

    def _map_data(self, point):
        """ Maps values from screen space into data space.
        """
        index_mapper = self.component.index_mapper
        value_mapper = self.component.value_mapper
        if self.component.orientation == 'h':
            ndx = index_mapper.map_data(point[0])
            val = value_mapper.map_data(point[1])
        else:
            ndx = index_mapper.map_data(point[1])
            val = value_mapper.map_data(point[0])
        return (ndx, val)

    def _map_screen(self, point):
        """ Maps values from data space into screen space.
        """
        # Temporary hack--this object should know nothing about "canny_plot"!
        x_mapper = self.component.x_mapper
        y_mapper = self.component.y_mapper

        x = x_mapper.map_screen(point[0])
        y = y_mapper.map_screen(point[1])
        return (x, y)

    def _really_draw(self, gc):
        """Render the line segments."""
        w = self.component.width
        h = self.component.height
        padl, padr, padt, padb = self.component.padding
        aw = w - padl - padr
        ah = h - padt - padb
        outerw, outerh = self.component.outer_bounds
        with gc:
            gc.set_stroke_color(self.line_color_[:3] + (self.alpha,))
            gc.set_line_width(2.5)
            for p0, p1 in self.segments:
                # XXX These calculations should be in a mapper or something...
                x0 = padl + p0[0] * aw / float(self.image_size[1])
                y0 = padb + (self.image_size[0] - p0[1]) * ah / float(self.image_size[0])
                x1 = padl + p1[0] * aw / float(self.image_size[1])
                y1 = padb + (self.image_size[0] - p1[1]) * ah / float(self.image_size[0])
                gc.move_to(x0, y0)
                gc.line_to(x1, y1)
                gc.stroke_path()

        return


    #------------------------------------------------------------------------
    # Trait event handlers
    #------------------------------------------------------------------------
    
    def _component_changed(self, old, new):
        if new:
            self.container = new
        return
