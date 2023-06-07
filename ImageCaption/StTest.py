'''严格来说这个库应该叫图片展示的，但是这个文件一开始是用来写可视化界面的，一直没改，懒得改了。。。。。。。。'''

import os
import streamlit as st
from PIL import Image



def show_img(src='./NewImages'):
    # 设置文件夹路径
    folder_path = src

    # 获取文件夹中的所有文件名
    file_names = os.listdir(folder_path)

    # 创建一个网格布局
    col1, col2, col3 = st.columns(3)

    # 遍历文件夹中的每个文件
    for i, file_name in enumerate(file_names):
        # 仅处理图片文件
        if file_name.endswith(".jpg") or file_name.endswith(".png"):
            # 拼接文件路径
            file_path = os.path.join(folder_path, file_name)

            # 打开图片并调整大小
            image = Image.open(file_path)
            image.thumbnail((300, 300))  # 调整图片大小

            # 根据索引将图片放入不同的列中
            if i % 3 == 0:
                col1.image(image, caption=file_name, use_column_width=True)
            elif i % 3 == 1:
                col2.image(image, caption=file_name, use_column_width=True)
            else:
                col3.image(image, caption=file_name, use_column_width=True)








if __name__ == '__main__':



    show_img()


















