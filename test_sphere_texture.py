
from globular.obj import dumps_texture_mtl, dumps_trimesh
from globular.sphere import generate_sphere_faces
from globular.mesh import merge_meshes

# generate sphere
meshes = generate_sphere_faces(resolution=20)
mesh = merge_meshes(*meshes)

# randomly perturb length of each vertex
#from globular.vector import Vector
#from random import uniform
#perturb = 0.1
#mesh.vertices = [(Vector(*v) * uniform(1-perturb, 1+perturb)).array()
#                for v in mesh.vertices]

# add in sphere texture coordinates
from globular.vector import Vector
from globular.sphere import point_to_coordinate
from PIL import Image
mesh.texture_coordinates = [point_to_coordinate(Vector(*v))
                            for v in mesh.vertices]

# write to file
with open('test_sphere_texture.obj', 'w') as fobj:
    raw = dumps_trimesh(mesh, name='globe', material='bluemarble', mtl_file='test_sphere_texture.mtl')
    fobj.write(raw)

with open('test_sphere_texture.mtl', 'w') as fobj:
    raw = dumps_texture_mtl(bluemarble={'Ka':'1.0 1.0 1.0',
                                        'Kd':'1.0 1.0 1.0',
                                        'Ks':'1.0 1.0 1.0',
                                        'Tr':'0.5',
                                        'illum':1,
                                        'Ns':0.0,
                                        'map_Kd':'land_shallow_topo_2048.png',
                                        })
    fobj.write(raw)
