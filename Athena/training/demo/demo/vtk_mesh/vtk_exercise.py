#!/usr/local/bin/python
# This file reads in a cylindrical mesh and displays it.
#
# Try adding some noise to the vertices read in from the data file using
# scipy.randn function.  Using noise with a variance of 0.02 will do
# nicely.  You can check out vtk_answer.py to see one approach.

from vtk import vtkRenderer, vtkRenderWindow, vtkRenderWindowInteractor,\
                vtkActor, vtkPolyDataMapper
from mesh_from_file import read_mesh, vtk_mesh

### Read and morph mesh
# Read input file
points, triangles = read_mesh('cylinder2.tpm')
mesh = vtk_mesh(points, triangles)

### Feed mesh into mapper 
mapper = vtkPolyDataMapper()
mapper.SetInput(mesh)

### And finally build an actor to be displayed.
actor = vtkActor()
actor.SetMapper(mapper)

### Set up render window to display the actor
# create a renderer
renderer = vtkRenderer()

# create a render window and hand it the renderer
render_window = vtkRenderWindow()
render_window.AddRenderer(renderer)
render_window.SetSize(300,300)

# create interactor and hand it the render window
# This handles mouse interaction with window.
interactor = vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Finally, display the actor
renderer.AddActor(actor)
interactor.Initialize()
interactor.Start()