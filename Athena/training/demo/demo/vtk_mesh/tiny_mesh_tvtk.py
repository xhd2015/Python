#!/usr/local/bin/python
import os
from numpy import array

### SETUP
from tvtk.api import tvtk

### Simple render/render_window/interactor class
### to simplify things.  It should be moved out of this module
class SimpleVtkWindow(tvtk.RenderWindowInteractor):
       
    def __init__(self, size=(300,300), obj=None, update=True):
        tvtk.RenderWindowInteractor.__init__(self, obj, update)
        
        # create a renderer
        self.renderer = tvtk.Renderer()
        
        # create a render window and hand it the renderer
        self.render_window = tvtk.RenderWindow()
        self.render_window.add_renderer(self.renderer)
        self.render_window.size = size
        
        self.initialize()
        # self.start()

    def add_actor(self, actor):
        self.renderer.add_actor(actor)
        # update window here.


### DATA
points = array([[0,0,0,10],
                [1,0,0,20],
                [0,1,0,20],
                [0,0,1,30]])

triangles = array([[0,1,3],
                   [0,3,2],
                   [1,2,3],
                   [0,2,1]])

### PIPELINE
# Convert list of points to VTK structure
verts = tvtk.Points()        
temperature = tvtk.FloatArray()
for p in points:           
	verts.insert_next_point(p[0],p[1],p[2])
	temperature.insert_next_value(p[3])

# Define triangular cells from the vertex 
# "ids" (index) and append to polygon list.
polygons = tvtk.CellArray()
for tri in triangles:
	cell = tvtk.IdList()
	cell.insert_next_id(tri[0])
	cell.insert_next_id(tri[1])
	cell.insert_next_id(tri[2])
	polygons.insert_next_cell(cell)
	

# Create a mesh from these lists
mesh = tvtk.PolyData()
mesh.points = verts
mesh.polys = polygons
mesh.point_data.scalars = temperature


# Set the mapper to scale temperature range 
# across the entire range of colors
mapper = tvtk.PolyDataMapper()
mapper.input = mesh
mapper.scalar_range = temperature.range

# Create a scalar bar
scalar_bar = tvtk.ScalarBarActor()
scalar_bar.lookup_table = mapper.lookup_table
scalar_bar.title = "Temperature"
scalar_bar.position_coordinate.coordinate_system = 'normalized_viewport'
scalar_bar.position_coordinate.value = 0.1, 0.01, 0.0
scalar_bar.orientation = "horizontal"
scalar_bar.width = 0.8
scalar_bar.height = 0.17
               
actor = tvtk.Actor()
actor.mapper = mapper
                                
window = SimpleVtkWindow()
window.add_actor(actor)
window.add_actor(scalar_bar)    
window.start()
