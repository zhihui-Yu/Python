'''
    单例模式 实例只有一个且只初始化一次
            删除时，会有一个计数器，当所有引用都没有时 才真的删除

'''
class singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance :
            cls.__instance = object.__new__(cls)
            print("new")
        return cls.__instance

    def __del__(self):
        print("del")

a = singleton("18","20")
b = singleton("19","20",'30')

print(a)
print(b)

a.age = 19
print(b.age)

del a
print("b",b)