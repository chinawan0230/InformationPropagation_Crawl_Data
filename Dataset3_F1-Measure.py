# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文


#[ 0.012       0.00888889  0.0048      0.005       0.00685714  0.00545455  0.00444444]
#[ 0.05247706  0.05538462  0.04221176  0.048       0.07823602  0.05587719  0.04935922]
#[ 0.05078095  0.0528595   0.03918987  0.04351648  0.07477124  0.04725  0.04444444]
#[ 0.0644031   0.06884354  0.05076923  0.05714783  0.08319527  0.06698507   0.063     ]
names = ['1', '2', '3', '4', '5', '6', '7']
x = range(len(names))

y2 = [0.02944785,  0.01960784,  0.01179775,  0.00989011,  0.01564246, 0.01186312,  0.00990991]
y  = [0.08318408,  0.07584416,  0.08489933,  0.07632184,  0.12431499, 0.09167325,  0.07774968]
y1 = [0.08042232,  0.07399209,  0.07943162,  0.06874372,  0.12066298, 0.07924528,  0.07555556]
y3 = [0.11583864,  0.10308571,  0.10985915,  0.10004242,  0.13698189, 0.12182243,  0.11730559]
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