dic2 = dict.fromkeys(range(32),'咱')
# print(dic2)

dic3 = dic2.copy()
dic2.clear()
# print(dic2)
# print(dic3)

dic4 = {'a':'周','b':'jun','c':'hong','d':'lu'}
print(dic4)
print(dic4.pop('a'))
print(dic4)
print(dic4.popitem())
print(dic4)
dic4.setdefault('小白','周俊')
print(dic4)
# dir(dict)
# print(dir(dict))

# print(dir(set))
f = open('001.txt')
read = f.read()
print(read)

