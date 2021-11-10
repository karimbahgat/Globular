'''
Creating a sphere consisting of faces and triangular meshes.
'''

from .vector import Vector
from .mesh import MeshData

import numpy as np

def create_face(normal, resolution):
    axisA = Vector(normal.y, normal.z, normal.x)
    axisB = normal.cross(axisA)
    vertices = []
    triangles = []

    for y in range(resolution):
        for x in range(resolution):
            vertex_index = x + y * resolution
            tx = x / (resolution - 1)
            ty = y / (resolution - 1)
            point = normal + axisA * (2*tx-1) + axisB * (2*ty-1)
            vertices.append(point.array())

            if x != (resolution - 1) and y != (resolution - 1):
                triangles.append([vertex_index,
                                vertex_index + resolution + 1,
                                vertex_index + resolution])
                triangles.append([vertex_index,
                                vertex_index + 1,
                                vertex_index + resolution + 1])

    return MeshData(vertices, triangles)

def generate_cube_faces(resolution):
    all_meshes = []
    face_normals = [Vector.up(),
                    Vector.down(),
                    Vector.left(),
                    Vector.right(),
                    Vector.forward(),
                    Vector.back()]
    for normal in face_normals:
        face_mesh = create_face(normal, resolution)
        all_meshes.append(face_mesh)

    return all_meshes

def cube_to_sphere(p):
    return p.normalize()

def generate_sphere_faces(resolution):
    all_meshes = generate_cube_faces(resolution)
    for mesh in all_meshes:
        mesh.vertices = np.array([cube_to_sphere(Vector(*v)).array() for v in mesh.vertices])
    return all_meshes
