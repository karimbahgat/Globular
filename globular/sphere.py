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

def point_to_coordinate(point, sphere_radius=1):
    u = (np.pi + np.arctan2(point.x, -point.z)) / (2*np.pi)
    v = (np.pi/2.0 + np.arcsin(point.y)) / np.pi
    v = 1 - v # because of inverted image y axis
    #u = np.arctan2(point.x, -point.y) / (2*np.pi)
    #v = np.arcsin(point.z) / np.pi
    #u = np.arctan(point.x / point.y)
    #v = np.arccos(point.z / sphere_radius)
    #u = 0.5 + np.arctan2(point.y, point.x) / (2*np.pi)
    #v = 0.5 + np.arctan2(point.z, sphere_radius) / (2*np.pi)
    return u,v

def sphere_point_height_mapping(point, heightmap):
    lon,lat = point_to_coordinate(point)
    lat_pixel = heightmap.shape[0] * lat
    lon_pixel = heightmap.shape[1] * lon
    height = heightmap[lat_pixel,lon_pixel]
    return height

def sphere_point_texture_mapping(point, texture):
    lon,lat = point_to_coordinate(point)
    lat_pixel = texture.shape[0] * lat
    lon_pixel = texture.shape[1] * lon
    color = texture[lat_pixel,lon_pixel]
    return color
