#!/usr/bin/env python
# encoding: cp936
"""
@author:lichengyan
@file: zipTest.py(zip,map)
@time: 2017/10/24
"""

def run():
    a = [9,8,7,45,66]
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print matrix
    print u"矩阵行列互换(zip):",zip(*matrix)

def count(x):
    return x*2

def run1():
    a = [9,8,7,45,66]
    print "map:",map(count,a)

if __name__ == '__main__':
    run()
    run1()