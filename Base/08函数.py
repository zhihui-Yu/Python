'''
    函数：可以带参数，但是不需要写类型，函数可以有返回值也可以没有
'''
# def fun():
#     return "fun()"
#
# print(fun())

# def add(a,b):
#     return a+b
#
# print(add(1,2))

#全局变量可以在函数中用，但是在函数中要加global 关键字才能改变变量值
# count = 10
# def fun():
#
#     # print(count)
#     global count
#     count = 20
#     print(count)
# fun()
# print(count)

#默认参数，在使用函数时，没有补充则用默认值
# def div(a,b=1):
#     print(a/b)
# div(3)
# div(3,2)

# 不定长参数  args 接收元组  **kwargs 接收k-v参数
# def fun(a,b,*args,**kwargs):
#     print("a=",a)
#     print("b=",b)
#     print("*args=",*args)
#     print("*kwargs=",*kwargs)
#
# fun(1,2,3,4,5,7,8,m=1)

# 对于不可变类型，因变量不能修改，所以运算不会影响到变量自身；
# 而对于可变类型来说，函数体中的运算有可能会更改传入的参数变量。
# def add(a):
#     a += a;
# a = 1
# a = [1,2]
# add(a)
# print(a)

#递归函数  斐波那契 python 中只有这样类似三目运算符的作用
# def fib(n):
#     return 1 if n==1 else n * fib(n-1)
#
# print(fib(3))

# 匿名函数 使用场合 ：函数作为参数传递 或者内置函数
# sum = lambda a,b : a+b
# print(sum(1,2))
# def fun(a, b, opt) :
#     print(a)
#     print(b)
#     print("result=",opt(a,b))
#
# 函数作为参数传递
# fun(1,2,lambda x,y:x+y)
# fun(1,2,lambda x,y:x-y)
# fun(1,2,lambda x,y:x*y)
# fun(1,2,lambda x,y:x/y)

# 内置函数
# students = [{"name":"zhangsan","age":18},{"name":"lisi","age":19},{"name":"wangwu","age":17}]
# 按name排序
# students.sort(key=lambda x:x['name'])
#按age排序
# students.sort(key=lambda x:x['age'])
# print(students)

