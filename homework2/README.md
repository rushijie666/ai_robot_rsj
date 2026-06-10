# week2作业记录：

## 第二周课程内容：
### 课程内容1：设置github ssh密钥并进行ubuntu里的命令行交互


### 课程内容2：设置vs code 与wsl ubuntu交互

### 课程内容3：运行小乌龟节点，进行ros命令行交互




## 作业成果：
### 作业1：运行ros2 画直线
![alt text](week2/2-1.jpg)![alt text](week2/2-3.jpg) ![alt text](week2/2-2.jpg)

1. 核心理解
ROS2 的节点之间通过 Topic 通信，控制小乌龟时本质上是在向 /turtle1/cmd_vel 发布速度消息。
VS Code + WSL 的组合适合机器人课程实验：代码管理清楚，命令运行环境也接近真实 Linux。
GitHub SSH 配置成功后，课程作业可以稳定同步到远程仓库。
2. 问题与解决
如果 ssh -T git@github.com 失败，需要检查公钥是否复制完整。
如果 TurtleSim 没有反应，需要确认控制命令发布到正确话题 /turtle1/cmd_vel。
3. 本周总结
本周完成了 GitHub、VS Code、WSL 与 ROS2 的基础联动，并通过 TurtleSim 直线运动验证了 ROS2 控制链路。