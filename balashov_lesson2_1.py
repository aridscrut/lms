# -*- coding: utf-8 -*-
"""Balashov_lesson2-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CgMSPmqiiQSneFPbUYrXEEqYeBMCxIsQ
"""

import math

import numpy as np
import time

a = np.array([2,7,4,9])

b = a*2 + np.array([1,2,3,4])
print(b)

c = np.arange(1, 10, 2)
print(c)

start_time = time.time()
l1 = [i for i in range(1, 1000000)]
l2 = [i for i in range(1, 1000000)]
res = [a + b for a, b in zip(l1, l2)]
t = time.time() - start_time
start_time_np = time.time()
ar1 = np.arange(1,1000000)
ar2 = np.arange(1,1000000)
res = ar1 + ar2
t1 = time.time() - start_time_np
print(t, t1)

a = np.array([2,5,7,0,4])
print((a>3).sum())

a.mean()

a.std()

a.cumsum()

np.full(5,7)

np.linspace(2, 3, 5)

np.ones(4)

np.zeros(4)

np.pi

np.e

print(np.sin(np.pi/2))

np.sin([0, np.pi / 4, np.pi / 2])

np.zeros((3, 5))

np.ones((4,6))

np.eye(4)

a = np.array([[1,3,0],[1,9,9],[8,9,0], [5,3,1]])

a.shape

len(a)

a.size

a[1,2]

a[3,2]

a = np.linspace(0,5,6)
print(a)
a.shape

a.shape = 3, 2
print(a)

a*2

a = np.array([[1,2,3],[2,0,7],[1,2,5],[5,7,8]])
print(a)
print(a.T)

a.sum(axis = 1)

a[:, :1]

z = np.ones((10,10))
z[1:-1, 1:-1] = 0
print(z)

s = np.zeros((8,8))
s[1::2, ::2] = 1
s[::2, 1::2] = 1
print(s)