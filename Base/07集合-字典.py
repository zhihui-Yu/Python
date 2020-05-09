'''
    字典 dict
        1. 格式有点像json
        2. 是可变元素
    注意：
        1. 默认无序
        2. key必须是不可变对象
        3. 占用空间大  空间换时间
'''
scores = {'mike':80, 'bob':85, 'james':90}
# print(type(scores))

# 下标获取值，必须下标存在，不然会报错
# print(scores['mike'])
# get 获取元素,如果没有则用后面的默认值代替
# print(scores.get('mikes',90))

#修改 可以根据下标修改
# scores['mike']=20
# print(scores['mike'])

#添加 可以用不存在的下标添加
# scores['john']=99
# print(scores['john'])

#del 删除   可以删除某个元素 也可以全删
# del scores['mike']
# del scores
# print(scores)

'''
    获取长度 len
    keys 返回一个包含字典所有key的列表
    values 返回一个包含字典所有value的列表
    item 返回一个包含字典所有key-value的列表
    has_key 判断是否包含某个key 2.7版本
'''
# print(scores.keys())
# print(scores.values())
# print(scores.items())

'''
    遍历 可以用keys、values、item
'''
# for key in scores.keys():
#     print(key,scores[key])

#只能得到value
# for v in scores.values():
#     print(v)

for key,value in scores.items():
    print(key,value)