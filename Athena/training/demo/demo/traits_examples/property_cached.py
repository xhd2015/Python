
from traits.api import HasTraits, Float, Property, cached_property


class Rectangle(HasTraits):

    # Width of the rectangle
    width = Float(1.0)

    # Height of the rectangle
    height = Float(2.0)

    # The area of the rectangle (width*height)
    area = Property(depends_on=['width', 'height'])

    @cached_property
    def _get_area(self):
        """ Return the area (width*height) of the rectangle.
        """
        print 'Recalculating area...'
        return self.width * self.height


if __name__ == "__main__":
    rect = Rectangle(width=3.0, height=4.0)
