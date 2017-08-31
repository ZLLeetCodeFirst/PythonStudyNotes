string01 = '{a}tang{b}'.format(a='xiao',b='lang')
print(string01)
#输出结果
# xiaotanglang

string02 = '{0} i love lang {1}'.format(string01,string01)
print(string02)
#输出结果
# xiaotanglang i love lang xiaotanglang

def zlfunctioin(a,b):
    '函数文档,第一次编写'

    print('zhoulu')

help(zlfunctioin)

#=============== Start 闭包#     ==================
#x = 10
def fun1(x):
    def fun2(y):
        return x * y
    return fun2
i = fun1(5)(8)
print(i)
#输出结果
# 40

def fun3():
    x = 10
    def fun4():
        nonlocal x
        x = x*x
        return x
    return fun4()
j = fun3()
print(j)
#输出结果
# 100

# lambda方法 的使用
k = lambda x,y:x+y
print(k(3,4))
# 输出结果
# 7

# filter 方法 过滤器 两个形参,第一个为函数对象,第二个为输入参数(可迭代对象,元组,序列),filter返回第二个参数在第一个函数对象执行结果非零的(第二个参数中)对象
def jishu(x):
    return x%2
su = list(filter(jishu,range(10)))
print(su)
#输出结果
# [1, 3, 5, 7, 9]

# map 方法 第一个形参为 函数对象,第二个为可迭代对象(元组,序列),返回可迭代对象在函数依次执行的结果
def map02(x):
    return x*x
jiang = list(map(map02,[1,2,3,4,5,6]))
print(jiang)
# 输出结果
# [1, 4, 9, 16, 25, 36]

# ========== 汉诺塔 ========
def hanta(n,x,y,z):
    if n == 1:
        print(x ,'->', z)
    else:
        hanta(n-1,x,z,y)
        print(x ,'->', z)
        hanta(n-1,y,x,z)

i = int(input('请输入整数:'))
hanta(i,'一柱','二柱','三柱')