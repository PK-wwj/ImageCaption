import io
import os
import streamlit as st
import requests
from PIL import Image
from model import get_caption_model, generate_caption
from VideoProcess import videoProcess #视频处理模块
from pygtrans import Translate#翻译模块
from GetNewImages import scrape_images
from StTest import show_img
import shutil


#确保模型只加载一次
#@st.cache(allow_output_mutation=True)
@st.cache_resource
def get_model():
    return get_caption_model()

caption_model = get_model()


#记载指定的参数

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

def predict():
    captions = []
    CNcaptions = []
    pred_caption = generate_caption('tmp.jpg', caption_model)

    st.markdown('#### 图片描述:')
    captions.append(pred_caption)

    for _ in range(3):
        pred_caption = generate_caption('tmp.jpg', caption_model, add_noise=True)
        if pred_caption not in captions:
            captions.append(pred_caption)

    for c in captions:
        client = Translate()
        text = client.translate(c)
        print(text.translatedText)
        CNcaptions.append(text.translatedText)
        st.write(text.translatedText)



def predict_getimg():
    captions = []
    CNcaptions = []
    pred_caption = generate_caption('tmp.jpg', caption_model)

    st.markdown('#### 图片描述:')
    captions.append(pred_caption)
    def button_clicked(query_sentence):
        st.write(query_sentence)
        scrape_images(query_sentence,param2)#描述语句，爬取数目，爬取路径
        st.write('爬取成功')
        show_img()
        #将图片存储到指定位置
        for i in range(1, param2 + 1):
            shutil.copy('./NewImages/' + f"{i}.jpg", param1 + '/' + f"{i}.jpg")
            print(i)

    for _ in range(2):
        pred_caption = generate_caption('tmp.jpg', caption_model, add_noise=True)
        if pred_caption not in captions:
            captions.append(pred_caption)

    for c in captions:
        client = Translate()
        text = client.translate(c)
        print(text.translatedText)
        CNcaptions.append(text.translatedText)
   # '''每有一句描述就生成一个按钮''''''enumerate可以同时遍历索引和值'''
    for i, caption in enumerate(captions):
        columns = st.columns([3, 1])
        # 在第一个列中放置文本
        with columns[0]:
            st.write(CNcaptions[i])
        # 在第二个列中放置按钮
        with columns[1]:
            st.write(f'描述{i+1}')
    # 生成按钮
    if st.button("爬取图片"):
        # 按钮被点击时调用指定的函数
        button_clicked(CNcaptions[0])


def video_predict():
    captions = []
    st.markdown('#### 视频描述:')


    for filename in os.listdir("Images"):
        # 拼接文件的完整路径
        file_path = os.path.join("Images", filename)

        # 检查文件是否为图片文件
        if os.path.isfile(file_path) and filename.lower().endswith((".jpg", ".jpeg", ".png")):
            # 打开图片文件
            pred_caption = generate_caption(file_path, caption_model, add_noise=True)
            captions.append(pred_caption)

    for c in captions:
        client = Translate()
        text = client.translate(c)
        print(text.translatedText)
        st.write(text.translatedText)


