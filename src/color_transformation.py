import cv2
import numpy as np


def color_transfer(source_image, target_image):
    const_LMS_array = np.matrix([[0.3811, 0.5783, 0.0402],
                                 [0.1967, 0.7244, 0.0782],
                                 [0.0241, 0.1288, 0.8444]])

    LMS_source = np.empty(source_image.shape)
    LMS_target = np.empty(target_image.shape)

    for y in range(source_image.shape[0]):
        for x in range(source_image.shape[1]):
            source_pixel = source_image[y][x]
            LMS_source[y][x] = const_LMS_array @ source_pixel
            LMS_source[y][x] = [1 if p == 0 else p for p in LMS_source[y][x]]

            # *******************************************

    for y in range(target_image.shape[0]):
        for x in range(target_image.shape[1]):
            target_pixel = target_image[y][x]
            LMS_target[y][x] = const_LMS_array @ target_pixel
            LMS_target[y][x] = [1 if p == 0 else p for p in LMS_target[y][x]]

    LMS_source = logarithmic_space_converter(LMS_source)
    LMS_target = logarithmic_space_converter(LMS_target)

    LAB_source = LMS_2_LAB(LMS_source)
    LAB_target = LMS_2_LAB(LMS_target)

    LAB_pixels = LAB_pixel_converter(LAB_source, LAB_target)

    LMS = LAB_2_LMS(LAB_pixels)

    LMS_linear_space = linear_space_converter(LMS)

    RGB = LMS_2_RGB(LMS_linear_space)

    result_BGR(RGB)


def logarithmic_space_converter(LMS):
    return np.log10(LMS)


def LMS_2_LAB(LMS):
    const_LAB_array_1 = np.matrix([[1 / np.sqrt(3), 0, 0],
                                   [0, 1 / np.sqrt(6), 0],
                                   [0, 0, 1 / np.sqrt(2)]])

    const_LAB_array_2 = np.matrix([[1, 1, 1],
                                   [1, 1, -2],
                                   [1, -1, 0]])

    const_product = const_LAB_array_1 @ const_LAB_array_2

    LAB = np.empty(LMS.shape)

    for y in range(LAB.shape[0]):
        for x in range(LAB.shape[1]):
            LAB[y][x] = const_product @ LMS[y][x]

    return LAB


def LAB_pixel_converter(LAB_source, LAB_target):
    L_source_mean, A_source_mean, B_source_mean = mean_calculator(LAB_source)
    L_target_mean, A_target_mean, B_target_mean = mean_calculator(LAB_target)

    L_source_std, A_source_std, B_source_std = std_calculator(LAB_source)
    L_target_std, A_target_std, B_target_std = std_calculator(LAB_target)

    L_star = LAB_source[:, :, 0] - L_source_mean
    A_star = LAB_source[:, :, 1] - A_source_mean
    B_star = LAB_source[:, :, 2] - B_source_mean

    L_app = (L_target_std / L_source_std) * L_star
    A_app = (A_target_std / A_source_std) * A_star
    B_app = (B_target_std / B_source_std) * B_star

    L_scd = L_app + L_target_mean
    A_scd = A_app + A_target_mean
    B_scd = B_app + B_target_mean

    new_LAB = np.empty(LAB_source.shape)

    new_LAB[:, :, 0] = L_scd
    new_LAB[:, :, 1] = A_scd
    new_LAB[:, :, 2] = B_scd

    return new_LAB


def mean_calculator(LAB):
    L_mean = np.mean(LAB[:, :, 0])
    A_mean = np.mean(LAB[:, :, 1])
    B_mean = np.mean(LAB[:, :, 2])

    return L_mean, A_mean, B_mean


def std_calculator(LAB):
    L_std = np.std(LAB[:, :, 0])
    A_std = np.std(LAB[:, :, 1])
    B_std = np.std(LAB[:, :, 2])

    return L_std, A_std, B_std


def LAB_2_LMS(LAB):
    const_LAB_array_1 = np.matrix([[1, 1, 1],
                                   [1, 1, -1],
                                   [1, -2, 0]])

    const_LAB_array_2 = np.matrix([[1 / np.sqrt(3), 0, 0],
                                   [0, 1 / np.sqrt(6), 0],
                                   [0, 0, 1 / np.sqrt(2)]])

    const_product = const_LAB_array_1 @ const_LAB_array_2

    LMS = np.empty(LAB.shape)

    for y in range(LAB.shape[0]):
        for x in range(LAB.shape[1]):
            LMS[y][x] = const_product @ LAB[y][x]

    return LMS


def linear_space_converter(LMS):
    LMS[:, :, 0] = np.power(10, LMS[:, :, 0])
    LMS[:, :, 1] = np.power(10, LMS[:, :, 1])
    LMS[:, :, 2] = np.power(10, LMS[:, :, 2])

    return LMS


def LMS_2_RGB(LMS):
    const_LMS_array = np.matrix([[4.4679, -3.5873, 0.1193],
                                 [-1.2186, 2.3809, -0.1624],
                                 [0.0497, -0.2439, 1.2045]])

    for y in range(LMS.shape[0]):
        for x in range(LMS.shape[1]):
            LMS[y][x] = const_LMS_array @ LMS[y][x]

    return LMS


def result_BGR(RGB):
    BGR = RGB[:, :, ::-1]

    cv2.imwrite("OUTPUT.png", BGR)
