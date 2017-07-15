import sys, os
import cv2

pic_path = ""


def walk_dir(dir):
    image_list = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            ext = os.path.splitext(name)[1][1:]
            if (ext.lower() == 'jpg'):
                path = root + os.sep + name
                image_list.append(path)
    return image_list

def auto_resize(img):
    reImg = cv2.resize(img, (32,32),interpolation = cv2.INTER_CUBIC)
    return reImg

def resize_save(img, path):
    image_name = img.filename.split(os.sep)[-1]
    save_name = path + os.sep + image_name
    new_im = auto_resize(img)
    print save_name
    new_im.save(save_name)