# -*-coding:utf-8 -*-

# import tensorflow as tf
import numpy as np
import os


usr_face_dir = '/Users/zhang/faceset/'
def get_face_labels(file_dir):
    usr_0 = []
    lable_usr_0 = []
    usr_1 = []
    lable_usr_1 = []
    usr_2 = []
    lable_usr_2 = []
    usr_3 = []
    lable_usr_3 = []
    usr_4 = []
    lable_usr_4 = []
    for face_pic in os.listdir(file_dir):
        name, list_name = face_pic.split('_')
        # id = re.findall(r"\d", name)
        # label_usr_id.append(id)
        if name == "usr0":
            usr_0.append(file_dir + face_pic)
            lable_usr_0.append(0)
        elif name == "usr1":
            usr_1.append(file_dir + face_pic)
            lable_usr_1.append(1)
        elif name == "usr2":
            usr_2.append(file_dir + face_pic)
            lable_usr_2.append(2)
        elif name == "usr3":
            usr_3.append(file_dir + face_pic)
            lable_usr_3.append(3)
        elif name == "usr4":
            usr_4.append(file_dir + face_pic)
            lable_usr_4.append(4)
    
    print("usr0 pic number:%d"%len(usr_0))
    print("usr1 pic number:%d"%len(usr_1))
    print("usr2 pic number:%d"%len(usr_2))
    print("usr3 pic number:%d"%len(usr_3))
    print("usr4 pic number:%d"%len(usr_4))


    #将所有文件路径转化为一维数组；将所有人脸标签转化为一维数组
    face_pic_list = np.hstack((usr_0, usr_1, usr_2, usr_3, usr_4))
    face_label_list = np.hstack((lable_usr_0, lable_usr_1, lable_usr_2, lable_usr_3, lable_usr_4))
     
     #将人脸图像和标签映射，形成第一列为图像位置，第二列为标签的数组，并按行打乱顺序
    temp = np.array([face_pic_list, face_label_list])
    temp = temp.transpose()
    np.random.shuffle(temp)
    
    #返回已经打乱顺序的图片路径和标签，但映射关系不变
    face_pic_list = list(temp[:,0])
    face_label_list = list(temp[:, 1])
    face_label_list = [int(i) for i in label_list]      #将元素从字符转换成int

    return face_pic_list, face_label_list

# if __name__ == '__main__':
#     get_face_labels(usr_face_dir)