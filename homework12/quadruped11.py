import pybullet as p
import pybullet_data
import time
import numpy as np


class QuadrupedController:
    """
    四足机器人控制器
    功能：
    1. 空中保持脚朝下
    2. 四脚先着地
    3. 稳定站立
    4. 慢速TROT行走
    """

    def __init__(self, robot_id):

        self.robot_id = robot_id

        # Laikago关节ID
        self.leg_joints = {
            'RF': [0, 1, 2],
            'LF': [4, 5, 6],
            'RR': [8, 9, 10],
            'LR': [12, 13, 14]
        }

        # 步态参数
        self.stance_height = 0.33
        self.step_height = 0.04
        self.step_length = 0.03

    # ==========================================
    # 逆运动学 IK
    # ==========================================
    def inverse_kinematics(self, x, z):

        l1 = 0.2
        l2 = 0.2

        D = (x*x + z*z - l1*l1 - l2*l2) / (2*l1*l2)

        D = np.clip(D, -1.0, 1.0)

        knee = np.arccos(D)

        hip = np.arctan2(z, x) - np.arctan2(
            l2*np.sin(knee),
            l1 + l2*np.cos(knee)
        )

        return hip, -knee

    # ==========================================
    # 空中姿态（脚朝下）
    # ==========================================
    def air_pose(self):

        # 腿提前展开
        air_pose = [0, 0.9, -1.8]

        for leg_name, joint_ids in self.leg_joints.items():

            for joint_id, angle in zip(joint_ids, air_pose):

                p.setJointMotorControl2(
                    bodyIndex=self.robot_id,
                    jointIndex=joint_id,
                    controlMode=p.POSITION_CONTROL,
                    targetPosition=angle,
                    force=180
                )

    # ==========================================
    # 稳定站立
    # ==========================================
    def stand(self):

        stand_pose = [0, 0.8, -1.6]

        for leg_name, joint_ids in self.leg_joints.items():

            for joint_id, angle in zip(joint_ids, stand_pose):

                p.setJointMotorControl2(
                    bodyIndex=self.robot_id,
                    jointIndex=joint_id,
                    controlMode=p.POSITION_CONTROL,
                    targetPosition=angle,
                    force=180
                )

    # ==========================================
    # TROT步态
    # ==========================================
    def trot_gait(self, t, leg_name, frequency=0.35):

        # 对角腿同步
        if leg_name in ['LF', 'RR']:
            phase = 0
        else:
            phase = np.pi

        cycle = (2*np.pi*frequency*t + phase) % (2*np.pi)

        # 摆动相
        if cycle < np.pi:

            progress = cycle / np.pi

            x = self.step_length * (progress - 0.5)

            z = self.step_height * np.sin(np.pi * progress)

        # 支撑相
        else:

            progress = (cycle - np.pi) / np.pi

            x = self.step_length * (0.5 - progress)

            z = 0

        hip = 0

        thigh, calf = self.inverse_kinematics(
            x,
            -self.stance_height + z
        )

        return [hip, thigh, calf]

    # ==========================================
    # 行走
    # ==========================================
    def walk(self, t):

        for leg_name, joint_ids in self.leg_joints.items():

            target_angles = self.trot_gait(
                t,
                leg_name,
                frequency=0.35
            )

            for joint_id, angle in zip(joint_ids, target_angles):

                p.setJointMotorControl2(
                    bodyIndex=self.robot_id,
                    jointIndex=joint_id,
                    controlMode=p.POSITION_CONTROL,
                    targetPosition=angle,
                    force=180
                )


# ==========================================
# 主程序
# ==========================================
def main():

    # GUI模式
    p.connect(p.GUI)

    # PyBullet资源路径
    p.setAdditionalSearchPath(
        pybullet_data.getDataPath()
    )

    # 重力
    p.setGravity(0, 0, -9.8)

    # 地面
    p.loadURDF("plane.urdf")

    # ==========================================
    # 初始位置
    # ==========================================
    start_pos = [0, 0, 0.6]

    # 初始姿态
    # 稍微抬头，避免头着地
    start_orientation = p.getQuaternionFromEuler(
        [0, -0.15, 0]
    )

    # 加载机器人
    robot = p.loadURDF(
        "laikago/laikago_toes.urdf",
        start_pos,
        start_orientation
    )

    # 增加阻尼
    p.changeDynamics(
        robot,
        -1,
        linearDamping=0.04,
        angularDamping=0.04
    )

    # 打印关节信息
    print("====== JOINT INFO ======")

    for i in range(p.getNumJoints(robot)):

        info = p.getJointInfo(robot, i)

        print(i, info[1].decode("utf-8"))

    # 创建控制器
    controller = QuadrupedController(robot)

    dt = 1 / 240

    # ==========================================
    # 第一阶段：空中落下
    # ==========================================
    print("机器人从空中落下...")

    for _ in range(360):

        # 空中腿部展开
        controller.air_pose()

        # 获取当前位置
        position, orientation = p.getBasePositionAndOrientation(robot)

        # 强制身体保持水平
        p.resetBasePositionAndOrientation(
            robot,
            position,
            p.getQuaternionFromEuler([0, -0.1, 0])
        )

        # 清除旋转速度
        p.resetBaseVelocity(
            robot,
            angularVelocity=[0, 0, 0]
        )

        p.stepSimulation()

        time.sleep(dt)

    # ==========================================
    # 第二阶段：稳定站立
    # ==========================================
    print("机器人稳定站立...")

    for _ in range(480):

        controller.stand()

        p.stepSimulation()

        time.sleep(dt)

    # ==========================================
    # 第三阶段：开始行走
    # ==========================================
    print("机器人开始行走...")

    t = 0

    while True:

        controller.walk(t)

        p.stepSimulation()

        time.sleep(dt)

        t += dt


# ==========================================
# 程序入口
# ==========================================
if __name__ == "__main__":

    main()
