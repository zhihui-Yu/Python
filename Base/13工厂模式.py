'''
    工厂模式有 简单工厂 工厂方法 抽象工厂
        简单工厂 一个工厂可以创建多种实例
        工厂方法 多个工厂创建多种实例
        抽象工厂 用于创建产品簇
'''
#简单工厂
class Person(object):
    def person(self):
        pass


class Chinese(Person):
    def person(self):
        print("国籍: 中国人")


class Japanese(Person):
    def person(self):
        print("国籍: 日本人")

class Korea(Person):
    def person(self):
        print("国籍: 韩国人")

class Factory(object):
    @staticmethod
    def createPerson(type):
        if type == 1:
            return Chinese()
        elif type == 2:
            return Japanese()
        elif type == 3:
            return Korea()

personA = Factory.createPerson(1)
personA.person()
