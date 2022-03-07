'''
Prep the very large GEBCO 2021 elevation data, 
by extracting tiled files and downsampling. 
'''

from zipfile import ZipFile
from io import BytesIO
from PIL import Image
Image.MAX_IMAGE_PIXELS = 999999999999999999

path = r'C:\Users\kimok\Downloads\gebco_2021_geotiff.zip'

import transformio as tio
size = 10000,5000
bounds = [-180,90,180,-90]
coord2pixel = tio.imwarp.fitbounds(size[0], size[1], bounds).inverse()
target = Image.new('I', size, 0)

archive = ZipFile(path)
for fil in archive.namelist():
    if fil.endswith('.tif'):
        print(fil)
        meta = fil.replace('.tif','').split('_')[2:]
        n,s,w,e = [float(_[1:]) for _ in meta]
        print(w,n,e,s)
        [px1],[py1] = coord2pixel.predict([w], [n])
        [px2],[py2] = coord2pixel.predict([e], [s])
        px1,py1,px2,py2 = map(int, (px1,py1,px2,py2))
        print(px1,py1,px2,py2)
        nw = abs(px2-px1)
        nh = abs(py2-py1)
        print(nw,nh)
        with archive.open(fil) as fobj:
            fobj2 = BytesIO(fobj.read())
            print('raw',fobj2)
            im = Image.open(fobj2)
            print(im)
            small = im.resize((nw,nh), Image.NEAREST)
            print(small)
            target.paste(small, box=(px1,py1,px2,py2))

target.save('gebco_2021_geotiff_small.tif')

