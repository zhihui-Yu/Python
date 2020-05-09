#列表
'''
    len 获取列表长度
    可以通过索引来访问元素 下标从0开始

'''
list = ['Michael','Bob','John']
# print(list)
# print(type(list))
# print(len(list))
# print(list[0])
# for i in list:
#     print(i)

'''
    增加 append 直接加载末尾
        extend 每一个char都单独添加末尾
        insert  注意：  insert(index,object)
'''
# print(list.append('James1'),list)
# print(list.insert(4,'James2'),list)
# print(list.extend('James3'),list)

'''
    修改 要通过下标来确定要修改的是哪个元素，然后才能进行修改
'''
# list[2] = 'Ross'
# print(list)

'''
    查找 in 判断是否存在
        not in 判断是否不存在
        count 判断元素有几个
        index 判断区间中有几个元素  左闭右开
'''
# print('Bob' in list)
# print('Bob' not in list)
# print(list.count('Bob'))
# print(list.index('Bob',0,3))

'''
    删除 del 根据下标进行删除，其实可以删除所有变量
        pop 默认删除最后一个元素
        remove 根据元素的值删除
'''
# print(list.pop(),list)
# del list[0]
# list.remove('Bob')
# print(list)

'''
    排序 sort  当参数 reverse=True 时 倒序
        
'''
# list = [1,3,4,2,5,7,6]
# print(list.sort(),list)
# print(list.sort(reverse=True),list)

# 遍历索引加值
# for i,v in enumerate(list) :
#     print(i,v)