'''
    元组 tuple 可变元素，因为存储的是地址 地址元素变了，但是地址不变，得到的值仍然会变
    用 () 赋值，当只有一个时 那一个元素本身是什么类型 变量就是什么类型
    只有一个时，加入逗号也会变成元组
'''
# tuple = (1,)
# print(type(tuple))

'''
    修改元组内的可变元素 只能通过坐标来修改
    注意：
        元组是不可变元素
'''
aTuple = ('Mike',['Poal','Deel'],'Galer')
aTuple[1][1]='James'
print(type(aTuple[1]))