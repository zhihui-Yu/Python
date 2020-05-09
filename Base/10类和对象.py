# Python也是面向对象语言  有继承 多态 封装

'''
    类用class声明
        __new__ : 创建对象时调用
        __init__: 初始化对象时调用，可以看出构造器 ！！在这里传入的参数 在new中也要写！！
        __del__ : 对象删除时调用
        __str__ : toString
        以上均为默认

    改变属性值 ：
        1.使用类名.属性
        2.对象.属性 改变属性值
        3.在类中创建方法 对象.方法名()
    __属性名 ： 私有,只能通过get方法遍历

'''
class Car(object) :
    name = 'zhangsan'
    __age = "19"
    def __init__(self,name,age):
        print("init")
        self.name = name
        self.__age = age
    def __new__(cls,name,age):
        print("new")
        # 要返回创建的对象
        return object.__new__(cls)
    def __del__(self):
        print("del")
    def __str__(self):
        return 'name: ' + self.name + ',age: ' + self.__age
    def getAge(self):
        return self.__age


obj = Car("lisi",'16')
print(type(obj))
print(obj)

obj2 = Car("zhaoliu",'33')
obj2.name="sss"
print(obj2)

#不能调
#print(obj.__age)
print(obj.getAge())