#用户界面
def page1():
    txt_filepath = './file.txt'
    param1, param2 = read_parameters(txt_filepath)
    param2 = int(param2)
    st.sidebar.header('导航栏')
    # 添加导航栏选项
    selected_page = st.sidebar.radio('功能选择', ('首页', '图像字幕', '以图搜图', '视频字幕'))

    # 根据选项展示不同的页面内容
    if selected_page == '首页':
        st.title('欢迎使用图像字幕生成系统')
        # 添加主页的内容
        # 检查是否有文件上传

    elif selected_page == '图像字幕':
        # 设置页面文本
        st.title('图像字幕生成功能')
        img_url = st.text_input(label='输入图片的地址URL')
        if (img_url != "") and (img_url != None):
            img = Image.open(requests.get(img_url, stream=True).raw)
            img = img.convert('RGB')
            st.image(img)
            img.save('tmp.jpg')
            predict()
            os.remove('tmp.jpg')

        def uploadPicture():
            return st.file_uploader(label='本地上传图片', type=['jpg', 'png', 'jpeg'])

        # 上传图片
        st.markdown('<center style="opacity: 70%">或者</center>', unsafe_allow_html=True)
        img_upload = uploadPicture()
        if img_upload != None:
            # 读取图片地址，三色显示
            img = img_upload.read()
            img = Image.open(io.BytesIO(img))
            img = img.convert('RGB')
            img.save('tmp.jpg')
            st.image(img)
            predict()
            os.remove('tmp.jpg')

    elif selected_page == '以图搜图':
        st.title('以图搜图功能')
        img_url = st.text_input(label='输入图片的地址URL')
        if (img_url != "") and (img_url != None):
            img = Image.open(requests.get(img_url, stream=True).raw)
            img = img.convert('RGB')
            st.image(img)
            img.save('tmp.jpg')
            predict()
            os.remove('tmp.jpg')

        def uploadPicture():
            return st.file_uploader(label='本地上传图片', type=['jpg', 'png', 'jpeg'])

        # 上传图片
        st.markdown('<center style="opacity: 70%">或者</center>', unsafe_allow_html=True)
        img_upload = uploadPicture()

        if img_upload != None:
            # 读取图片地址，三色显示
            img = img_upload.read()
            img = Image.open(io.BytesIO(img))
            img = img.convert('RGB')
            img.save('tmp.jpg')
            st.image(img)
            predict_getimg()
            os.remove('tmp.jpg')


    elif selected_page == '视频字幕':
        st.title('视频字幕功能')
        # 上传视频
        st.markdown('<center style="opacity: 70%">或者</center>', unsafe_allow_html=True)

        def uploadVideo():
            return st.file_uploader(label='本地上传视频', type='mp4')

        vid_upload = uploadVideo()

        if vid_upload != None:
            video_bytes = vid_upload.read()
            # 播放视频
            with open("temp_video.mp4", "wb") as f:
                f.write(video_bytes)
            # 获取视频文件的本地路径
            video_path = "temp_video.mp4"
            st.video(video_bytes)
            # 调用其他函数，并将视频路径作为参数传递
            videoProcess(video_path)
            video_predict()

#登陆界面
def login():
    username = st.text_input('用户名（默认1）')
    password = st.text_input('密码（默认1）', type='password')

    if st.button('Login'):
        # 验证用户凭据的逻辑
        if username == 'admin' and password == 'password':
            # 用户登录成功，将登录状态和用户名保存在会话中
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.success('Login successful!')
        elif username == '1' and password == '1':
            # 另一个账号登录成功，将登录状态和用户名保存在会话中
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.success('Login successful!')
        else:
            st.error('Invalid username or password.')


#修改txt文件指定行
#参数为 1：txt地址 2：行数（>0) 3：新的值
def modify_line(file_path, line_number, new_value):
    # 读取文本文件
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # 修改指定行的值
    if 0 < line_number <= len(lines):
        lines[line_number - 1] = f'{new_value}\n'  # 注意行号从1开始，列表索引从0开始

        # 将修改后的内容写回到文本文件
        with open(file_path, 'w') as file:
            file.writelines(lines)
        print(f"Line {line_number} modified successfully!")
    else:
        print(f"Invalid line number: {line_number}")



#管理员界面
def page2():
    # 界面2的内容
    st.write('#欢迎来到管理员界面')
    parameter = st.text_input('爬取图片的存放地址')
    if st.button('确认保存', key='save_data_1'):
        if os.path.isdir(parameter):
            modify_line('file.txt', 1, parameter)
            st.success('成功修改!')
        else:
            st.warning('地址错误无法打开，请重新输入')

    max_number = st.number_input('爬取最大数量', min_value=1, max_value=30)
    if st.button('确认保存', key='save_data_2'):
        if max_number:
            modify_line('file.txt', 2, max_number)
            st.success('保存成功!')
        else:
            st.warning('数值错误，请重新输入')




def main():

    if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
        # 显示登录界面
        login()
    else:
        # 用户已登录，显示其他内容或功能
        username = st.session_state['username']
        if username == 'admin':
            # 管理员登录，显示界面1
            page2()
        elif username == '1':
            # 另一个账号登录，显示界面2
            page1()
        else:
            st.error('Invalid!')



if __name__ == '__main__':
    main()







