
age =30

for i in range(10):
    if(i>2):
        print("many attemps")
        break
    inputage = int(input("guess_age:"))

    if(age == inputage):
        print("congratulations you")
        break
    elif(age > inputage):
        print("Think big")
    else:
        print("Think small")