
'''
    继承 子类中可以用super().方法名()调用父类方法
    多态 使用鸭子模型，定义时的类型和运行时的类型不一样，此时就成为多态
        有点不像多态，因为没有类型值，要什么都是直接赋值的
    多继承 ： 一个类可以继承多个父类
    类属性 ： 定义在类内 但是不在方法中
    实例属性 ； 定义在方法中
    @classmethod : 修饰类中的方法变为静态方法，需要传参 cls
    @staticmethod : 同上，但是不需要传参
'''
class Animal:
    def __init__(self):
        pass
    def call(self):
        print("动物叫")

class Cat(Animal):
    #实例属性
    name = ""
    def __init__(self,name):
        super().__init__()
        #与上面等价
        #super(Animal,self).__init__()
        self.name = name
    def call(self):
        print(self.name , "叫")

class Dog(Animal):
    name = ""
    def __init__(self,name):
        super().__init__()
        self.name = name
    def call(self):
        print(self.name , "叫")

#多继承
class BigCat(Cat,Animal):
    name = ""

    def __init__(self, name,age):
        super().__init__(name)
        self.name = name
        self.age = age

    def call(self):
        print(self.name, "叫")

#多态
def call(obj):
    obj.call()

A = Animal()
A.call()
A = Cat("卡菲猫")
A.call()
A = Dog("大黑狗")
#多态
call(A)

B = BigCat("dudu","20")
B.call()

#类属性
print(B.name)
#实例属性
print(B.age)

class Demo:

    age = 10
    name = "Demo"
    @classmethod
    def getAge(cls):
       return cls.age

    @staticmethod
    def getName():
        return Demo.name

print(Demo.getAge())
print(Demo.getName())