#/usr/bin/env python3
grid = [
    ['.', '.', '.', '.', '.', '.'],
    
['.', '0', '0', '.', '.', '.'],
    ['0', '0', '0', '0', '.', '.'],
    ['0', '0', '0', '0', '0', '.'],
    ['.', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '.'],
    ['0', '0', '0', '0', '.', '.'],
    ['.', '0', '0', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ]

def grid_print(list_print):
    row_num = len(list_print)
    col_num = len(list_print[0])

    print("========START OF PRINT========")
    for i in range(row_num):
        for j in range(col_num):
            print(list_print[i][j], end=" ")
        print("\n")
    print("========END OF PRINT========")

def grid_rotate(list_rotate):
    row_num = len(list_rotate)    #9
    col_num = len(list_rotate[0])    #6

    print("========START OF PRINT========")
    for i in range(col_num):
        for j in range(row_num):
            print(list_rotate[j][i], end=" ")
        print("\n")
    print("========END OF PRINT========")

grid_print(grid)
grid_rotate(grid)
