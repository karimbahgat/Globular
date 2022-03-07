'''
Read and write .obj files.
'''

from .mesh import MeshData

def loads(raw):
    raise NotImplementedError()

def dumps_trimesh(mesh, name=None, material=None, mtl_file=None):
    raw = ''
    # define material
    if mtl_file:
        raw += 'mtllib {}\n'.format(mtl_file)
    if material:
        raw += 'usemtl {}\n'.format(material)
    # define the mesh object data
    if name:
        raw += 'o {}\n'.format(name)
    for xyz in mesh.vertices:
        raw += 'v {} {} {}\n'.format(*xyz)
    if mesh.texture_coordinates is None:
        # no texture
        for tri in (mesh.triangles + 1): # from 0 to 1 indexing
            tri = map(int, tri)
            raw += 'f {} {} {}\n'.format(*tri)
    else:
        # texture
        for tcoord in mesh.texture_coordinates:
            tcoord = map(str, tcoord)
            raw += 'vt {}\n'.format(' '.join(tcoord))
        for tri in (mesh.triangles + 1): # from 0 to 1 indexing
            # each face defined by {vertex index} / {texture coordinate index}
            # for now assume equally many of both, so therefore 1-1 correspondence
            tri = map(int, tri)
            raw += 'f {0}/{0} {1}/{1} {2}/{2}\n'.format(*tri)
    return raw

def dumps_texture_mtl(**texture_opts):
    raw = ''
    # export texture options to mtl file
    for name,opts in texture_opts.items():
        raw += 'newmtl {}\n'.format(name)
        for k,v in opts.items():
            raw += '{} {}\n'.format(k,v)
    return raw

