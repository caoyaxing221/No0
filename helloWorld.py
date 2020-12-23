#!/usr/bin/python ./
# -*- coding: UTF-8 -*-
#import this
#PEP 8：请访问https://python.org/dev/peps/pep-0008/，阅读PEP8格式设置指南。 制表符转换为指定数量的空格 建议每行不超过80字符
## string
name = " 123ada" + " wang's321 "
print('\t',name.title(),'\n',name.upper(),'\n\t',name.lower())
print('|',name,'|',name.rstrip(),'|',name.lstrip(),'|',name.strip(),'|',name.strip().strip("12"))
## int
print(1+1,1-1,2+1*3,3/2,2**3)##python 2 相除需要至少一个为浮点数否则结果为整数
## float
print(0.1+0.1,0.2+0.2,2*0.1,2*0.2,0.1+0.2,3*0.1)
age = 23
message ='Han Mei Mei is '
print(message + str(age))
## 列表 元祖 字典 集合
## list
bicycles = []
print(bicycles)
if bicycles:
    print(1)
else:
    print(2)
bicycles = [1,'giant','phoenix','pigeon']
print(bicycles,bicycles[-1])
bicycles[2] = 'giant'
bicycles.append('forever')
print(bicycles)
bicycles.insert(1,'BMW')
print(bicycles)
del bicycles[0]
print(bicycles)
popped_bicycle = bicycles.pop()
print(bicycles)
print(popped_bicycle)
first_bicycle = bicycles.pop(0)
print(first_bicycle)
print(bicycles)
bicycles.insert(1,'small')
print(bicycles)
bicycles.remove('giant')
print(bicycles)
bicycles.sort()
print(bicycles)
bicycles.sort(reverse = True)
print(bicycles)
print(sorted(bicycles))## reverse = True
print(bicycles)
bicycles.insert(0,'apple')
bicycles.reverse()
print(bicycles)
print(len(bicycles))
## 列表操作
for bicycle in bicycles:
    print(bicycle)
for i in range(1,5):
    print(i)
numbers = list(range(0,10))
print(numbers)
numbers = list(range(1,1000000))
print(min(numbers),max(numbers),sum(numbers))
print(99 in numbers)
print(99 not in numbers)
even_numbers = list(range(2,12,2))
print(even_numbers)
suqares = [value**2 for value in range(1,11)]
print(suqares)
##列表切片
print(suqares[1:])
print(suqares[:-3])
my_foods = ['apple','banana']
friend_foods = my_foods[:]
print(friend_foods)
my_foods.append('tea')
friend_foods.append('milk')
print(my_foods,friend_foods)
friend_foods = my_foods
my_foods.append('milk')
friend_foods.append('cocacola')
print(my_foods,friend_foods)
##元祖 列表可修改 元祖不可变
dimensions = (200,50)
print(dimensions,dimensions[0],dimensions[1])
#dimensions[0] = 50
dimensions = (200,200)
print(dimensions)
## == != > < >= <= and or 
print(1 == 2,1 != 2)
age = 12
if age < 4:
    print('you are free')
elif age < 18:
    print('your cost is 5')
else:
    print('your cost is 10')