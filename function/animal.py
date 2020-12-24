class Animal():
    """模拟动物"""
    def __init__(self, name, age):
        #创建新的实例自动运行
        #self 为指向实例本身的引用 让实例能够访问类中的属性和方法
        #self 前缀的变量可以供类中所有方法使用 可以通过类的任何实例访问这些变量
        """初始化属性name和age"""
        self.name = name
        #可以通过实例访问的变量称为属性
        self.age = age
        self.color = 'yellow'
    def set_name(self,name):
        self.name = name
    def sit(self):
        """模拟动物坐下"""
        print(self.name.title()+" is now sitting.")
    def get_animal_info(self):
        return "{name:'%s',age:'%s',color'%s'}"%(self.name,self.age,self.color)