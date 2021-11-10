'''
Data structures for mesh data.
'''

import numpy as np

class MeshData(object):
    
    def __init__(self, vertices, triangles):
        self.vertices = np.array(vertices)
        self.triangles = np.array(triangles)

def merge_meshes(*meshes):
    #vertices = np.concatenate([mesh.vertices for mesh in meshes])
    vertices = []
    triangles = []
    for mesh in meshes:
        triangles.extend(mesh.triangles + len(vertices)) # offset to new position
        vertices.extend(mesh.vertices)
    return MeshData(vertices, triangles)
