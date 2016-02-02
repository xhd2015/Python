#!/usr/bin/env python
"""
Shape Inheritance
-----------------

In this exercise, you will use class inheritance to define a few 
different shapes and draw them onto an image.  All the classes will
derive from a single base class, Shape, that is defined for you.
The Shape base class requires two arguments, x and y, that are the
position of the shape in the image.  It also has two keyword arguments,
color and line_width, to specify properties of the shape.  In this
exercise, color can be 'red', 'green', or 'blue'.  The Shape class
also has a method draw(image) that will draw the shape into the
specified image.

One Shape sub-class, Square, is already defined for you.  Study its
draw(image) method and then define two more classes, Line and Rectangle.
Use these classes to draw two more shapes to the image.  You will need
to override both the __init__ and the draw method in your sub-classes.

1. The constructor for Line should take 4 values::
    
        Line(x1, y1, x2, y2)

   Here x1, y1 define one end point and x2, y2 define the other end point.
   color and line_width should be optional arguments.

2. The constructor for Rectangle should take 4 values::

        Rectangle(x, y, width, height)
    
   Again, color and line_width should be optional arguments.

Bonus
~~~~~

    Add a Circle class.

Hints
~~~~~

    The "image" has several methods to specify and also "stroke" a path.
    
    move_to(x, y)
        move to an x, y position
    line_to(x, y) 
        add a line from the current position to x, y
    arc(x, y, radius, start_angle, end_angle)
        add an arc centered at x, y with the specified radius
        from the start_angle to end_angle (specified in radians)
    close_path()
        draw a line from the current point to the starting point
        of the path being defined
    stroke_path()
        draw all the lines that have been added to the current path
"""

from kiva.agg import GraphicsContextArray as Image


# Map color strings to RGB values.
color_dict = dict(red=(1.0, 0.0, 0.0), 
                  green=(0.0, 1.0, 0.0),
                  blue=(0.0, 0.0, 1.0))
              
class Shape(object):
    
    def __init__(self, x, y, color='red', line_width=2):
        self.color = color
        self.line_width = line_width
        self.x = x
        self.y = y
        
    def draw(self, image):
        raise NotImplementedError

class Square(Shape):
    
    def __init__(self, x, y, size, color='red', line_width=2):
        super(Square, self).__init__(x, y, color=color, line_width=line_width)
        self.size = size
        
    def draw(self, image):
        image.set_stroke_color(color_dict[self.color])
        image.set_line_width(self.line_width)
        
        image.move_to(self.x, self.y)
        image.line_to(self.x+self.size, self.y)
        image.line_to(self.x+self.size, self.y+self.size)
        image.line_to(self.x, self.y+self.size)

        image.close_path()
        image.stroke_path()
        
class Rectangle(Shape):
    
    def __init__(self, x, y, width, height, color='red', line_width=2):
        super(Rectangle, self).__init__(x, y, color=color, line_width=line_width)
        self.width = width 
        self.height = height
        
    def draw(self, image):
        image.set_stroke_color(color_dict[self.color])
        image.set_line_width(self.line_width)
        
        image.move_to(self.x, self.y)
        image.line_to(self.x+self.width, self.y)
        image.line_to(self.x+self.width, self.y+self.height)
        image.line_to(self.x, self.y+self.height)

        image.close_path()
        image.stroke_path()

class Line(Shape):
    
    def __init__(self, x1, y1, x2, y2, color='red', line_width=2):
        super(Line, self).__init__(x1, y1, color=color, line_width=line_width)
        self.x2 = x2 
        self.y2 = y2
        
    def draw(self, image):
        image.set_stroke_color(color_dict[self.color])
        image.set_line_width(self.line_width)
        
        image.move_to(self.x, self.y)
        image.line_to(self.x2, self.y2)
        
        image.stroke_path()

class Rectangle(Shape):
    
    def __init__(self, x, y, width, height, color='red', line_width=2):
        super(Rectangle, self).__init__(x, y, color=color, line_width=line_width)
        self.width = width 
        self.height = height
        
    def draw(self, image):
        image.set_stroke_color(color_dict[self.color])
        image.set_line_width(self.line_width)
        
        image.move_to(self.x, self.y)
        image.line_to(self.x+self.width, self.y)
        image.line_to(self.x+self.width, self.y+self.height)
        image.line_to(self.x, self.y+self.height)

        image.close_path()
        image.stroke_path()

class Circle(Shape):
    
    def __init__(self, x, y, radius, color='red', line_width=2):
        super(Circle, self).__init__(x, y, color=color, line_width=line_width)
        self.radius = radius
        
    def draw(self, image):
        image.set_stroke_color(color_dict[self.color])
        image.set_line_width(self.line_width)
        
        image.arc(self.x, self.y, self.radius, 0, 6.28318)
        image.close_path()
        image.stroke_path()

# Create an image that we can draw our shapes into
image_size = (300,300)
image = Image(image_size)

# Create a box and add it to the image.
box = Square(30, 30, 100, color='green')
box.draw(image)

line = Line(50, 250, 250, 50)
line.draw(image)

rect = Rectangle( 50, 50, 30, 50)        
rect.draw(image)

circle = Circle( 150, 150, 60, color='blue')        
circle.draw(image)

# Save the image out as a png image.
image.save('shapes.png')
