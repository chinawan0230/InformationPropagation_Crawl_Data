# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文


names = ['1', '2', '3', '4', '5', '6', '7']
x = range(len(names))
y2 = [0.073, 0.019, 0.008, 0.01, 0.008, 0.008, 0.008]
y = [0.12, 0.108, 0.109, 0.088, 0.092, 0.1, 0.142]
y1 = [0.073, 0.07, 0.064, 0.056, 0.068, 0.082, 0.114]
y3 = [0.139, 0.13, 0.121, 0.124, 0.142, 0.150, 0.158]

plt.plot(x, y2, marker='^', ms=10, label='CT + General threshold model')
plt.plot(x, y, marker='s', label='GT (Diffusion cascades)')
plt.plot(x, y1, marker='*', ms=10, label='GT (Page rank)')
plt.plot(x, y3, marker='.', ms=10, label='Our method')
plt.legend()  # 让图例生效  rotation=45
plt.xticks(x, names)
plt.margins(0.05)
plt.subplots_adjust(bottom=0.15)
plt.xlabel("Time step (3 days)")  # X轴标签
plt.ylabel("F1-Measure")  # Y轴标签

plt.show()