# -*- coding: utf-8 -*-
"""lesson9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ww_FmPKaPPifW-g6caBD4JJMOogANU5d
"""

#Задание 1
def nok(a, b):
    c = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return c // (a + b)

a = int(input())
b = int(input())
print(nok(a, b))

#Задание 2
n = int(input("n="))
reslist=[]
for i in range(2, n+1):
    for j in reslist:
        if i % j == 0:
            break
    else:
        reslist.append(i)
print(reslist)

#Задание 3
def denominators(n):
    reslst = []
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            reslst.append(i)
    return reslst

n = int(input("n="))
print(denominators(n))