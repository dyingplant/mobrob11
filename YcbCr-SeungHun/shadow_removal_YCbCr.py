import numpy as np
import cv2
import os
import glob

def remove_shadow(image_path):

    or_img = cv2.imread(image_path)
    y_cb_cr_img = cv2.cvtColor(or_img, cv2.COLOR_BGR2YCrCb)

    binary_mask = np.copy(y_cb_cr_img)

    y_mean = np.mean(cv2.split(y_cb_cr_img)[0])

    y_std = np.std(cv2.split(y_cb_cr_img)[0])

  
    for i in range(y_cb_cr_img.shape[0]):
        for j in range(y_cb_cr_img.shape[1]):
            if y_cb_cr_img[i, j, 0] < y_mean - (y_std / 3):
                binary_mask[i, j] = [255, 255, 255]
            else:
                binary_mask[i, j] = [0, 0, 0]

 
    kernel = np.ones((3, 3), np.uint8)
    erosion = cv2.erode(binary_mask, kernel, iterations=1)

    spi_la, spi_s, n_la, n_s = 0, 0, 0, 0

    for i in range(y_cb_cr_img.shape[0]):
        for j in range(y_cb_cr_img.shape[1]):
            if erosion[i, j, 0] == 0 and erosion[i, j, 1] == 0 and erosion[i, j, 2] == 0:
                spi_la += y_cb_cr_img[i, j, 0]
                n_la += 1
            else:
                spi_s += y_cb_cr_img[i, j, 0]
                n_s += 1

    average_ld = spi_la / n_la
    average_le = spi_s / n_s
    i_diff = average_ld - average_le
    ratio_as_al = average_ld / average_le


    for i in range(y_cb_cr_img.shape[0]):
        for j in range(y_cb_cr_img.shape[1]):
            if erosion[i, j, 0] == 255 and erosion[i, j, 1] == 255 and erosion[i, j, 2] == 255:
                y_cb_cr_img[i, j] = [y_cb_cr_img[i, j, 0] + i_diff, y_cb_cr_img[i, j, 1] + ratio_as_al,
                                     y_cb_cr_img[i, j, 2] + ratio_as_al]


    final_image = cv2.cvtColor(y_cb_cr_img, cv2.COLOR_YCR_CB2BGR)
    return final_image


source_directory = '/home/seunghun/Desktop/color_data/00/image_3' #image_3
target_directory = '/home/seunghun/Desktop/color_data/shadow_removed_color_00/image_3' #image_3


if not os.path.exists(target_directory):
    os.makedirs(target_directory)


for image_path in glob.glob(os.path.join(source_directory, '*.png')):
    print(f'Processing {image_path}...')
    processed_image = remove_shadow(image_path)
    base_name = os.path.basename(image_path)
    save_path = os.path.join(target_directory, base_name)
    cv2.imwrite(save_path, processed_image)
    print(f'Saved processed image to {save_path}')
