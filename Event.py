import pandas as pd

df = pd.read_excel("E:\\Data\\cdnsjbdbd.xlsx", encoding='gbk',skiprows=2)
print(df.head())

# with open("E:\\Data\\cdnsjbdbd.excel","r") as f:
#     for line in f.readlines():
#         print
