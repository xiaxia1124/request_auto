import csv
import glob
import io
import json
import os.path
import re
from collections import defaultdict, OrderedDict, Counter, namedtuple
from datetime import datetime
from fnmatch import fnmatch
from operator import itemgetter

from queue import PriorityQueue

import heapq
import pathlib

#
# class User():
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, n):
#         self._age = n + 5
#
#
# user = User('xiao', 1)
# user.age = 5
# print(user.age)

'''
heap模块可快速获取到列表的最大或者最小的n个数字
'''
# nums = [1,23,4,56,-1,789]
# print(heapq.nlargest(1, nums))
# print(heapq.nsmallest(2, nums))
#
# heapq.heapify(nums)
# print(nums)
# print(heapq.heappop(nums))
#
# q=PriorityQueue()




'''
字典中的键映射多个值
'''
# d = defaultdict(list)
# d['key'].append('value1')
# d['key'].append('value2')
# print(d)
#
# d2 = defaultdict(set)
# d2['key'].add('set1')
# d2['key'].add('set2')
# print(d2)

'''
字典排序
'''
# d = OrderedDict()
# d['a'] = 2
# d['b'] = 4
# d['c'] = 1
# d['d'] = 5
# # for key in d:
# #     print(key, d[key])
# # print(d['a'])
# json.dumps(d)
# for key in d:
#     print(key, d[key])
'''
怎样在数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）
'''
# my_dict = {'a': 3, 'b': 2, 'c': 1}
# print(my_dict.items())
#
# min_value = min(zip(my_dict.values(), my_dict.keys()))
# max_value = max(zip(my_dict.values(), my_dict.keys()))
# min_value1 = min(my_dict.items(), key=lambda item: item[1])
# max_value1 = max(my_dict.items(), key=lambda item: item[1])
# sorted_dict1 = dict(sorted(my_dict.items(), key=lambda item: item[1]))
#
# print(min_value)
# print(min_value1)
# print(max_value1)
# print(sorted_dict1)
'''
切片
'''
# record = '....................100 .......513.25 ..........'
# SHARES = slice(20, 23)
# PRICE = slice(31, 37)
# cost = int(record[SHARES]) * float(record[PRICE])
# print(cost)
'''
序列中出现次数最多的元素
'''
# words = [
#     'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
#     'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
#     'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
#     'my', 'eyes', "you're", 'under'
# ]
# word_counts = Counter(words)
# print(word_counts)
# print(word_counts['look'])
# print(word_counts.most_common(1))

'''
通过某个关键字排序一个字典列表,itemgetter()也同样适用于 min() 和 max() 等函数
'''
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
# rows_by_name = sorted(rows, key=itemgetter('fname', 'lname'))
# print(rows_by_name)
# rows_by_uid = sorted(rows, key=itemgetter('uid'))
# print(rows_by_uid)
# rows_by_name2 = sorted(rows, key=lambda r: (r['fname'], r['lname']))
# print(rows_by_name2)
# rows_max = max(rows, key=itemgetter('fname'))
# print(rows_max)

'''
过滤序列元素
'''
# mylist = [1, 4, -5, 10, -7, 2, 3, -1]
# filter_list = [n for n in mylist if n >0]
# filter_list.sort()
# print(filter_list)
#
# values = ['1', '2', '-3', '-', '4', 'N/A', '5']
# def is_int(val):
#     try:
#         int(val)
#         return True
#     except ValueError:
#         return False
# intvals = list(filter(is_int, values))
# print(intvals)
#
# [n if n > 0 else 0 for n in mylist]

'''
从字典中提取子集
'''
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
p1 = dict((key, value) for key, value in prices.items() if value > 200)
print(p1)

'''
映射名称到序列元素
'''
# from collections import namedtuple
# Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
# sub = Subscriber('test@xx.com', '2021-03-12')
# print(sub)
# print(sub.addr)

# nums = [1, 2, 3, 4, 5]
# s = sum(x * x for x in nums)
# print(s)

'''
合并多个字典或映射
'''
# a = {'x': 1, 'z': 3}
# b = {'y': 2, 'z': 4}
# from collections import ChainMap
# c = ChainMap(a, b)
'''
如果出现重复键，会返回第一次出现的映射值
'''
# print(c['z'])
#
# text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
# m = datepat.match('11/27/2012')
#
# re.IGNORECASE

'''
删除字符中不需要的字符
'''
filename = "E:\error2.txt"
# with open(filename, 'rt') as f:
#     # readlines()会创建一个临时的列表
#     for line in f.readlines():
#         print(line)
#         print(line.strip())
#     # 但是下面这种不需要预先读取所有数据放到一个临时的列表中去，它仅仅只是创建一个生成器，并且每次返回行之前会先执行 strip 操作。
#     lines = (line.strip() for line in f)
#     for line in lines:
#         print(line)
#
# with open(filename, 'rt', newline='') as f:
#     print(f.read())
'''
打印输出至文件中
'''
# with open(filename, 'wt') as f:
#     print('hello world', file=f)

