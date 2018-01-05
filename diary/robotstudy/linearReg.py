#!/user/bin/env python
# -*- coding:utf-8 -*-
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

def sigmoid(Z):
    return 1.0/(1.0+np.exp(-Z))

def main():
    z = np.arange(-7,7,0.1)
    phi_z=sigmoid(z)

    plt.plot(z,phi_z)
    plt.axvline(0.0,color='k')
    plt.axhspan(0.0,1.0,facecolor='1.0',alpha=1.0,ls='dotted')
    plt.axhline(y=0.5,ls='dotted',color='k')
    plt.yticks([0.0,0.5,1.0])
    plt.ylim(-0.1,1.1)
    plt.xlabel('z')
    plt.ylabel('$\phi (z)$')
    plt.show()

def main_new():
    # train = loan_data.iloc[0: 55596, :]
    # test = loan_data.iloc[55596:, :]

    # 导入
    lr = LogisticRegression(C=0.001, class_weight='balanced', dual=False,
                       fit_intercept=True, intercept_scaling=1, max_iter=1000,
                       multi_class='ovr', n_jobs=1, penalty='12', random_state=None,
                       solver='liblinear', tol=0.0001, verbose=0, warm_start=False)
    # # 训练
    # lr.fit(train_feature,label)
    # # 预测
    # predict['label'] = lr.predict(predict_feature)

if __name__ == '__main__':
    main_new()