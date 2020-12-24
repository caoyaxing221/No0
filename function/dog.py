from animal import Animal
#创建子类时，父类必须包含在当前文件中，且位于子类前面 在子类括号指定父类名称
class Dog(Animal):
    """docstring for ClassName"""
    def __init__(self, name, age):
        """初始化父类属性"""
        super().__init__(name,age)
        self.tail = "yellow"
    def roll_over(self):
        """模拟小狗打滚"""
        print(self.name.title()+" rolled over!")
    def get_tail_color(self):
        return self.tail
    def sit(self):
        """重写方法"""
        print("can't sit")
class House():
      """docstring for ClassName"""
      def __init__(self):
          self.dog = Dog('gg',2)
            
my_dog = Animal('dog',6)
print(my_dog.name.title(),my_dog.age)
my_dog.age = 10
my_dog.sit()
my_dog.set_name('gougou')
print(my_dog.get_animal_info())
my_dog = Dog('dog',1)
my_dog.roll_over()
print(my_dog.get_tail_color())
my_dog.sit()
house = House()
house.dog.sit()


