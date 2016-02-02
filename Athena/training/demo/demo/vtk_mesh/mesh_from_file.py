#!/usr/local/bin/python

from vtk import vtkRenderer, vtkRenderWindow, vtkRenderWindowInteractor,\
                vtkPoints, vtkCellArray, vtkPolyData,vtkActor, \
                vtkPolyDataMapper, vtkScalarBarActor, vtkIdList
from numpy import int32, loadtxt
from cStringIO import StringIO

def read_mesh(file_name):
    
    # First read in the data from the files.
    # The first 2 lines have the number of vertices and
    # triangles within the file.  This is followed by a 
    # vertex coordinate list which is followed the triangle
    # list.
    #
    # format is:
    #
    #   Nvertices
    #   Ntriangles
    #   x1 y1 z1
    #   x2 y2 z2
    #   ...
    #   v11 v12 v13    
    #   v21 v22 v23
    #   ...
    
    data = open(file_name).readlines()
    
    Npoints = int(data[0].split()[0])
    Ntriangles = int(data[1].split()[0])
    
    point_start = 2
    point_end = point_start + Npoints
    points = loadtxt(StringIO("".join(data[point_start:point_end])))
    
    tri_start = point_end
    tri_end = tri_start + Ntriangles
    triangles = loadtxt(StringIO("".join(data[tri_start:tri_end])))
    # The minus one is because the nodes were indexed base 1 in the file
    triangles = triangles.astype(int32) - 1
    return points, triangles
    
def vtk_mesh(points, triangles):    
    # Now set up the VTK objects
    # Convert list of points to VTK structure
    verts = vtkPoints()        
    for p in points:           
    	verts.InsertNextPoint(p[0],p[1],p[2])
    
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
    
    return mesh

if __name__ == "__main__":
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
