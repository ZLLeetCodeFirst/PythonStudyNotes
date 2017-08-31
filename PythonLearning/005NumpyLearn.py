import numpy as np
#=============== Start 一维数组   ==================
#一维数组的 索引和切片
a = np.arange(9)
# 3-7 不包括7
b = a[3:7]
print(b)
# 0-7步长为2
c = a[:7:2]
print(c)
# 下标翻转数组
d = a[::-1]
print(d)
# 输出结果
# [3 4 5 6]
# [0 2 4 6]
# [8 7 6 5 4 3 2 1 0]


#=============== Start 多维数组的切片和索引    ==================
# reshape 改变数组的纬度,参数为正整数元组
a = np.arange(24).reshape(2,3,4)
print(a)
# 输出结果
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
#
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

# 多维数组的切片
b = a[0,0,0]
print(b)
# 输出结果
# 0
c = a[:,0,0]
print(c)
# 输出结果
# [ 0 12]
d = a[0]
print(d)
# 输出结果
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

e = a[0,:,:] #等价于e = a[0,...]   多个冒号等价于...
print(e)
# 输出结果
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

f = a[0,1]
print(f)
# 输出结果
# [4 5 6 7]

g = a[0,1,::2]
print(g)
# 输出结果
# [4 6]

h = a[...,1]
print(h)
#输出结果
# [[ 1  5  9]
#  [13 17 21]]

i = a[:,1]
print(i)
# 输出结果
# [[ 4  5  6  7]
#  [16 17 18 19]]

j = a[0,:,-1]
print(j)
# 输出结果
# [ 3  7 11]

k = a[0,:,1]
print(k)
#输出结果
# [1 5 9]

l = a[0,::-1,-1]
print(l)
#输出结果
# [11  7  3]

m = a[0,::2,-1]
print(m)
#输出结果
# [ 3 11]

n = a[::-1]
print(n)
#输出结果
# [[[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]
#
#  [[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]]

#=============== Start 改变数组的纬度    ==================
# ravel flatten reshape resize

print(a)
b = a.ravel()
print(b)
print(a)
c = a.flatten()
print(c)
print(a)

#=============== Start 数组的组合    ==================
print('#=============== Start 数组的组合    ==================')
a = np.arange(9).reshape(3,3)
b = 2 * a
#水平组合 hstack  和concatenate 函数也可以实现,axis = 1 可以实现
c = np.hstack((a,b))
print(a)
print(b)
print(c)

#输出结果
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]
# [[ 0  2  4]
#  [ 6  8 10]
#  [12 14 16]]
# [[ 0  1  2  0  2  4]
#  [ 3  4  5  6  8 10]
#  [ 6  7  8 12 14 16]]

# 垂直组合 vstacK 或者 concatenate 函数 axis=0
d = np.vstack((a,b))
print(a)
print(b)
print(d)
# 输出结果
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]
# [[ 0  2  4]
#  [ 6  8 10]
#  [12 14 16]]
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 0  2  4]
#  [ 6  8 10]
#  [12 14 16]]

# 03 深度组合 dstack
e = np.dstack((a,b))
print(a)
print(b)
print(e)
print(e.shape)
#输出结果
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]
# [[ 0  2  4]
#  [ 6  8 10]
#  [12 14 16]]
# [[[ 0  0]
#   [ 1  2]
#   [ 2  4]]
#
#  [[ 3  6]
#   [ 4  8]
#   [ 5 10]]
#
#  [[ 6 12]
#   [ 7 14]
#   [ 8 16]]]
# (3, 3, 2)

# 04 列组合 column_stack
# 对于一维数组按照列方向进行组合 对于二维数组和hstack效果相同
v1 = np.arange(3)
v2 = np.arange(3)
print(v1)
print(v2)
f = np.column_stack((v1,v2))
print(f)
#输出结果
# [0 1 2]

# [0 1 2]

# [[0 0]
#  [1 1]
#  [2 2]]

h = np.column_stack((a,b))
print(h)
print(c)
print(c==h)#使用 == 直接进行数组比较
#输出结果
# [[ 0  1  2  0  2  4]
#  [ 3  4  5  6  8 10]
#  [ 6  7  8 12 14 16]]
# [[ 0  1  2  0  2  4]
#  [ 3  4  5  6  8 10]
#  [ 6  7  8 12 14 16]]
# [[ True  True  True  True  True  True]
#  [ True  True  True  True  True  True]
#  [ True  True  True  True  True  True]]

#行组合 row_stack 二维数组和vstack效果相同
k = np.row_stack((v1,v2))
print(k)
#输出结果
# [[0 1 2]
#  [0 1 2]]
j = np.vstack((v1,v2))
print(j)
print(j == k)
#输出结果
# [[0 1 2]
#  [0 1 2]]
# [[ True  True  True]
#  [ True  True  True]]

# =============== Start 数组的f分割    ==================
print('#=============== Start 数组的分割    ==================')
a = np.arange(9).reshape(3,3)
b = 2 * a
## 02水平分割 hsplit 或者 split 参数 axis = 1 都可以实现
c = np.hsplit(a,3)
print(c)
#输出结果
# [array([[0],
#        [3],
#        [6]]),
# array([[1],
#        [4],
#        [7]]),
#  array([[2],
#        [5],
#        [8]])]

## 02垂直 分割 vsplit 或者 split函数axis=0都可以完成
d = np.vsplit(a,3)
print(d)
#输出结果
# [array([[0, 1, 2]]),
#  array([[3, 4, 5]]),
#  array([[6, 7, 8]])]

## 03 深度分割 dsplit 按照深度方向分割数组
e = np.arange(27).reshape(3,3,3)
print(e)
f = np.dsplit(e,3)
print(f)
# #输出结果
# [[[ 0  1  2]
#   [ 3  4  5]
#   [ 6  7  8]]
#
#  [[ 9 10 11]
#   [12 13 14]
#   [15 16 17]]
#
#  [[18 19 20]
#   [21 22 23]
#   [24 25 26]]]
#
# [array([[[ 0],
#         [ 3],
#         [ 6]],
#
#        [[ 9],
#         [12],
#         [15]],
#
#        [[18],
#         [21],
#         [24]]]), array([[[ 1],
#         [ 4],
#         [ 7]],
#
#        [[10],
#         [13],
#         [16]],
#
#        [[19],
#         [22],
#         [25]]]), array([[[ 2],
#         [ 5],
#         [ 8]],
#
#        [[11],
#         [14],
#         [17]],
#
#        [[20],
#         [23],
#         [26]]])]


#=============== Start 数组的遍历#     ==================

#Numpy 数组的遍历 flat 属性  返回 numpy.flatiter对象(唯一获取flatiter的方式)
a = np.arange(4).reshape(2,2)
print(a)
f = a.flat
print(f)
for item in f:
    print(item)

#输出结果
# [[0 1]
#  [2 3]]
# <numpy.flatiter object at 0x10082c000>
# 0
# 1
# 2
# 3






