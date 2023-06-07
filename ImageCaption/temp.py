'''测试文件屁用没有'''
import streamlit as st
import os
import shutil

def read_parameters(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()

    # 解析参数
    param1 = lines[0].strip()
    param2 = lines[1].strip()

    return param1, param2
txt_filepath = './file.txt'
param1, param2 = read_parameters(txt_filepath)
param2=int(param2)
print(param1)
print(param2)

#shutil.copy('./NewImages/', './temp/')
source_folder=param1
for i in range(1,param2+1):
    shutil.copy('./NewImages/' + f"{i}.jpg", param1+'/'+ f"{i}.jpg")
    print(i)