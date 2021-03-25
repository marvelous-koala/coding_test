import sys
import numpy as np

def node_check(arr):
    lng = arr.shape[0]
    checks = []
    for col in range(1, lng):
        for ind in range(1, lng):
            if arr[col][ind] == 1:
                checks.append([col, ind])
    return checks

def line_checker(board, a, direction, size):
    ud, lr = a
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

def liner(board, a, direction, lines, size):
    ud, lr = a
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
    return ropes

def dfs(board, nodes, cores, nums, ropes):
    global g_cores, g_ropes
    if g_cores < cores:
        g_cores = cores
        g_ropes = ropes
        #print(board)
        #print(ropes)
        #print(cores)
    if g_ropes > ropes and g_cores == cores:
        g_ropes = ropes
    if len(nodes) == nums:
        return
    
    for di in directions:
        if line_checker(board, nodes[nums], di, sqrs) == False:
            continue
        rope = liner(board, nodes[nums], di, 2, sqrs)
        dfs(board, nodes, cores + 1, nums + 1, ropes + rope)
        liner(board, nodes[nums], di, 0, sqrs)


    dfs(board, nodes, cores, nums + 1, ropes)

sys.stdin = open("sample_input.txt", "r")
T = int(input())
# T = 1
cases = [[] for x in range(T)]
directions = ['up', 'down', 'left', 'right']
for k in range(T):
    sqrs = int(input())
    cont = [list(map(int, input().split())) for temp in range(sqrs)]
    cases[k].append(cont)
    a = cases[k]
    a = a[0]
    temp = np.array(a)
    nodes = node_check(temp)
    g_cores = 0
    g_ropes = 0
    cores = 0
    ropes = 0
    board = temp.copy()
    dfs(board, nodes, 0, 0, 0)
    print("#{0} {1}".format(k+1, g_ropes))

