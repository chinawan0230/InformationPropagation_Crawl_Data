# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
x = range(len(names))
y = [0.06254115, 0.72547729, 0.81303489, 1.0, 0.98090849,
     0.3285056, 0.17314022, 0.11257406, 0.35198157, 0.06912442,
     0.03489138, 0.01382488, 0.01382488, 0.00329164, 0.00197498, 0]
y1 = [0., 0.00119904, 0.00239808, 0.01199041, 1.0,
     0.34172662, 0.20623501, 0.18095204, 0.18105516, 0.15038369,
     0.11798561, 0.05838849, 0.03839329, 0.02959233, 0.01199041, 0.00859712]
y2 = [0.00471698, 0.01808176, 0.30424528, 0.79481132, 0.7091195,
      1.0, 0.40880503, 0.27672956, 0.20581761, 0.17877358,
      0.13688679, 0.03930818, 0.01886792, 0.00157233, 0.00628931, 0.]



plt.plot(x, y, marker='o', label='Social event 1')
plt.plot(x, y1, marker='>', ms=10, label='Entertainment event 2')
plt.plot(x, y2, marker='s', ms=10, label='International news event 3')

plt.figure(1)
plt.legend()  # 让图例生效
plt.xticks(x, names)
plt.margins(0.05)
plt.subplots_adjust(bottom=0.15)
plt.xlabel("Time step (days)")  # X轴标签
plt.ylabel("Normalization of information diffusion")  # Y轴标签
# plt.title("A simple plot")  # 标题
plt.savefig('F:\photo\comparision.eps')
plt.show()