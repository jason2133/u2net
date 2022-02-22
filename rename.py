import glob
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--image_path', required=True, help='get U-2-Net/test_data/test_images path')
args = parser.parse_args()

path = args.image_path

# names = glob.glob(path + '/*.jpg')
names = glob.glob(path + '/*')

for idx, name in enumerate(names):
  dst = path + '/' + str(idx) + '.jpg'
  os.rename(name, dst)
