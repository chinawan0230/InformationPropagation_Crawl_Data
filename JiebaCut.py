#coding=utf-8
import jieba
import jieba.posseg as pseg
import time
t1 = time.time()
# 字符串通过编码转换为字节码，字节码通过解码转换为字符串
f = open("cdnsj_single.txt", "r") # 读取文本，把整个文件读进来作为整个字符串
string = f.read()
words = pseg.cut(string) # 进行分词
result = "" # 记录最终结果的变量
for w in words:
   result += str(w.word)+"/"+str(w.flag) # 加词性标注
f = open("cdnsj_single_pos_target.txt", "w") # 将结果保存到另一个文档中
f.write(result)
f.close()
t2 = time.time()
print("分词及词性标注完成，耗时："+str(t2-t1)+"秒。") # 反馈结果