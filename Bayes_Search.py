import numpy as np
from filterpy.kalman import KalmanFilter
from filterpy.common import Q_discrete_white_noise
import random
from REMUS6000 import REMUS6000

# 初始化
x0 = np.array([0, 0, 0, 0])    # 初始状态 (位置, 速度)
p0 = np.array([[0, 0, 0, 0],   # 初始协方差矩阵
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]])

search_area = (0, 100, 0, 100) # 搜索区域
#obstacles = [(20, 30), (40, 50), (60, 70)] # 障碍物位置

rovs = []
num_rovs = 5

# 为每个ROV创建一个卡尔曼滤波器
for i in range(num_rovs): # num_rovs ROV数量
    pf = KalmanFilter(dim_x=4, dim_z=1)
    pf.x = x0                                             # initial state (位置, 速度)
    pf.F = np.array([[1, 0, 1, 0],
                     [0, 1, 0, 1], 
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])                       # 状态转移矩阵 state transition matrix
    pf.H = np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0]])                       # 观测矩阵 Measurement function
    pf.P = p0                                             # 协方差矩阵 covariance matrix
    pf.R = np.array([1,1])                                # 观测噪声协方差 state uncertainty
    pf.Q = Q_discrete_white_noise(dim=4, dt=0.1, var=0.1) # 过程噪声协方差矩阵process uncertainty
    rovs.append(pf)

# 创建ROV实例
rov = REMUS6000(initial_position=[0, 0], initial_velocity=[0, 0])

# 观测模型
def observation_model(x, v):
    # x: [纬度, 经度, x方向速度, y方向速度]
    # v: 观测噪声
    rov.move(dt=1, control_inputs=[0.1, 0, 0])  # 假设控制输入为速度
    sensor_data = rov.collect_sensor_data()
    print(f"Sensor data: {sensor_data}")
    return x, sensor_data

# 动态模型


# 过程模型（搜索策略规划）
def search_strategy(x, P, search_area, step_size):
    # 规划搜索路径
    # 这里我们简单地假设ROV直线移动到当前估计位置
    # 在实际应用中需要更复杂的路径规划算法
    search_point = np.clip(x[:2], search_area[0], search_area[1])
    return search_point

step_size = 5  # ROV每次移动的距离
num_iterations = 10  # num_iterations 迭代次数

for k in range(num_iterations): 
    for i, pf in enumerate(rovs):
        # 预测阶段
        # x_pred = pf.F @ pf.x
        # P_pred = pf.F @ pf.P @ pf.F.T + pf.Q
        
        pf.predict()
        
        # 更新阶段
        z = observation_model(pf.x, np.random.randn())
        pf.update(z)
        
        # 计算卡尔曼增益
        # K = P_pred @ pf.H.T @ np.linalg.inv(pf.H @ P_pred @ pf.H.T + pf.R)

        # 更新状态估计
        # x = x_pred + K @ (observation - pf.H @ x_pred)

        # 更新协方差估计
        # P = (np.eye(4) - K @ pf.H) @ P_pred

        # 输出当前状态估计
        # print(f"Step {num_iterations+1}: Estimated position at ({x[0]}, {x[1]})")
        
        # 规划搜索路径
        search_point = search_strategy(pf.x, pf.P, search_area, step_size)
        # 输出当前搜索点
        # print(f"Step {num_iterations+1}: Search point at {search_point}")

    # 合并ROVS的信息（DDF）
    
    # for i , pf in enumerate(rovs):
    #     print(f'ROV {i} position: {pf.x[0],pf.x[1]} velocity: {pf.x[2]}')