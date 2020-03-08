from PIL import Image

Image.MAX_IMAGE_PIXELS = 933120000

# TODO support multiple input images
# TODO pass input image path as flag
raw = Image.open("./raw/tree-trunk_lod0_diffuse.tif")

sizes = [2**10, 2**11, 2**12, 2**13, 2**14]
for size in sizes:
  print('resizing to ' + str(size) + 'px')
  resized = raw.resize((size, size), Image.ANTIALIAS)
  resized.save('./out/tree_trunk_lod0_diffuse_' + str(size) + '.jpg')
  print('resizing to ' + str(size) + 'px done')