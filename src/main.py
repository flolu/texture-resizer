import sys
import os
import imghdr

from process import process_image

input_path = sys.argv[1]
if os.path.isdir(input_path):
  all_files = os.listdir(input_path)
  images = []
  for file in all_files:
    full_path = os.path.join(input_path, file)
    if os.path.isfile(full_path) and imghdr.what(full_path):
        images.append(full_path)

  print(f'found {len(images)} images to process\n')

  for image in images:
    process_image(image)

if os.path.isfile(input_path):
  process_image(input_path)
