1
# for i in range(1,5):
#     print('x' * i)
2
# x = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],

# ]
3
# for i in range(2,12,2):
#     print('x' * i)
4
# for i in range(1,10):
#     print(str(i)+str(i)+str(i))
5
# x = 10
# while x >= 1:
#     x = x-1
#     print(str(x) * x)
6
# x = 6
# while x >= 1:
#     x = x-1
#     print('*' * x)
7
# events = [
#   {
#     'date':  '2019-12-29',
#     'event': 'name1'
#   },
#   {
#     'date':  '2019-12-31',
#     'event': 'name2'
#   },
#   {
#     'date':  '2019-12-29',
#     'event': 'name3'
#   },
#   {
#     'date':  '2019-12-30',
#     'event': 'name4'
#   },
#   {
#     'date':  '2019-12-29',
#     'event': 'name5'
#   },
#   {
#     'date':  '2019-12-31',
#     'event': 'name6'
#   },
#   {
#     'date':  '2019-12-29',
#     'event': 'name7'
#   },
#   {
#     'date':  '2019-12-30',
#     'event': 'name8'
#   },
#   {
#     'date':  '2019-12-30',
#     'event': 'name9'
#   },
# ]
# MyBox = {}
# for event in events:
#     date = event['date']
#     event_n = event['event']
#     if date not in MyBox:
#         MyBox[date] = [event_n]
#     else:
#         MyBox[date].append(event_n)
# print(MyBox)

8
# events = [
#     {
#         'date': '2019-12-529',
#         'event': 'name1'
#     },
#     {
#         'date': '2019-12-3641',
#         'event': 'name1',
#     },
#     {
#         'date': '2019-12-329',
#         'event': 'name3',
#     },
#     {
#         'date': '2019-12-30',
#         'event': 'name1'
#     },
#     {
#         'date': '2019-12-229',
#         'event': 'name3'
#     },
#     {
#         'date': '2019-12-131',
#         'event': 'name3'
#     },
#     {
#         'date': '2019-12-129',
#         'event': 'name7'
#     },
#     {
#         'date': '2019-12-230',
#         'event': 'name7'
#     },
#     {
#         'date': '2019-12-430',
#         'event': 'name9'
#     },
# ]

# MyBox = {}
# for event in events:
#     date = 
9
# events = [
#   {
#     'date':  '2019-12',
#     'event': 'name1'
#   },
#   {
#     'date':  '2019-12',
#     'event': 'name2'
#   },
#   {
#     'date':  '2019-11',
#     'event': 'name3'
#   },
#   {
#     'date':  '2019-11',
#     'event': 'name4'
#   },
#   {
#     'date':  '2020-10',
#     'event': 'name5'
#   },
#   {
#     'date':  '2020-10',
#     'event': 'name6'
#   },
#   {
#     'date':  '2020-11',
#     'event': 'name5'
#   },
#   {
#     'date':  '2020-11',
#     'event': 'name6'
#   },
#   {
#     'date':  '2020-12',
#     'event': 'name7'
#   },
#   {
#     'date':  '2020-12',
#     'event': 'name8'
#   },
#   {
#     'date':  '2020-12',
#     'event': 'name9'
#   },
# ]
# MyBox = {}
# for event in events:
#     date = event['date']
#     event_n = event['event']
#     if date not in MyBox:
#         MyBox[date] = [event_n]
#     else:
#         MyBox[date].append(event_n)
#     for x in MyBox:
#         print(x, MyBox[x])
# print(MyBox)
10
# a = [1,2,3,4,5,6,7,8,9,10]
# b = filter(lambda num: num % 2 == 0, a)
# print(list(b))
11
# lst = ['abcd', 'ab', 'cd', 'de', 'bc']
# b = filter(lambda num: len(num) == 2, lst)
# print(list(b))
# aaa = ['aab','aas','dq','df','re','wqeq']
# b = filter(lambda num: len(num) == 2, aaa)
# print(list(b))
# for i in aaa:
#     if len(i) == 2:
#         print(i)
12
# a = 5
# def name():
#     a = 3
#     return a
# print(name())
13
# num = 4
# def func():
#     global num
#     num *= 2 
#     return num 
# print(func())
14
# num = 10
# def func():
#     global num
#     num -= 3
#     return num
# print(func())
15
import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
