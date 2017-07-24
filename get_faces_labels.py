# -*-coding:utf-8 -*-

# import tensorflow as tf
import numpy as np
import os


usr_face_dir = '/Users/zhang/developer/users_face_file/'
def get_face_labels(file_dir):
    usr_face_dir_jpg = []
    usr_face_id = []
    for face_pic in os.listdir(file_dir):
        id, list_name = face_pic.split('_')
        if id == '.DS':     #macOS的锅，总有隐藏文件来捣乱
            continue
        else:
            pass
        usr_face_id.append(int(id))
        usr_face_dir_jpg.append(file_dir + face_pic)


    # #将所有文件路径转化为一维数组；将所有人脸标签转化为一维数组
    face_pic_array = np.hstack(usr_face_dir_jpg)
    face_label_array = np.hstack(usr_face_id)

     #将人脸图像和标签映射，形成第一列为图像位置，第二列为标签的数组，并按行打乱顺序
    temp = np.array([face_pic_array, face_label_array])
    temp = temp.transpose()
    np.random.shuffle(temp)
    
    #返回已经打乱顺序的图片路径和标签，但映射关系不变
    face_pic_list = list(temp[:,0])
    face_label_list = list(temp[:, 1])
    face_label_list = list(int(i) for i in face_label_list)

    return face_pic_list, face_label_list

# if __name__ == '__main__':
#     get_face_labels(usr_face_dir)