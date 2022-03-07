
from globular.obj import dumps_trimesh
from globular.sphere import generate_sphere_faces
from globular.mesh import merge_meshes

meshes = generate_sphere_faces(resolution=100)
mesh = merge_meshes(*meshes)

# randomly perturb length of each vertex
#from globular.vector import Vector
#from random import uniform
#perturb = 0.1
#mesh.vertices = [(Vector(*v) * uniform(1-perturb, 1+perturb)).array()
#                for v in mesh.vertices]

# load elevation from elevation data
print('heightmap')
from globular.vector import Vector
from globular.sphere import point_to_coordinate
from PIL import Image
import numpy as np
scale = 0.3
#heightmap = np.array(Image.open('land_shallow_topo_2048.png'))[:,:,1] # green band
heightmap = np.array(Image.open('gebco_2021_geotiff_small.tif'))
print(heightmap.min(), heightmap.max())
heightmap[heightmap < 0] = 0 # clamp at sealevel
heightmap = (heightmap - heightmap.min()) / (heightmap.max() - heightmap.min())
print(heightmap.min(), heightmap.max())
heightmap *= scale
vertices = [Vector(*v)
            for v in mesh.vertices]
coordinates = [point_to_coordinate(v) for v in vertices]
coordinates = [(u if not np.isnan(u) else 1, v if not np.isnan(v) else 1)
                for u,v in coordinates]
pixels = [(int((heightmap.shape[1]-1)*u), int(1-(heightmap.shape[0]-1)*v))
            for u,v in coordinates]
heights = [heightmap[py,px] for px,py in pixels]
mesh.vertices = [(v + v*h).array()
                for v,h in zip(vertices,heights)]

# add in sphere texture coordinates
print('texture')
from globular.vector import Vector
from globular.sphere import point_to_coordinate
from PIL import Image
mesh.texture_coordinates = [point_to_coordinate(Vector(*v))
                            for v in mesh.vertices]

# write to file
print('writing to file')
with open('test_elevation.obj', 'w') as fobj:
    raw = dumps_trimesh(mesh, name='globe', material='bluemarble', mtl_file='test_elevation.mtl')
    print(len(raw))
    fobj.write(raw)

from globular.obj import dumps_texture_mtl, dumps_trimesh
with open('test_elevation.mtl', 'w') as fobj:
    raw = dumps_texture_mtl(bluemarble={'Ka':'1.0 1.0 1.0',
                                        'Kd':'1.0 1.0 1.0',
                                        'Ks':'1.0 1.0 1.0',
                                        'Tr':'0.5',
                                        'illum':1,
                                        'Ns':0.0,
                                        'map_Kd':'land_shallow_topo_2048.png',
                                        })
    fobj.write(raw)
