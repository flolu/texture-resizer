from PIL import Image
import time
import math
import os

Image.MAX_IMAGE_PIXELS = 933120000

def resize(image, name, size):
  start_time = time.time()

  print(f'\tresize to {str(size)}px')
  # TODO support for .exr
  resized = image.resize((size, size), Image.ANTIALIAS)

  OUT_DIR_NAME = 'out'
  out_directory = f'./{OUT_DIR_NAME}/'
  out_path = f'{out_directory}/{name}_{str(size)}px.jpg'
  if not os.path.exists(out_directory):
    os.makedirs(out_directory)
  print(f'\tsave to {out_path}')
  resized.save(out_path)

  elapsed_time = time.time() - start_time
  print(f'\tdone in {round(elapsed_time)}s')