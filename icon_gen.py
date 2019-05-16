import argparse
import os
import shutil
from PIL import Image


icon_ratios = [1, 1.5, 2, 3, 4]

icon_locations = ['mipmap-mdpi', 'mipmap-hdpi', 'mipmap-xhdpi',
                  'mipmap-xxhdpi', 'mipmap-xxxhdpi']

icon_name = "ic_launcher.png"

lowest_resolution = 48


def resize_image(src_path, destination, img_ratio, img_location):
    icon_img = Image.open(src_path)

    w, h = icon_img.size
    if w != h:
        exit("Image is not a square!")

    img_size = int(lowest_resolution * img_ratio)

    resized_icon = icon_img.resize((img_size, img_size), Image.LANCZOS)
    resized_icon_dir = destination + img_location

    if os.path.exists(resized_icon_dir):
        shutil.rmtree(resized_icon_dir)
    os.makedirs(resized_icon_dir)

    resized_icon.save(resized_icon_dir + '/' + icon_name, quality=100)


def main():
    # arguments parsing
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Img path")
    args = vars(ap.parse_args())

    src = args["image"]

    # check if path is valid
    if not(os.path.exists(src)):
        exit("Path invalid!")

    # check if file is image
    
    # creating path
    destination = ''
    if os.path.dirname(src) == '':
        destination = './'

    destination += os.path.dirname(src) + "/res/"
    print("Generating at " + "'" + os.path.dirname(src) + "'")

    # generating icons
    for icon_ratio, icon_location in zip(icon_ratios, icon_locations):
        resize_image(src, destination, icon_ratio, icon_location)
        print(icon_location + ' generated.')


if __name__ == "__main__":
    main()