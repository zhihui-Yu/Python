'''
    set 可变元素 类似java中的set
    特点：
        1. 保存的值是惟一的
        2. 无序
'''

a = set('abscscsscsc')
# print(type(a))

'''
    增删 可同时多个进行
    add 添加
    update 添加新元素
    remove 删除指定元素
    clear 清空
    len 长度
    in 判断是否在其中
'''
a.add('f')
a.update(['d','c','f'])
a.remove('f')
a.clear()
print(a)