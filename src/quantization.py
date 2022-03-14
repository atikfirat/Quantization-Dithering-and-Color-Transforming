import cv2
import numpy as np
from dithering import FloydSteinberg


def BGR2GRAY(img):
    gray = 0.21 * img[..., 2] + 0.71 * img[..., 1] + 0.07 * img[..., 0]
    return gray


def quantization(image, q):
    color_space = 255

    quantized_image = np.round(image / (color_space / q)) * (color_space / q)

    cv2.imwrite("Quantization_q={}.png".format(q), quantized_image)

    return quantized_image


def main():

    image_path = "1.png"
    image = cv2.imread(image_path)
    image = BGR2GRAY(image)

    quantization_parameter = 32
    quantization(image, quantization_parameter)

    FloydSteinberg(image, quantization_parameter)


if __name__ == "__main__":
    main()

    
