import numpy as np
import matplotlib.pyplot as plt

# 创建灰度图像数组
gray_image = np.array([
    [0, 30, 60, 30, 0],
    [10, 80, 110, 80, 10],
    [20, 130, 255, 130, 20],
    [10, 80, 110, 80, 10],
    [0, 30, 60, 30, 0]
])

section = np.copy(gray_image)
data_Min = np.abs(np.min(section))
section = section - data_Min
data_Max = np.max(section)
section = section / (data_Max-data_Min)
section = np.round(section * 65535).astype(np.uint16)
# print(section)

# 绘制灰度图
plt.imshow(section, cmap='gray')  # 指定灰度色彩映射
plt.colorbar()  # 添加颜色条
plt.title('Grayscale Image')  # 图像标题
plt.show()  # 显示图像
