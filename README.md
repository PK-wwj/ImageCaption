## ImageCaption

图像字幕生成，包含可视化部分和模型文件

## 模型下载

。。。。\ImageCaption\ImageCaption\saved_models文件夹中有两个重要的模型，请在百度网盘下载后，放入此文件夹中

链接：https://pan.baidu.com/s/1foPHtv16Zdh23XSWkNY-vg?pwd=pkwj 
提取码：pkwj

## file.txt

两行参数，第一行是爬取图片的额外保存路径，默认是Temp文件夹，默认保存路径是NewImages文件夹

第二行是爬取的数目，理论上最大值为30，因为我爬虫只能读那么多

## Temp

temp文件夹的内容为NewImages文件夹内容的复制

## GetNewimage

爬虫模块，header应该需要去重写

## 运行方式

在app.py文件所在位置打开终端

运行 Streamlit run （文件路径）\app.py

