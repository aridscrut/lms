# -*- coding: utf-8 -*-
"""lesson3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/144OUKzyvW4JjndASra8vz2RFCV1BycMo
"""

#Задание 1
s = str(input())
summ = 0
for i in s:
  summ += int(i)
print(summ)

#Задание 2
n = int(input())
res = 1
for i in range(2, n + 1):
  res = res*i
print(res)

#Задание 3
a = int(input())
i = 1
while i <= a:
  if i % 7 == 0:
    print(i)
  i += 1