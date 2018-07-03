# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文


names = ['1', '2', '3', '4', '5', '6', '7']
x = range(len(names))

y2 = [0.088,       0.07453744,  0.06683938,  0.06348837,  0.05815603,  0.05866667,  0.06579235]
y  = [0.12522417,  0.12218182,  0.1220339,   0.11704918,  0.12187625,  0.13191806,  0.13526412]
y1 = [0.10438776,  0.10243902,  0.10387435,  0.09913043,  0.11142857,  0.10652807,  0.11021869]
y3 = [0.14108499,  0.13043478,  0.13538462,  0.12870968,  0.12709924,  0.13526412,  0.14315091]
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
