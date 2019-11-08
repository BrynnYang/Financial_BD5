# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:46:48 2019

@author: yangfan
"""


#import matplotlib.pyplot as plt 
import pylab as plt
import pandas as pd
dataset = pd.read_table('result_5_40.txt', header=None, sep=' ')
n = len(dataset)
plt.title('Result')
plt.xlabel('X')
plt.ylabel('Y')
for i in range(n):
    if dataset[2][i] == 1:
        plt.plot(dataset[0][i], dataset[1][i], 'or')
    elif dataset[2][i] == 2:
        plt.plot(dataset[0][i], dataset[1][i], 'og')
    elif dataset[2][i] == 3:
        plt.plot(dataset[0][i], dataset[1][i], 'ob')
    elif dataset[2][i] == 4:
        plt.plot(dataset[0][i], dataset[1][i], 'oy')
    elif dataset[2][i] == 5:
        plt.plot(dataset[0][i], dataset[1][i], 'ok')
    '''
    elif dataset[2][i] == 6:
        plt.plot(dataset[0][i], dataset[1][i], 'oc')
    elif dataset[2][i] == 7:
        plt.plot(dataset[0][i], dataset[1][i], 'om')
    '''
plt.show()