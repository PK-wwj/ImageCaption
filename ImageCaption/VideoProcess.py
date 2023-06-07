# 导入所有必要的库
import cv2
import os



'''读取mp4文件并进行分割'''
def videoProcess(path):
    '''读取mp4文件并进行分割'''
    cam = cv2.VideoCapture(path)
    try:
        # 创建名为data的文件夹
        if not os.path.exists('Images'):
            os.makedirs('Images')
            print('created successfully ')

    # 如果未创建，则引发错误
    except OSError:
        print('Error: Creating directory of data')

    # 定义保存图片函数
    # image:要保存的图片名字
    # addr；图片地址与相片名字的前部分
    # num: 相片，名字的后缀。int 类型
    def save_image(image, addr, num):
        address = addr + str(num) + '.jpg'
        cv2.imwrite(address, image)

    # reading from frame
    ret, frame = cam.read()  # ret为布尔值 frame保存着视频中的每一帧图像 是个三维矩阵
    i = 0
    timeF = 60  # 设置要保存图像的间隔 60为每隔60帧保存一张图像
    j = 0
    while ret:
        i = i + 1
        # 如果视频仍然存在，继续创建图像
        if i % timeF == 0:
            # 呈现输出图片的数量
            j = j + 1
            save_image(frame, './Images/', j)
            print('save image:', j)
        ret, frame = cam.read()
        # 一旦完成释放所有的空间和窗口
    cam.release()
    cv2.destroyAllWindows()


# 从指定的路径读取视频




if __name__ == '__main__':
    path = "Video/fight.mp4"
    videoProcess(path)
