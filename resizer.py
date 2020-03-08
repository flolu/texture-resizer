import sys
import os
import time

from PIL import Image
from termcolor import colored

Image.MAX_IMAGE_PIXELS = 933120000

start_time = time.time()
print('\n')

image_path = sys.argv[1]
# TODO get filename
image_name = os.path.splitext(os.path.basename(image_path))[0]
# TODO support multiple input images
raw = Image.open(image_path)
image_size = raw.size[0]

if image_size != raw.size[1]:
  raise Exception(colored(f"input image should be a square, but {image_name} is {str(image_size)}x{str(raw.size[1])} in size", 'red'))

SMALLEST_SIZE = 2 ** 10
def get_size_in_pixels(k):
  return SMALLEST_SIZE * k

if image_size < SMALLEST_SIZE:
  raise Exception(colored(f'input image has to be at lest {SMALLEST_SIZE}px in size, but {image_name} is {image_size}px', 'red'))

print(f"process {colored(image_name, 'green')} ({image_size}px)")

sizes = []
i = 1
while get_size_in_pixels(i) <= image_size:
  sizes.append(i)
  i *= 2

print(f"convert to: {', '.join(str(f'{get_size_in_pixels(s)}px') for s in sizes)}\n")

for size in sizes:
  start = time.time()
  print(f'resize {str(size)}k')
  # TODO don't encode color if its a b/w texture
  resized = raw.resize((get_size_in_pixels(size), get_size_in_pixels(size)), Image.ANTIALIAS)
  resized.save(f'./out/{image_name}_{str(size)}k.jpg')
  elapsed = time.time() - start
  print(f'done in {round(elapsed)}s\n')

elapsed_time = time.time() - start_time
print(f'\nfinished converting {len(sizes)} textures in {round(elapsed_time)}s')