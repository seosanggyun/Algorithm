import sys
sys.stdin = open('input.txt')

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y, cnt):
    Q = [(x, y, cnt)]
    while Q:
        x, y, cnt = Q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if maze[nx][ny] == 0:
                    maze[x][y] = 1
                    Q.append((nx, ny, cnt+1))
                if maze[nx][ny] == 3:
                    return cnt
    return 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    result = 0
    # 0 길, 1 벽, 2s, 3e
    for x in range(N):
        for y in range(N):
            if maze[x][y] == 2:
                result = BFS(x, y, 0)
    print(f'#{tc} {result}')
