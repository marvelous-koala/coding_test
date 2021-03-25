import sys
import numpy as np
import copy

def node_check(arr, sqrs):
    checks = []
    for i in range(1, sqrs):
        for j in range(1, sqrs):
            if arr[i][j] == 1:
                checks.append([i, j])
    return checks

def line_checker(board, node, direction, size):
    ud, lr = node
    ropes = 0
    if direction == 'up':
        t = 0
        while t < ud:
            if board[t][lr] != 0:
                return False
            t += 1
    elif direction == 'down':
        t = size - 1
        while t > ud:
            if board[t][lr] != 0:
                return False
            t -= 1
    elif direction == 'left':
        t = 0
        while t < lr:
            if board[ud][t] != 0:
                return False
            t += 1
    else:
        t = size - 1
        while t > lr:
            if board[ud][t] != 0:
                return False
            t -= 1
    return True

def liner(brd, node, direction, lines, size):
    board = brd[:]
    ud, lr = node
    ropes = 0
    if direction == 'up':
        t = 0
        while t < ud:
            board[t][lr] = lines
            t += 1
            ropes += 1
    elif direction == 'down':
        t = size - 1
        while t > ud:
            board[t][lr] = lines
            t -= 1
            ropes += 1
    elif direction == 'left':
        t = 0
        while t < lr:
            board[ud][t] = lines
            t += 1
            ropes += 1
    else:
        t = size - 1
        while t > lr:
            board[ud][t] = lines
            t -= 1
            ropes += 1
    return board, ropes

def dfs(stack):
    global answer, nodes, sqrs
    while stack:
        brd, core, ropes, idx = stack.pop()
        if (answer[0] < core) or (answer[0] == core and answer[1] > ropes):
            answer[0] = core
            answer[1] = ropes

        if (len(nodes) == idx) or (len(nodes) - idx < answer[0] - core):
            continue
        for di in directions:
            if line_checker(brd, nodes[idx], di, sqrs) == True:
                new_board, rope = liner(brd, nodes[idx], di, 2, sqrs)
                stack.append([new_board, core + 1, ropes + rope, idx + 1])
            else:
                stack.append([brd, core, ropes, idx + 1])
    

sys.stdin = open("sample_input.txt", "r")
T = int(input())
directions = ['up', 'down', 'left', 'right']

for k in range(T):
    sqrs = int(input())
    board = [list(map(int, input().split())) for temp in range(sqrs)]
    answer = [0,0]
    stack = []
    cores, ropes, idx = 0, 0, 0
    stack.append([board, cores, ropes, idx])
    nodes = node_check(board, sqrs)
    dfs(stack)
    print("#", k+1, " ", answer[1])
temp
board



stack = []
cores, ropes, idx = 0, 0, 0
stack.append([board, cores, ropes, idx])

nodes = node_check(board, sqrs)
answer = [0,0]
dfs(stack)

answer