from PIL import Image
import time
import math

Image.MAX_IMAGE_PIXELS = 933120000

def resize(image, name, size):
  start_time = time.time()

  print(f'\n\tresize to {str(size)}px')
  # TODO don't encode color if its a b/w texture
  resized = image.resize((size, size), Image.ANTIALIAS)

  out_path = f'./out/{name}_{str(size)}px.jpg'
  print(f'\tsave to {out_path}')
  resized.save(out_path)

  elapsed_time = time.time() - start_time
  print(f'\tdone in {round(elapsed_time)}s\n')