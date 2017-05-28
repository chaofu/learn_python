
def sayhi():
    print("hello ")

def cal(a,b):
    c =a+b
    print("c",c)
sayhi()
cal(3,4)
def stu_rigerst(name,age,*arg):
    print(name,age,arg)
stu_rigerst("zhang","34","li","d")

def digui(c):
    print(c)
    if int(c/2) == 0:
       return  c
    return  digui(int(c/2))
digui(10)

