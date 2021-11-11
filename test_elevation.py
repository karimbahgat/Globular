
from globular.obj import dumps_trimesh
from globular.sphere import generate_sphere_faces
from globular.mesh import merge_meshes

meshes = generate_sphere_faces(resolution=50)
mesh = merge_meshes(*meshes)

# randomly perturb length of each vertex
#from globular.vector import Vector
#from random import uniform
#perturb = 0.1
#mesh.vertices = [(Vector(*v) * uniform(1-perturb, 1+perturb)).array()
#                for v in mesh.vertices]

# load elevation from elevation data
from globular.vector import Vector
from globular.sphere import point_to_coordinate
from PIL import Image
import numpy as np
scale = 0.2
heightmap = np.array(Image.open('land_shallow_topo_2048.png'))[:,:,1] # green band
heightmap = heightmap / heightmap.max() * scale
vertices = [Vector(*v)
            for v in mesh.vertices]
coordinates = [point_to_coordinate(v) for v in vertices]
coordinates = [(u if not np.isnan(u) else 1, v if not np.isnan(v) else 1)
                for u,v in coordinates]
pixels = [(int(1-(heightmap.shape[1]-1)*u), int((heightmap.shape[0]-1)*v))
            for u,v in coordinates]
heights = [heightmap[py,px] for px,py in pixels]
mesh.vertices = [(v + v*h).array()
                for v,h in zip(vertices,heights)]

with open('test_elevation.obj', 'w') as fobj:
    raw = dumps_trimesh(mesh)
    fobj.write(raw)
