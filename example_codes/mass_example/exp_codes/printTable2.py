#!/usr/bin/env python3
# coding=utf-8

tableData = [
    ['apple', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
    ]

def printTable(t_data):
    row = len(t_data)
    col = len(t_data[0])
    width = [0]*row     # 保存最大值
    length = [[0]*col]*row  # 保存每个值

    for i in range(row):
        for j in range(col):
            length[i][j] = len(t_data[i][j])
        # print(length[i])
        width[i] = max(length[i])
        # print(width[i])

    for i in range(col):
        for j in range(row):
            print(t_data[j][i].rjust(width[j]), end = '\t')
            # print(t_data[j][i], end = '\t')
        print('\n')

printTable(tableData)