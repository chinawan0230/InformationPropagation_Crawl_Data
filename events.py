# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
x = range(len(names))
y1 = [102, 1109, 1242, 1526, 1497, 506, 270, 178, 329, 112, 60, 28, 28, 12, 10, 7]
y2 = [1, 2, 3, 11, 835, 286, 173, 51, 152, 18, 16, 13, 8, 9, 11, 4]
y3 = [12, 29, 393, 1017, 908, 1278, 526, 358, 395, 615, 231, 56, 30, 8, 14, 6]



#plt.plot(x, y, 'ro-')
#plt.plot(x, y1, 'bo-')
#pl.xlim(-1, 11)  # 限定横轴的范围
#pl.ylim(-1, 110)  # 限定纵轴的范围
plt.plot(x, y1, marker='s', label='Event1')
plt.plot(x, y2, marker='^', label='Event2')
plt.plot(x, y3, marker='*', label='Event3')
plt.legend()  # 让图例生效
plt.xticks(x, names, rotation=45)
plt.margins(0.05)
plt.subplots_adjust(bottom=0.15)
plt.xlabel("Time step (days)")  # X轴标签
plt.ylabel("Posts")  # Y轴标签
# plt.title("A simple plot")  # 标题

plt.show()