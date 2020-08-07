from PIL import Image
from termcolor import colored
import time
import os

from resize import resize

def process_image(image_path):
  start_time = time.time()

  print(f'process image: {image_path}')

  image = Image.open(image_path)
  fullname = os.path.basename(image_path)
  name = os.path.splitext(fullname)[0]
  image_size = image.size[0]

  if image_size != image.size[1]:
    print(colored(f'skip processing {name} because its dimension is not a square (it is {str(image_size)}x{str(image.size[1])}px)', 'yellow'))
    print('\n')
    return

  SMALLEST_SIZE = 2**12 # 4096

  if image_size < SMALLEST_SIZE:
    print(colored(f'skip processing {name} because it is smaller than {SMALLEST_SIZE}px (it is {str(image_size)}px)', 'yellow'))
    print('\n')
    return

  print(f"\n• process {colored(fullname, 'cyan')}")

  sizes = []
  s = SMALLEST_SIZE
  while s <= image_size:
    sizes.append(s)
    s *= 2

  sizes.reverse()

  for size in sizes:
    resize(image, name, size)

  elapsed_time = time.time() - start_time
  print(f"✓ processing {colored(fullname, 'green')} done in {round(elapsed_time)}s")