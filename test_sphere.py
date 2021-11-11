
from globular.obj import dumps_trimesh
from globular.sphere import generate_sphere_faces
from globular.mesh import merge_meshes

meshes = generate_sphere_faces(resolution=10)
mesh = merge_meshes(*meshes)

with open('test_sphere.obj', 'w') as fobj:
    raw = dumps_trimesh(mesh)
    fobj.write(raw)
