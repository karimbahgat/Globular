
from globular.obj import dumps_texture_mtl, dumps_trimesh
from globular.sphere import generate_sphere_faces
from globular.mesh import merge_meshes

# generate sphere
meshes = generate_sphere_faces(resolution=20)
mesh = merge_meshes(*meshes)

# offset to a slightly larger sphere
from globular.vector import Vector
from random import uniform
cloud_height = 1.2
mesh.vertices = [(Vector(*v) * cloud_height).array()
                for v in mesh.vertices]

# add in sphere texture coordinates
from globular.vector import Vector
from globular.sphere import point_to_coordinate
from PIL import Image
mesh.texture_coordinates = [point_to_coordinate(Vector(*v))
                            for v in mesh.vertices]

# write to file
with open('test_sphere_texture_with_clouds.obj', 'w') as fobj:
    raw = dumps_trimesh(mesh, name='clouds', material='clouds', 
                        mtl_file='test_sphere_texture_with_clouds.mtl')
    fobj.write(raw)

with open('test_sphere_texture_with_clouds.mtl', 'w') as fobj:
    raw = dumps_texture_mtl(clouds={#'Ka':'1.0 1.0 1.0',
                                        #'Kd':'0.705882 0.000000 0.000000',
                                        #'Ks':'0.700000 0 0',
                                        #'Ke':'0.000000 0.000000 0.000000',
                                        #'Ns':50.0,
                                        #'Ni':'1.450000',
                                        'illum':2,
                                        #'d':'0.5',
                                        #'map_Kd':'cloud_combined_2048.png',
                                        'map_d':'cloud_combined_2048.png',
                                        })
    fobj.write(raw)
