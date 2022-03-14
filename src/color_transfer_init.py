import cv2

from color_transformation import color_transfer


def main():
    source_image_path = "fallingwater.jpg"
    source_image = cv2.imread(source_image_path)
    source_image = cv2.cvtColor(source_image, cv2.COLOR_BGR2RGB)

    target_image_path = "autumn.jpg"
    target_image = cv2.imread(target_image_path)
    target_image = cv2.cvtColor(target_image, cv2.COLOR_BGR2RGB)

    color_transfer(source_image, target_image)


if __name__ == "__main__":
    main()
