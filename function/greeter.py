def greet_user(usernames):#形参
    """显示简单的问候语"""
    for username in usernames:
        print("Hello,"+username.title()+"!")


#小写名称加下划线
def somebody_hello(name,age=1):#先列没有默认值的形参
    print("%s is %s years old, hello"%(name.title(),age))


def get_formatted_name(
    first_name,last_name,
    middle_name=''):
    """返回姓名"""
    if middle_name:
        full_name = first_name+' '+middle_name+' '+last_name
    else:
        full_name = first_name+' '+last_name
    return full_name.title(),"{first_name:'%s',last_name:'%s'}"%(first_name,last_name)


def showItems(size,*items):
    print(size,items)


def showProfile(first,last,**user_info):
    print(first,last,user_info)

    
users = ["lily","lucy"]
greet_user(users[:])#实参
somebody_hello("star",18)
somebody_hello(age=10,name="zhang san")
somebody_hello("a")
res,json = get_formatted_name("zhang","san")
print(res,json)
showItems(1,1)
showItems(3,1,2,3)
showProfile("Zhang","San", age = 10, sex = "男")