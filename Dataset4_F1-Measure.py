# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文


#[ 0.05660377  0.03818182  0.03073892  0.02894118  0.027173    0.03076923  0.03826087]
#[ 0.12170213  0.10956522  0.1146472   0.09882503  0.12833333  0.12469438  0.1422973 ]
#[ 0.1141688   0.09295775  0.11052632  0.10103704  0.12301102  0.11611457  0.13866051]
#[ 0.14047891  0.11755102  0.12911111  0.12145278  0.13350528  0.1350237   0.15470899]
names = ['1', '2', '3', '4', '5', '6', '7']
x = range(len(names))

y2 = [ 0.05660377,  0.03818182,  0.03073892,  0.02894118,  0.027173,    0.03076923,  0.03826087]
y  = [ 0.12170213,  0.10956522,  0.1146472,   0.09882503,  0.12833333,  0.12469438,  0.1422973 ]
y1 = [ 0.1141688,   0.09295775,  0.11052632,  0.10103704,  0.12301102,  0.11611457,  0.13866051]
y3 = [ 0.14047891,  0.11755102,  0.12911111,  0.12145278,  0.13350528,  0.1350237,   0.15470899]
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