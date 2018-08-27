#!/usr/bin/python
#coding=utf-8

import pprint

theBoard = {
    'top-l':'', 'top-m':'', 'top-r':'',
    'mid-l':'', 'mid-m':'', 'mid-r':'',
    'low-l':'', 'low-m':'', 'low-r':''
    }


def printBoard(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print("-+-+-")
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print("-+-+-")
    print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])
    print("-+-+-")


#printBoard(theBoard)
print("input something like:")
pprint.pprint(theBoard)

turn = 'X'

for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input('提示：iniput something like top-l、mid-m、low-r')
    theBoard[move] = turn

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)
