'''
Data structures for mesh data.
'''

import numpy as np

class MeshData(object):
    
    def __init__(self, vertices, triangles, texture_coordinates=None):
        self.vertices = np.array(vertices)
        self.triangles = np.array(triangles)
        self.texture_coordinates = np.array(texture_coordinates) if texture_coordinates is not None else None

def merge_meshes(*meshes):
    #vertices = np.concatenate([mesh.vertices for mesh in meshes])
    vertices = []
    triangles = []
    texture_coordinates = []
    for mesh in meshes:
        triangles.extend(mesh.triangles + len(vertices)) # offset to new position
        vertices.extend(mesh.vertices)
        if mesh.texture_coordinates is not None:
            texture_coordinates.extend(mesh.texture_coordinates)
    return MeshData(vertices, triangles, texture_coordinates or None)
