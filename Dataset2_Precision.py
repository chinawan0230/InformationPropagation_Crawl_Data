# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
names = ['1', '2', '3', '4', '5', '6', '7']
x = range(len(names))
y2 = [0.043, 0.01, 0.004, 0.005, 0.004, 0.004, 0.004]
y = [0.074, 0.063, 0.062, 0.048, 0.051, 0.057, 0.09]
y1 = [0.043, 0.041, 0.037, 0.032, 0.038, 0.044, 0.068]

y3 = [0.082, 0.075, 0.070, 0.073, 0.084, 0.089, 0.093]
#plt.plot(x, y, 'ro-')
#plt.plot(x, y1, 'bo-')
#pl.xlim(-1, 11)  # 限定横轴的范围
#pl.ylim(-1, 110)  # 限定纵轴的范围
plt.plot(x, y2, marker='^', ms=10, label='CT + General threshold model')
plt.plot(x, y, marker='s', label='GT (Diffusion cascades)')
plt.plot(x, y1, marker='*', ms=10, label='GT (Page rank)')

plt.plot(x, y3, marker='.', ms=10, label='Our method')
plt.figure(1)
plt.legend()  # 让图例生效
plt.xticks(x, names)
plt.margins(0.05)
plt.subplots_adjust(bottom=0.15)
plt.xlabel("Time step (3 days)")  # X轴标签
plt.ylabel("Precision")  # Y轴标签
# plt.title("A simple plot")  # 标题

plt.show()