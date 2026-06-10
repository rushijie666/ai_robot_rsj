# week10作业记录：

## 第十周课程内容：
### 课程内容1：安装opencv

### 课程内容2：opencv运行

![alt text](cat.png)
![alt text](cat2.png)

1. Docker 基础概念
Image 镜像
镜像是只读模板，包含程序运行所需的环境、依赖和配置。

Container 容器
容器是镜像运行后的实例，可以理解为正在运行的程序环境。

2. Docker 常用命令
查看 Docker 版本：

docker --version

查看运行中的容器：

docker ps

查看所有容器：

docker ps -a

运行容器：

docker run 镜像名

停止容器：

docker stop 容器ID

3. OpenCV 实验
OpenCV 是一个开源计算机视觉库，可以用于图像读取、灰度转换、边缘检测和目标识别等任务。

安装命令：

pip3 install opencv-python opencv-contrib-python --break-system-packages

运行实验程序：

python3 opencv_demo.py

总结
通过本周实验，我了解了 Docker 镜像和容器的区别，也学习了 OpenCV 的基本图像处理流程。

姓名：여세걸

![alt text](download.png)