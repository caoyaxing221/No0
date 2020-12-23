i = 1
while i <= 5:
    print(i)
    i += 1
flag = True
print("enter quit to quit")
while  flag:
    message = input("please enter your name:")
    if message == 'quit':
        flag = False
    else:
        print("your name is :" + message)
flag = True
while  flag:
    message = input("please enter your name:")
    if message == '':
        continue
    break