from dog import Dog,Animal #类名应采用驼峰命名法，即将类名中的每个单词的首字母都大写，而不使用下划线。实例名和模块名都采用小写格式，并在单词之间加上下划线 在类中，可使用一个空行来分隔方法；而在模块中，可使用两个空行来分隔类
import dog
from dog import * #不推荐 不清楚导入了哪些类 还有可能出现与程序文件同名类
from collections import OrderedDict #标准库 http://pymotw.com/
from random import randint
my_dog = Dog('gg',9)
my_dog.roll_over()
my_cat = dog.Animal('cat',1)
my_cat.sit()
dic = OrderedDict()
dic['z'] = 1
dic['a'] = 2
for name,i in dic.items():
    print(name,i)
dic2 = {}
dic2['z'] = 1
dic2['a'] = 2
for name,i in dic2.items():
    print(name,i)
print(randint(1,6))