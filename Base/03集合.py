
'''
1、可变类型，值可以改变：
    列表 list
    字典 dict
    set  （没有value的字典）
2、不可变类型，值不可以改变：
    数值类型 int, long, bool, float
    字符串 str
    元组 tuple
'''

#字符串
# name = "zhangsan"
# str = 'lisi'
# name = name + "-" + str
# for i in name :
#     print(i,end="\t")
# print(name[5])

#切片的语法：[起始:结束:步长]  起始结束 左闭右开
# print(name[::])
#-1 从后往前
# print(name[::-1])
# 区间位置 从后往前
# print(name[5:2:-1])


# 字符串操作

#检测 lisi 是否包含在 name 中，如果是返回开始的索引值，否则返回-1
# print(name.find("lisi"))

#跟find()方法一样，只不过如果wangwu不在 name中会报一个异常.
# print(name.index("wangwu"))

#从右边开始找
# print(name.rfind("zhangsan"))

#返回 name中 n 出现的次数
# print(name.count("n"))

# 将 lisi 字符串 用 wangwu 字符串替换 返回替换完的字符串 但是原字符串不会变
# print(name.replace("lisi","wangwu"),name)

#将name以a分割，如果指定 maxsplit 分割次数，则只分割maxsplit+1个字符串，且从前往后，返回分割后字符串
# print(name.split("a",maxsplit=1))

#把首字符大写 返回改后的字符串
# print(name.capitalize())

#把字符串的每个单词首字母大写
# print(name.title())

#检测是否以 zhangsan  开头
# print(name.startswith("zhangsan"))

#检测是否以 lisi 结尾
# print(name.endswith("lisi"))

#将所有大写 变为小写
# print(name.lower())

#将所有字符变为大写
# print(name.upper())

#返回一个长度为20的字符串 超出原字符串则用#填充在左边   长度低于原字符串则显示原字符串
# print(name.ljust(20,'#'))

#返回一个长度为20的字符串 超出原字符串则用#填充在右边  长度低于原字符串则显示原字符串
# print(name.rjust(20,'#'))

#返回一个长度为20的字符串 超出原字符串则用#填充在中间  长度低于原字符串则显示原字符串
# print(name.center(20,'#'))

#删除 空白字符 lstrip 删左边  rstrip 删右边  strip 左右都删
# print(name.rstrip())
# print(name.lstrip())
# print(name.strip())

#查找位置  从右边开始找
# print(name.rindex("lisi"))

#以 a 为中心 截成三部分
# print(name.partition("a"))

#以 a 为中心 截成三部分 从右边开始的
# print(name.rpartition('a'))

#按照换行符分隔，返回一个包含各行作为元素的列表
# print(name.splitlines())

#判断是不是都是字母
# print(name.isalpha())

#判断是否都是字母
# print(name.isdigit())

#判断是否都是字母或数字
# print(name.isalnum())

#判断是否只包含空格
# print(name.isspace())

#在name中插入 一个元素 会重复name
# print(name.join(["b","c",'d']))
