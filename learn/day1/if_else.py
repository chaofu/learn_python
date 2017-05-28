
name ="zhang"
password ="123456"

username = input("your name:")
pw = input("your password:")

if name == username:
    print("you name:")
    if(password == pw):
        print("wecome:")
    else:
        print("password is wrong")
else:
    print("username is wrong")