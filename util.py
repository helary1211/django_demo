# _*_ encoding:utf-8 _*_
# @Time : 2020/8/18 18:27
# @Author : chenmeihuan
# @File : util.py
# @Software: PyCharm
import csv
with open('data.csv') as f:
    for i in csv.reader(f):
        print(i)
