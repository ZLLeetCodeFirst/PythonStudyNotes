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