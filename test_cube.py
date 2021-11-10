
from globular.obj import dumps_trimesh
from globular.sphere import generate_cube_faces
from globular.mesh import merge_meshes

meshes = generate_cube_faces(resolution=20)
mesh = merge_meshes(*meshes)

with open('test_cube.obj', 'w') as fobj:
    raw = dumps_trimesh(mesh)
    fobj.write(raw)
