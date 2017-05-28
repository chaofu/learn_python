
age =30
count=0
for i in range(10):
    if(count>3):
        flag = input("you want to guress")
        if(flag == 'y'):
            count = 0
            continue
        else:
            print("bu wan le")
            break
    else:
        inputage = int(input("guess_age:"))

        if (age == inputage):
            print("congratulations you")
            break
        elif (age > inputage):
            print("Think big")
        else:
            print("Think small")
    count =count +1