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
#strategy的参数含义  mean mediam most_frequent  分别是平均值 中值  出现频次最高的
imr = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imr = imr.fit(df)
imputed_data = imr.transform(df.values)
print(imputed_data)

#处理类别数据
df = pd.DataFrame([['green','M',10.1,'class1'],
                  ['blue','L',10.2,'class2'],
                  ['red', 'XL', 10.3, 'class3']])
df.columns = ['color','size','price','classlabel']
print(df)


#有序特征的映射
size_mapping = {'XL':3,'L':2,'M':1}
df['size'] = df['size'].map(size_mapping)
print(df)

#类标的编码
import numpy as np
class_mapping = {label:idx for idx,label in enumerate(np.unique(df['classlabel']))}
print(class_mapping)
##将类标转化为证书
df['classlabel'] = df['classlabel'].map(class_mapping)
print(df)

##类标转化为原来的值
inv_class_mapping = {v:k for k,v in class_mapping.items()}
df['classlabel'] = df['classlabel'].map(inv_class_mapping)
print(df)

#使用 LabelEncoder类 转化类标
from sklearn.preprocessing import LabelEncoder
class_le = LabelEncoder()
y = class_le.fit_transform(df['classlabel'].values)
print(y)
#还原为原来的字符串
class_le.inverse_transform(y)

#标称特征上的独热编码
X = df[['color','size','price']].values
print(X)
color_le = LabelEncoder()
print(X[:,0])
X[:,0] = color_le.fit_transform(X[:,0])
# print(X[:,0])
# print(X)


Y = [['10','20','30','4','5'],
     ['10','20','30','4','5'],
     ['10','20','30','4','5'],
     ['10','20','30','4','5'],
     ['10','20','30','4','5']]
yt = pd.DataFrame([['10','20','30','4','5'],
     ['10','20','30','4','5'],
     ['10','20','30','4','5'],
     ['10','20','30','4','5'],
     ['10','20','30','4','5']])
yt.columns = ['a','b','c','d','e']
print(Y)
print(yt)

#独热编码
from  sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categorical_features=[0])
re  = ohe.fit_transform(X).toarray()
print(re)


#通过pandas 中的 get_dummies
du = pd.get_dummies(df[['price','color','size']])
print(du)

#划分为  训练数据  和 测试数据
#开源红酒数据集
import ssl
import urllib
df_wine = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data',header=None)
df_wine.columns = ['Class label','Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium','Total phenols',
                   'Flavanoids','Nonflavanoid phenols','Proanthocyanins','Color intensity','Hue',
                   'OD280/OD315 of diluted wines','Proline']
print('红酒类别Class label',np.unique(df_wine['Class label']))
print(df_wine.head())

#划分 训练数据 和  测试数据 train_test_split
#iloc方法:选取 列或者行
from sklearn.cross_validation import train_test_split
X,y = df_wine.iloc[:,1:].values,df_wine.iloc[:,0].values
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0)

#归一化 特征缩放
from sklearn.preprocessing import  MinMaxScaler
mms = MinMaxScaler()
X_train_norm = mms.fit_transform(X_train)
X_test_norm = mms.transform(X_test)

#标准化  特征缩放
from  sklearn.preprocessing import StandardScaler
stdsc = StandardScaler()
X_train_std = stdsc.fit_transform(X_train)
X_test_std = stdsc.transform(X_test)

#L1正则化 满足数据的稀疏化
from sklearn.linear_model import LogisticRegression
LogisticRegression(penalty='l1')
lr = LogisticRegression(penalty='l1',C=0.1)
lr.fit(X_train_std,y_train)
print('训练结果:',lr.score(X_train_std,y_train))
print('测试结果:',lr.score(X_test_std,y_test))




#序列特征选择方法
from sklearn.base import clone
from itertools import combinations
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

class SBS():
    def __init__(self,
                 estimator,
                 k_features,
                 scoring=accuracy_score,
                 test_size=0.25,
                 random_state=1):
        self.scoring = scoring
        self.estimator = clone(estimator)
        self.k_features = k_features
        self.test_size = test_size
        self.random_state = random_state

    def fit (self,X,y):
            X_train,X_test,y_train,y_test =\
            train_test_split(X,y,test_size=self.test_size,random_state=self.random_state)
            dim = X_train.shape[1]
            self.indices_ = tuple(range(dim))
            self.subsets_ = [self.indices_]
            score = self._calc_score(X_train,y_train,X_test,y_test,self.indices_)
            self.scores_ = [score]

            while dim > self.k_features:
                scores = []
                subsets = []
                for p in combinations(self.indices_,r = dim -1):
                    score = self._calc_score(X_train,y_train,X_test,y_test,p)
                    scores.append(score)
                    subsets.append(p)

                best = np.argmax(scores)
                self.indices_ = subsets[best]
                self.subsets_.append(self.indices_)
                dim -= 1
                self.scores_.append(scores[best])
            self.k_score_ = self.scores_[1]
            return self
    def transform (self,X):
            return X[:,self.indices_]
    def _calc_score(self,X_train,y_train,X_test,y_test,indices):
            self.estimator.fit(X_train[:,indices],y_train)
            y_pred = self.estimator.predict(X_test[:,indices])
            score = self.scoring(y_test,y_pred)
            return score

from sklearn.neighbors import  KNeighborsClassifier
import matplotlib.pyplot as plt
knn = KNeighborsClassifier(n_neighbors=2)
sbs = SBS(knn,k_features=1)
sbs.fit(X_train_std,y_train)

k_feat = [len(k) for k in sbs.subsets_]
plt.plot(k_feat,sbs.scores_,marker='o')
plt.ylim([0.7,1.1])
plt.ylabel('Accuracy')
plt.xlabel('Number of features')
plt.grid()
plt.show()








