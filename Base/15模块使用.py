'''
    导入模块
        import (模块名称)
            调用时： 模块名.函数名()
        from (模块名称) import 函数名称[,函数名...]
            调用时: 函数名()
    定位模块过程：
        当你导入一个模块，Python解析器对模块位置的搜索顺序是：
            1、当前目录
            2、如果不在当前目录，Python则搜索在shell变量PYTHONPATH下的每个目录。
            3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/
            4、模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。

    模块即为py文件，每一个文件都可以当做模块来引入
'''
import math
print(math.sqrt(2))

from math import sqrt,floor
print(sqrt(3))
print(floor(2.5))

#导入自定义模块
import module
print(module.add(1,2,lambda x,y:x+y))