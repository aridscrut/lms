# -*- coding: utf-8 -*-
"""lesson4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XQDvYBAlnt4_IbcBhM0RTlc8oWlXSHCA
"""

#Задание 1
my_str = str(input())
my_list = my_str.split()
print(my_list[::-1])

#задание 2
mystr = str(input())
print(mystr[::2])

#Задание 3
my_str = str(input())
my_list = my_str.split()
N = my_list.pop()
res = [int(i) ** int(N) for i in my_list]
print(res)

#Задание 4
my_str = str(input())
my_elem = str(input())
print(my_str.replace(my_elem, my_elem + my_elem))

#Задание 5
my_str = str(input())
xcount = my_str.count('x')
ycount = my_str.count('y')
print('x: ' + str(xcount) + ', y: ' + str(ycount))

#Задание 6
my_str = str(input())
startpos = my_str.find('(')
endpos = my_str.find(')')
while startpos != -1:
  print(my_str[startpos + 1:endpos])
  startpos = my_str.find('(', endpos + 1)
  endpos = my_str.find(')', endpos + 1)