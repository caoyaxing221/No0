import json
class File():
    """docstring for File"""
    def __init__(self, path):
        self.path = path
        
    def with_open(self):
        try:
            with open (self.path) as file_object:
                # print(file_object)
                contents = file_object.read()
                # print(contents[:50].rstrip())
        except FileNotFoundError:
            return "file does not exist"
            #pass
        return contents
    def read_lines(self):
        with open (self.path,'r',encoding = 'utf-8') as file_object:
            for line in file_object:
                print(line.rstrip())
    def read_lines2(self):
        with open (self.path,'r',encoding = 'utf-8') as file_object:
            lines = file_object.readlines()
            return lines
    def check_birthday(self,birthday):
        # print(self.with_open())
        return birthday in self.with_open();
    def write_message(self,message):
        with open (self.path,'w',encoding = 'utf-8') as file_object:
            # print(file_object)
            file_object.write(message)
            # print(file_object.read())
            """r w(存在时会清空) r+ a"""
    def append_message(self,message):
        with open (self.path,'a',encoding = 'utf-8') as file_object:
            # print(file_object)
            file_object.write(message)
    def write_json(self,message):
        with open(self.path,'w') as f_obj:
            json.dump(message,f_obj)
    def read_json(self):
        with open(self.path) as f_obj:
            return json.load(f_obj)

    def div(self,dividend,divider):
        try:
            quotient = dividend/divider
            int('abc')
        except ZeroDivisionError as e:
            print('can not divide by zero')
            """程序崩溃可不好，但让用户看到traceback也不是好主意。不懂技术的用户会被它们搞糊涂，而且如果用户怀有恶意，他会通过traceback获悉你不希望他知道的信息。例如，他将知道你的程序文件的名称，还将看到部分不能正确运行的代码。有时候，训练有素的攻击者可根据这些信息判断出可对你的代码发起什么样的攻击"""
        except ValueError as e:
            pass
        except TypeError as e:
            pass
        else:
            print(quotient)
        finally:
            print('finish')
    #http://gutenberg.org/


if __name__=="__main__":
    File('pi_1000000.txt').with_open()
    file = File('pi_10.txt')
    file.read_lines()
    print(file.read_lines2())
    file = File('pi_1000000.txt')
    print(file.check_birthday('20200101'))
    print(file.with_open().count('33'))
    file = File('programming.txt')
    file.write_message('I love programming\nI love debug')
    file.append_message('\nYeah')
    file.read_lines()
    file.div(1,1)
    file.div(1,0)
    file.div('a',1)
    """JSON（JavaScript Object Notation）格式最初是为JavaScript开发的，但随后成了一种常见格式，被包括Python在内的众多语言采用"""
    file = File('user.json')
    str = {'user_name':'zhangsan','age':18}
    file.write_json(str)
    content = file.with_open()
    print(file.read_json())
    print(content)
    print(json.loads(content))