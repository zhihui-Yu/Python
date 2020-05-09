'''
    文件操作
'''

#打开或者创建文件 默认当前路径 可以点击open看读写参数
f = open("text.txt",'rb+')

# f.write("hahah")
#读num个字符
# print(f.read(1024))

# content = f.readlines()
# print(type(content))
# i = 1
# for temp in content :
#     print("%d:%s"%(i,temp))
#     i += 1


print("读取数据为：",f.read(3))
#获取当前位置
print("当前位置是：",f.tell())

#定位到某个位置
'''
    seek(offset, from)有2个参数
        offset:偏移量
        from:方向
            0:表示文件开头
            1:表示当前位置
            2:表示文件末尾
'''
f.seek(-2,2)
print("当前位置是：",f.tell())

f.close()

import os
# Windows 返回 ‘nt'; Linux 返回’posix'
print(os.name)
print(os.getcwd())
print(os.listdir())

