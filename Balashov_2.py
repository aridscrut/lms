# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lNbe4Ek3-qxIedxi1ggK7TvY_tHjbdpU
"""

#Задание 1
a = int(input())
if a % 2 == 0:
  print('Данное число четное')
else:
  print('Данное число не является четным')

a = float(input())
b = float(input())
if a > b:
  print(a)
else:
  print(b)

a = int(input())
b = int(input())
if (a % 2 == 0 and b % 2 == 0) or (a % 2 != 0 and b % 2 != 0):
  print('NO')
else:
  print('YES')