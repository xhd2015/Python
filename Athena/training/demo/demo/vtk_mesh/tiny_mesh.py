#!/usr/local/bin/python
import os

### SETUP
from vtk import *

# create a renderer
renderer = vtkRenderer()

# create a render window and hand it the renderer
render_window = vtkRenderWindow()
render_window.AddRenderer(renderer)
render_window.SetSize(300,300)
#render_window.StereoCapableWindowOn()

# create interactor and hand it the render window
# This handles mouse interaction with window.
interactor = vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

### DATA
points = [[0,0,0,10],
          [1,0,0,20],
          [0,1,0,20],
          [0,0,1,30]]

triangles = [[0,1,3],
             [0,3,2],
             [1,2,3],
             [0,2,1]]

### PIPELINE
# Convert list of points to VTK structure
verts = vtkPoints()        
temperature = vtkFloatArray()
for p in points:           
	verts.InsertNextPoint(p[0],p[1],p[2])
	temperature.InsertNextValue(p[3])

# Define triangular cells from the vertex 
# "ids" (index) and append to polygon list.
polygons = vtkCellArray()
for tri in triangles:
	cell = vtkIdList()
	cell.InsertNextId(tri[0])
	cell.InsertNextId(tri[1])
	cell.InsertNextId(tri[2])
	polygons.InsertNextCell(cell)
	

# Create a mesh from these lists
mesh = vtkPolyData()
mesh.SetPoints(verts)
mesh.SetPolys(polygons)
mesh.GetPointData().SetScalars(temperature)


# Set the mapper to scale temperature range 
# across the entire range of colors
mapper = vtkPolyDataMapper()
mapper.SetInput(mesh)
mapper.SetScalarRange(temperature.GetRange())

# Create a scalar bar
scalarBar = vtkScalarBarActor()
scalarBar.SetLookupTable(mapper.GetLookupTable())
scalarBar.SetTitle("Temperature")
scalarBar.GetPositionCoordinate().SetCoordinateSystemToNormalizedViewport()
scalarBar.GetPositionCoordinate().SetValue(0.1, 0.01)
scalarBar.SetOrientationToHorizontal()
scalarBar.SetWidth(0.8)
scalarBar.SetHeight(0.17)
        
        
actor = vtkActor()
actor.SetMapper(mapper)
renderer.AddActor(actor)
renderer.AddActor2D(scalarBar)
interactor.Initialize()
interactor.Start()
