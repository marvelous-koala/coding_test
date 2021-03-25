import sys
import numpy as np

sys.stdin = open("climb.txt", "r")
T = int(input())
vector = [[1,0], [-1,0], [0,1], [0,-1]]


for k in range(T):
    temp = input().split()
    size = int(temp[0])
    depth = int(temp[1])
    board = [list(map(int, input().split())) for temp in range(size)]
    high, peaks = peak_check(board)
    farest = 1
    for i in range(len(peaks)):
        stack = [peaks[i], 0, 0, high]        
        dfs(stack)
    print(farest)


def peak_check(board):
    peaks = []
    pk = -1
    for k in range(size):
        for j in range(size):
            a = board[k][j]
            if a > pk:
                peaks = []
                peaks.append([k,j])
                pk = a
            elif a == pk:
                peaks.append([k,j])
    return pk, peaks



def dfs(stack):
    start, line, dig, high = stack
    x, y = start
    global depth, farest
    if line > farest:
        farest = line
    for v in vector:
        a, b = v 
        if x + a < 0 or y + b < 0 or x + a == size or y + b == size:
            continue               
        next_high = board[a+x][b+y]

        if next_high >= high and dig == 1:
            continue

        elif next_high - depth < high and dig == 0:
            stack = [[x+a, y+b], line + 1, 1, high - 1]
            dfs(stack)

        elif next_high < high:
            stack = [[x+a, y+b], line + 1, 0, board[x + a][y + b]]
            dfs(stack)
    return


print("Hellow world")