import cv2
import numpy as np


def FloydSteinberg(image, q):

    height, width = image.shape
    color_space = 255
    for y_coord in range(1, height - 1):
        for x_coord in range(1, width - 1):

            old_pixel = image[y_coord][x_coord]
            new_pixel = np.round(image[y_coord][x_coord] / (color_space / q)) * (color_space / q)
            image[y_coord][x_coord] = new_pixel

            quantization_error = old_pixel - new_pixel

            image[y_coord][x_coord + 1] = image[y_coord][x_coord + 1] + quantization_error * (7 / 16)
            image[y_coord + 1][x_coord - 1] = image[y_coord + 1][x_coord - 1] + quantization_error * (3 / 16)
            image[y_coord + 1][x_coord] = image[y_coord + 1][x_coord] + quantization_error * (5 / 16)
            image[y_coord + 1][x_coord + 1] = image[y_coord + 1][x_coord + 1] + quantization_error * (1 / 16)

    cv2.imwrite("FS_Dithering_q={}.png".format(q), image)
