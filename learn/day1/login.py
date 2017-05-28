#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import getpass
name = "zhang"
pw ="123456"

username = input("your name:")
password = input("pleaes input pass:")
f = open("error_count.txt", 'r+')
count = f.readline()
print("count",count)
if count.strip()=='':
    count=0
count =  int(count)
if count>3:
    print("你的账号已经给锁定")
else:
    if name == username and pw== password:
        print("welcome login")
        f.write(0)
    else:
        print("用户名或者密码错误")
        if(count >0):
            count = count+1
            f.truncate() #清空文件内容
            f.write(str(count))
        else:
            f.write("1")
f.close()
