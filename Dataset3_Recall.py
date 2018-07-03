# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文


names = ['1', '2', '3', '4', '5', '6', '7']
x = range(len(names))
y2 = [0.8, 0.50, 0.35, 0.45, 0.35, 0.52, 0.55]
y = [0.76, 0.73, 0.55, 0.83, 0.86, 0.71, 0.75]
y1 = [0.62, 0.72, 0.52, 0.76, 0.84, 0.70, 0.68]
y3 = [0.88, 0.82, 0.65, 0.89, 0.92, 0.79, 0.85]
#plt.plot(x, y, 'ro-')
#plt.plot(x, y1, 'bo-')
#pl.xlim(-1, 11)  # 限定横轴的范围
#pl.ylim(-1, 110)  # 限定纵轴的范围
plt.plot(x, y2, marker='^', ms=10, label='CT + General threshold model')
plt.plot(x, y, marker='s', label='GT (Diffusion cascades)')
plt.plot(x, y1, marker='*', ms=10, label='GT (Page rank)')
plt.plot(x, y3, marker='.', ms=10, label='Our method')
plt.legend()  # 让图例生效
plt.xticks(x, names)
plt.margins(0.05)
plt.subplots_adjust(bottom=0.15)
plt.xlabel("Time step (3 days)")  # X轴标签
plt.ylabel("Recall")  # Y轴标签
# plt.title("A simple plot")  # 标题

plt.show()