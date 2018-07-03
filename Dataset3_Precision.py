# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
names = ['1', '2', '3', '4', '5', '6', '7']
x = range(len(names))
y2 = [0.015, 0.01, 0.006, 0.005, 0.008, 0.006, 0.005]
y = [0.044, 0.040, 0.046, 0.040, 0.067, 0.049, 0.041]
y1 = [0.043, 0.039, 0.043, 0.036, 0.065, 0.042, 0.040]
y3 = [0.062, 0.055, 0.060, 0.053, 0.074, 0.066, 0.063]
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