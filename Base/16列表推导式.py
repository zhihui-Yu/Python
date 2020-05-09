'''
    列表推导式

'''
a = [i for i in range(1,10)]
a = [(i,j) for i in range(1,10) for j in range(1,10)]
a = [(i,j,k) for i in range(1,10) for j in range(1,10) for k in range(1,10)]
print(a)
#list
print(type(a))

#tuple
b = (1,)
print(type(b))

#list
c = [1,2,3]
print(type(c))

#dict
d = {"name":"zhangsan"}
print(type(d))

#set
e = {1,2,3}
print(type(e))