'''
io流输入
'''
# s = io.StringIO()
# s.write('Hello World\n')
# print('Add', file=s)
# print(s.getvalue())
'''
'''
# json_str = '{"name": "John", "age": 30, "city": "New York"}'
# data = json.loads(json_str)
# print(data['name'])
# json1 = json.dumps(data)
#
# my_list = [1, 2, 3, 4, 5]
# filtered_list = list(filter(lambda x: x % 2 == 0, my_list))
# print(list(filtered_list))  # Output: [2, 4]

# time = datetime.now()
# text = '2023-04-18'
# y = datetime.strptime(text, '%Y-%m-%d')
# print(y)

'''
读取csv文件
'''
# with open('stocks.csv') as f:
#     f_csv = csv.reader(f)
#     header = next(f_csv)
#     print(header)
#     Row = namedtuple('Row', header)
#     for r in f_csv:
#         row = Row(*r)
#         print(row)
'''
往csv文件写入数据
'''
# headers = ['Symbol','Price','Date','Time','Change','Volume']
# rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
#          ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
#          ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
#        ]
# with open('stocks.csv', 'w') as f:
#     f_csv = csv.writer(f)
#     f_csv.writerow(headers)
#     f_csv.writerows(rows)
'''
文件路径 操作
'''
# path = "E:\杂七杂八文件\stocks.csv"
# # 获取路径中的文件名
# fileName = os.path.basename(path)
# print(fileName)
# # 获取路径中的文件路径
# dir = os.path.dirname(path)
# print(dir)
# # 将文件中添加新的路径
# newPath = os.path.join('test','data', os.path.basename(path))
# print(newPath)
#
# path = '~stocks.csv'
# dir = os.path.expanduser(path)
# print(dir)
# # 拆分文件名和文件后缀
# print(os.path.splitext(path))
#
# print(os.path.abspath(path))

'''
获取文件夹下的文件/文件夹列表
'''
# names = [name for name in os.listdir('E:\\xxia1') if os.path.isfile(os.path.join('E:\\xxia1', name))]
# print(names)
# files = [file for file in os.listdir('E:\\xxia1') if os.path.isdir(os.path.join('E:\\xxia1', file))]
# print(files)
# dbName = [name for name in os.listdir('E:\\xxia1') if name.endswith(".db")]
# print(dbName)
# xlsxName = [name for name in os.listdir('E:\\xxia1') if fnmatch(name, '账号*.xlsx')]
# print(xlsxName)
# print(glob.glob('*.py'))


import os

# 指定文件夹路径和文件名
# dir_path = 'D:/leqee/auto-robot-core/test/test_project/robot_source/resources'
# file_name = 'error.txt'

# 判断文件是否存在
# file_path = os.path.join(dir_path, file_name)
# print(file_path)
# if os.path.exists(file_path):
#     print(f'{file_name} exists in {dir_path} folder')
# else:
#     print(f'{file_name} does not exist in {dir_path} folder')
#
# sheet_list=['Sheet1', 'Sheet2', 'Sheet3', 'Sheet4', 'Sheet5', 'Sheet6', 'Sheet7', 'Sheet8', 'Sheet9', 'Sheet10', 'Sheet11', 'Sheet12', 'Sheet13', 'Sheet14']
# str1 = ','.join(sheet_list[1:])
# print(str1)
# # print(f"{sheet_list[0]},{sheet_list[1]}")
#
#
#
# def test_username(parametrized_username):
#     assert parametrized_username in ['one', 'two', 'three']
#
#
# def test_username(non_parametrized_username):
#     assert non_parametrized_username == 'username'

# import pytest
#
# @pytest.fixture(scope="module", autouse=True)
# def monitor_init1():
#     print("可以用这行代替之前框架的setUp")
#     a = 1
#     yield a
#     print("可以用这行代替之前框架的tearDown")
#
# @pytest.fixture()
# def one(two):
#     print("执行用例A")
#
# @pytest.fixture()
# def two():
#     print(1)
#
# def test_two(one):
#     print("执行用例B")

# path = os.path.abspath("test.py")
# print(path)
#
# print(os.path.basename(path))
#
# print(os.path.dirname(path))
#
# print(os.path.exists(path))
#
# print(os.path.split(path))  #返回元祖
#
# dic = {"paging": {"limit": 15, "offset": 0, "totalCount": 139, "totalPage": 10, "pageNum": 1, "pageSize": 15}}
# json_content = json.dumps(dic)
# print(type(json_content))
# print(type(json.loads(json_content)))
# a = "test name"
# print(a.capitalize())
# print(a.startswith("e1"))
# print(a.join("hello"))
# print(a.replace("n", "x"))
a = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(a)
file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config/fc_api.yaml')
print(file_path)

b = os.path.realpath(__file__)
c = __file__
print(b)
print(c)