# -*- coding:utf-8 -*-
'''
    单行注释 #
    多行注释 三个单引号

    为保证编译不乱码  加上以下两句(二选一)
        # -*- coding:utf-8 -*-
        # coding=utf-8

    Python 中对于变量  不需要指定类型
'''

# 关键字列表
# import keyword
# print(keyword.kwlist)

#print 输出
# print("hello","word")
# print("%d+%d=%d"%(100,200,300))
# print("%d"%(100))
# print("%d"%100)
# print("hello%s"%' world')
# print("%.3f"%3.1415926)
# print("key-"*10)

#输入
#  Python2 中 raw_input 和 Python3 中 input 一样，把接收的东西都当做字符串
#  Python2 中接收到什么就是什么类型
# from Tools.scripts.treesync import raw_input

# sum = input("输入总数：")
# print(type(sum))
# sum = raw_input("输入总数：")
# print(type(sum))

#运算符
# + - * / // **
# print("%d^3 = %d"%(2,2**3))
# 一个 / 就是除以  得出 会议余数显示
# print("%d/%d=%.2f"%(5,2,5/2))
# 两个 // 除以只有商
# print("%d/%d=%.2f"%(5,2,5//2))
# 求模  求余
# print("%d"%(5%2))

#逻辑运算符
# print("true and false : ",(True and False))
# print("true and true : ",(True and True))
# print("true or false : ",(True or True))
# print("true or true : ",(True or True))
# print("not False : ",(not False))
# print("not true : ",(not True))

