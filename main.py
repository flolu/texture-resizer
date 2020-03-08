import sys
import os

from process import process_image

print('\n')

input_path = sys.argv[1]
if os.path.isdir(input_path):
  print(f'passing directory as input is currently not supported')

if os.path.isfile(input_path):
  process_image(input_path)
else:
  exit
