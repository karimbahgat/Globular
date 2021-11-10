'''
Read and write .obj files.
'''

from .mesh import MeshData

def loads(raw):
    raise NotImplementedError()

def dumps_trimesh(mesh):
    raw = ''
    for xyz in mesh.vertices:
        xyz = map(float, xyz)
        raw += 'v {} {} {}\n'.format(*xyz)
    for tri in (mesh.triangles + 1): # from 0 to 1 indexing
        tri = map(int, tri)
        raw += 'f {} {} {}\n'.format(*tri)
    return raw
