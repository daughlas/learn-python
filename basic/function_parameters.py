#!/usr/bin/python3

def ChangeInt(a):
    a = 10


b = 2
ChangeInt(b)
print(b)  # 结果是 2


# !/usr/bin/python3

# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)


# !/usr/bin/python3

# 可写函数说明
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return


# 调用printme函数
printme(str="菜鸟教程")
print('菜鸟教程')

# 可写函数说明
def printInfo(name, age):
    "打印任何传入的字符串"
    print("名字： ", name)
    print("年龄： ", age)
    return

printInfo(age=50, name="ljw")

#可写函数说明
def printInfo2(name, age=35):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printInfo2(age=50, name="runoob")
print("------------------------")
printInfo2(name="runoob")


# 可写函数说明
def printInfo3(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)


# 调用printinfo 函数
printInfo3(70, 60, 50, 40, 30)

def f(a, b, *, c):
    return a + b + c
print(f(2, 4, c=100))