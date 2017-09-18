## 迭代器
string = 'FishC'
it = iter(string)
print(it)
print(next(it),next(it))


## 生成器

def fibs():
    a = 0
    b = 1
    while True:
        a,b = b, a+b
        yield a
lib = fibs()
print(next(lib))
for each in lib:
    if each > 100:
        break
    print(each,end='  ')
print('\n' ,next(lib))

import MoKuai as mk
mk.zlSum('中华民国')
mk.zlDele('中国')

import M1.MoKuai02 as mk2
mk2.zlSum('苏州')


print(dir(mk2))
