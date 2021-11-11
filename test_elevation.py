
from globular.obj import dumps_trimesh
from globular.sphere import generate_sphere_faces
from globular.mesh import merge_meshes

meshes = generate_sphere_faces(resolution=20)
mesh = merge_meshes(*meshes)

# randomly perturb length of each vertex
from globular.vector import Vector
from random import uniform
perturb = 0.1
mesh.vertices = [(Vector(*v) * uniform(1-perturb, 1+perturb)).array()
                for v in mesh.vertices]

with open('test_elevation.obj', 'w') as fobj:
    raw = dumps_trimesh(mesh)
    fobj.write(raw)
