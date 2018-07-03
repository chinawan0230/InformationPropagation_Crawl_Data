# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文


names = ['1', '2', '3', '4', '5', '6', '7']
x = range(len(names))
y2 = [0.24, 0.08, 0.04, 0.05, 0.06, 0.05, 0.04]
y = [0.35, 0.36, 0.39, 0.35, 0.42, 0.45, 0.47]
y1 = [0.22, 0.24, 0.26, 0.23, 0.28, 0.35, 0.32]
y3 = [0.46, 0.49, 0.44, 0.42, 0.46, 0.48, 0.53]
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