# 格式化输出字符串
print('%.3s'% 'zhouzhou')#前3
print('%.*s' % (6,'zhouzhouzhou'))#前6
print('%10.4s' % 'zhouzhou')#宽度为10,截取前4位,左边补空格
print('%-10.3s' % 'zhouzhou')#宽度为10,截取前3,右边补空格

zllist = ['zhou','Python','IOS','zhou','xcode','pycharm','IPython']

for i in range(10):
    #print('----',i)
    if i%2 != 0:
        print(i)
        continue
    i += 2
    print('+++',i)


#三种删除方法
zllist = ['zhou','Python','IOS','zhou','xcode','pycharm','IPython']
# 01 remove
delete01 = zllist.remove('zhou')
print(zllist)
# 02 del 删除 list
del zllist[1]
print(zllist)
# 03 有返回值删除
delete03 = zllist.pop(1)
print(delete03)
print(zllist)

#=============== START              ==================
# List切片 [1:2] 语法  拷贝 List 获得新的List 【起始位置(未设置从0开始):结束位置(未设置默认到尾部)】
print('[ : ]语法应用')
zllist = ['zhou','Python','IOS','zhou','xcode','pycharm','IPython']
a = zllist[1:2]
print(a)
b = zllist[1:]
print(b)
c = zllist[:1]
print(c)

# 查找该类的所有方法
#print(dir(zllist))

# List 原序列 翻转 返回新序列
zllist02 = [1,2,3,4,5,9,80,7,68]
zllist02.reverse()
print(zllist02)

# sort 方法  排序 正序
zllist02.sort()
print(zllist02)
#sor 倒序
zllist02.sort(reverse=True)
print(zllist02)


#=============== END              ==================

#=============== START 常犯的三种错误              ==================
def fn(var1,var2 = []):
    var2.append(var1)
    print(var2)

# fn(3)
# fn(4)
# fn(5)
# 解决方法
def fn2(var1,var2 = None):
    if not var2:
        var2 = []
    var2.append(var1)
    print(var2)
fn2(3)
fn2(4)
fn2(5)

class URLCatcher(object):
	urls = []
	def add_url(self,url):
		self.urls.append(url)

a = URLCatcher()
a.add_url('www.baidu.com')
b = URLCatcher()
b.add_url('www.google.com')
#print(b.urls)
#print(a.urls)

class URLCatcher02(object):
    def __init__(self):
        self.urls = []
    def add_url(self,url):
        self.urls.append(url)
c = URLCatcher02()
c.add_url('www.baidu.com')
d = URLCatcher02()
d.add_url('www.google.com')
print(c.urls)
print(d.urls)


change = {'1':'啊','2':[2,2]}
change02 = change.copy()
change02['4'] = '斯'
# change = {'1':'啊','2':[3,3],'3':'吃'}
print('change的值是:',change,'change02的值是:',change02)



#=============== END 常犯的三种错误              ==================
#=============== START 元祖  * 重复操作符            ==================
temp = (1,2,3)
temp = 8 * temp
print(temp)

#=============== Start 字符串              ==================
str = 'i love tanglang zhong'

str.capitalize() #字符串的第一个字符改为大写
str.casefold()  #所有字符改为小写
str.center(100)  #字符串居中,使用空格填充致width的新字符串
str.count('l',1,4)  #查找字符串出现次数
str.encode(encoding='utf-8',errors='strict')  #制定编码格式进行编码
str.endswith('u',0,10)  #检查字符串是否已'u'结束
str.expandtabs(tabsize = 8) #将字符串tab符号(\t) 转化为空格数为8的空格
str.find('z')  #检测'z'是否包含在字符串中
str.index('z')  #跟find方法一样,如果不在string中会产生异常
str.isalnum()  #如果字符串至少有一个字符并且所有字符都是字母或者数字则返回TRUE
str.isalpha()  #如果字符串至少有一个字符并且所有字符都是字母 ,则返回TRUE
str.isdecimal()  #如果字符串只包含十进制数字则返回TRUE
str.isdigit()  #如果字符串只包含数字则返回TRUE
str.islower()   #如果字符串中至少包含一个区分大小写的字符,并且这些字符都是小写,返回TRUE
str.isnumeric() #如果字符串只把韩数字字符,返回TRUE
str.isspace()  #只包含空格,返回TRUE
str.istitle()   #所有的单词都是以大写开始,其余字母均为小写,则返回TRUE
str.isupper()  #字符都是大写,则返回TRUE
str.join('zhou')  #以字符串作为分隔符,插入到'zhou'中所有的字符之间
str.ljust(10)  #返回一个左对齐的字符串,并使用空格填充致长度为width的新字符串
str.lower()  #所有大写字符转化为小写
str.lstrip('zhou')  #去掉字符串左边的所有空格
str.partition('zhou') #
str.replace('zhou','lu',1)#替换字符串
str.rfind('z',0,4)  #类似find(),从右边开始查找
str.rindex('l',0,5) #类似index(),从右边开始
str.rjust(10)  #返回右对齐的字符串,填充长度致width
str.rpartition('tang')
str.rstrip('lang')  #删除字符串末尾空格
str.split(sep=None,maxsplit=-1)  #分割字符串为列表
str.splitlines(([keepends]))  #按照'\n'分割,返回元祖
str.startswith(prefix='dd',start=0,end=10)  #字符串是否以prefix开头
str.strip(chars='')#删除前边和后边的所有空格,如果指定chars,则删除chars
str.swapcase()  #翻转字符串中的大小写
str.title()     #返回标题化的字符串,(所有单词以大写开始,其余字符为小写
str.translate()
str.upper()  #小写转化为大写
str.zfill(10)  #返回长度为width的字符串,原字符串右对齐,前边用0填充




#=============== Start Numpy              ==================
a = range(5)
print(a)