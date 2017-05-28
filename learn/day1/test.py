import sys
print(sys.path)
name = "zhan"
age =19
job = "iT"

msg = '''
=============user name %s
  yourname is: %s
  your age is: %s
  your job js: %s
'''  % (name,name,age,job)

print(msg)

resArr = ['zhang','chaofu','age']
print(resArr)
print(resArr[0])
print(resArr[2])
print(resArr[1:3])
resArr.append("lai")
print(resArr)
resArr_copy = resArr.copy();
print(resArr_copy)
print(resArr_copy.count("lai"))
info = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': "XiaoZe Maliya",
}
info['stu1104'] ="zhouenlai"
print(info)
print(info.get("stu1101"))
print("hello world !")
#for
for key in  info:
    print(key,info[key])
#file
# f =open("test.py")
# frist_line = f.readline()
# print(frist_line)
# print("line-------".center(50,'+'))
# # data = f.read()
# # print(data)
# f.close()

#集合
jihe = {1,2,3,4,5,4,3}
print(jihe)
#元组 不能修改
#只读列表，只有count, index 2 个方法
#作用：如果一些数据不想被人修改， 可以存成元组，比如身份证列表

#函数
a,b =5,8
def cacl(x,y):
    res = x**y
    return res

sumd= cacl(a,b)
print(sumd)