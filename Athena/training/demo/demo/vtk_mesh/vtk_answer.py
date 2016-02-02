#!/usr/local/bin/python
from vtk import vtkRenderer, vtkRenderWindow, vtkRenderWindowInteractor, \
    vtkActor, vtkPolyDataMapper
from mesh_from_file import read_mesh, vtk_mesh

# !!! Import randn from scipy
from numpy.random import random

### Read and morph mesh
# Read input file
points, triangles = read_mesh('cylinder2.tpm')

# !!! Now add some noise
# perturb points by gaussian noise with variance=0.02
points += random(len(points)) * .02
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
render_window.SetSize(300, 300)

# create interactor and hand it the render window
# This handles mouse interaction with window.
interactor = vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Finally, display the actor
renderer.AddActor(actor)
interactor.Initialize()
interactor.Start()
