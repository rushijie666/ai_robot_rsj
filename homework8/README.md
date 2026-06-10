# week8作业记录：

## 第八周课程内容：
### 课程内容1：docker下载调试连接

### 课程内容2：在docker跑小乌龟


1. Docker 的作用
Docker 可以把运行环境封装到容器中，减少不同电脑和系统之间的环境差异。

2. 为什么 ROS2 适合使用 Docker？
ROS2 依赖较多，不同系统安装时容易出现版本问题。
使用 Docker 可以快速获得统一环境，方便课堂实验和项目复现。

3. 本周使用的访问地址
运行 ROS2 桌面容器后，可以在浏览器中访问：

http://127.0.0.1:6080/

4. 启动 Docker ROS2 桌面容器
课堂参考项目：

https://github.com/Tiryoh/docker-ros2-desktop-vnc

5. 浏览器访问 ROS2 桌面
访问地址：

http://127.0.0.1:6080/

6. 在容器中运行 turtlesim
运行小乌龟：

ros2 run turtlesim turtlesim_node

运行键盘控制：

ros2 run turtlesim turtle_teleop_key

总结
通过本周实验，我了解了 Docker 容器的基本作用，并学习了如何通过 Docker 运行 ROS2 图形桌面环境。Docker 可以减少本机环境差异，使 ROS2 实验更加稳定和容易复现。



姓名：여세걸

![alt text](download.png)