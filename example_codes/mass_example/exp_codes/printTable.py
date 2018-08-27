#!/usr/bin/env python3
# coding=utf-8

# 测试
tableData = [
    ['apple', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
    ]


def printTable(t_data):
    length = [0]*len(t_data)        # int length for store length of tableData
    for i in range(len(t_data)):
        length[i] = len(' '.join(t_data[i]))

    col_width = max(length)

    for i in range(len(t_data)):
        strings = ' '.join(t_data[i])       # itranslate list to string Separated by spaces
        print(strings.rjust(col_width))

printTable(tableData)