#数据预处理 第四章 20170824

import pandas as pd
from io import StringIO
csv_data = '''A,b,c,d
            1.0,,3.0,4.0
            2,3,,4
            0.0,,,
            5,6,7,8'''
df = pd.read_csv(StringIO(csv_data)) #获取CSV格式的数据
print(df)
df2 = df.isnull().sum()  #数值为空的列  统计数量
print(df2)
print(df.values)        #数组
print(df.dropna())      #删除包含缺失值的行
print(df.dropna(axis=1))  #删除至少缺失一个值的列
print(df.dropna(how='all'))  #改行的所有数值缺失,则删除
print(df.dropna(thresh=4))  #删除没有至少4个非空的行
print(df.dropna(subset=['A'])) #删除该列缺失的行

#缺失数据填充
from sklearn.preprocessing import  Imputer
imr = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imr = imr.fit(df)
imputed_data = imr.transform(df.values)
print(imputed_data)

