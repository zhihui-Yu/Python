'''
    异常：当检测出异常，如果不处理则会让程序无法继续运行

    语法： try... except .. (else ... finally..)
          raise 异常名称 ： 抛出一个异常
    注意：
        1.多层嵌套语句中，内部出现的异常 外部有处理就可以，不需要每层都处理
        2.当 except 后面不写异常时，默认处理所有异常

'''
try:
    open("123.text",'r')
except FileNotFoundError as result:
    print("错误信息 : ",result.strerror)

#当需要捕获多个时，可以用元组存储异常
try:
    # open("123.text",'r')
    print(1/0)
except (FileNotFoundError,ZeroDivisionError) as result:
    print("错误信息 : ",result)

# else: 当没有捕获异常执行的语句
try:
    print("123")
except :
    print("Error")
else:
    print("NO Error")
finally:
    print("End")

'''
    自定义异常
'''
class ShortInputException(Exception):
    def __init__(self,len,atleast):
        self.len = len
        self.atleast = atleast

def main():
    try:
        s = input("输入一个字符串：")
        if len(s) < 3:
            raise ShortInputException(len(s),3)
    except ShortInputException as result:
        print("输入的字符串长度为%d,但是至少需要输入长度为%d"%(result.len,result.atleast))
    else:
        print("输入字符串为%s,成功"%s)
main()

'''
    raise 抛出异常
'''

a = False
if a :
    print("无异常")
else:
    raise Exception
