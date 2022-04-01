import sys; sys.stdin = open('기지국_in.txt')
from pprint import pprint

# 상 하 좌 우
dx = [-1, 1, 0, 0, -2, 2, 0, 0, -3, 3, 0, 0]
dy = [0, 0, -1, 1, 0, 0, -2, 2, 0, 0, -3, 3]


for tc in range(2):
    count = 0
    n = int(input())
    arr = [list(input()) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(n):
            if arr[i][j] == 'A':
                for d in range(4):
                    x = i
                    y = j
                    x += dx[d]
                    y += dy[d]
                    if arr[x][y] == 'H':
                        arr[x][y] = 'O'

            elif arr[i][j] == 'B':
                for d in range(8):
                    x = i
                    y = j
                    x += dx[d]
                    y += dy[d]
                    if arr[x][y] == 'H':
                        arr[x][y] = 'O'

            elif arr[i][j] == 'C':
                for d in range(12):
                    x = i
                    y = j
                    x += dx[d]
                    y += dy[d]
                    if arr[x][y] == 'H':
                        arr[x][y] = 'O'
    for ans in arr:
        count += ans.count('H')
    pprint(arr)
    print(count)
