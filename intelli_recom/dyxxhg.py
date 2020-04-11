import numpy
from pandas import read_csv
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

data = read_csv(
    'file:///Users/apple/Desktop/edu_worktime.csv',encoding='GBK'
)


#估计模型参数，建立回归模型
'''
(1) 首先导入简单线性回归的求解类LinearRegression
(2) 然后使用该类进行建模，得到lrModel的模型变量
'''
from sklearn.linear_model import LinearRegression
lrModel = LinearRegression()
#自变量和因变量选择出来
x = data[['edu','worktime']]
y = data[['salary']]

#模型训练
'''
调用模型的fit方法，对模型进行训练
这个训练过程就是参数求解的过程
并对模型进行拟合
'''
lrModel.fit(x,y)

#利用回归模型进行预测
lrModel.predict([[4,3]])
