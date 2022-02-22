import cv2
import numpy as np
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--image_path', required=True, help='get_U-2-Net/test_data/test_images_path')
args = parser.parse_args()

def get_files_count(folder_path):
    fileExt = r".jpg"
    jpg_list = [_ for _ in os.listdir(folder_path) if _.endswith(fileExt)]
    return len(jpg_list)
	

image_num = get_files_count(args.image_path)
print(image_num)

#make output_path
result_path = os.path.join(args.image_path + "_mask")
output_path = os.path.join(args.image_path + "_rm_bg")
if not os.path.exists(output_path):
    os.makedirs(output_path, exist_ok=True)
    print(f"output_dir: {output_path}")

#save results
for idx in range(image_num):
  img1 = cv2.imread(os.path.join(args.image_path, str(idx) + '.jpg'))
  mask = cv2.imread(os.path.join(result_path, str(idx) + '.png'))

  mask_inv = cv2.bitwise_not(mask)
  AND_result = cv2.bitwise_and(img1, mask)
  result = cv2.add(mask_inv, AND_result)

  output_dir = os.path.join(output_path, str(idx) + '.png')
  cv2.imwrite(output_dir, result)
  print(f'Masking image {idx} completed.\n')