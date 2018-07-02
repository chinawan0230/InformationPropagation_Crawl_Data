import xlrd
import xlwt
import pandas
from datetime import date,datetime

file = xlrd.open_workbook('E:\Data\cdnsj.xlsx')
sheet1 = file.sheet_by_index(0)
# print('该Excel文件共有行数：' + str(sheet1.nrows))

# 打印第一行与第二行数据
values_line1 = sheet1.row_values(0)
print(values_line1)
# values_line1 = sheet1.row_values(1)
# print(values_line1)

# 打印第一列数据
values_line2 = sheet1.col_values(0)
print(values_line2)

# 打印所有数据
# for i in range(0,sheet1.nrows):
#     line = sheet1.row_values(i)
#     print('第%d行数据：'%(i),end='')
#     print(line)

workbook = xlwt.Workbook(encoding='ascii')  # 创建工作簿
worksheet = workbook.add_sheet('My Worksheet')  # 创建sheet
# 将原数据集中的Uid存储到新的Excel（UID表）中
row = list(sheet1.col_values(0))
for i in range(0, sheet1.nrows):
    worksheet.write(i, 0, row[i])
    workbook.save('Weibo_Uid.xls')




