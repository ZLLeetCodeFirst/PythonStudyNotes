# IOS面试题目
# 1.不用临时变量怎么实现 swap(a, b) 交换a,b的值
# 解法一:使用异或
a = 4
b = 6
a = a ^ b
print(a)
b = b ^ a
print(b)
a = a ^ b
print(a)
print("a = %d,b = %d" % (a,b))

# 解法二:使用加法
a = 4
b = 6
a = a+b
b = a - b
a = b - a
print('01 END==============间隔符号=============')
# 2.在一个二维数组中，每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。请完成一个函数，
# 输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
class Solution:
    def find(self,target,arrary):
        for i in arrary:
            print(i)
            for j in i:
                if target == j:
                    print ('true')


list01 = [[1,2,8,9],[4,7,10,13]]
so = Solution()
so.find(7,list01)

# 3

a = range(1,5)
print(list(range(1,5)))

print('02 END==============间隔符号=============')



