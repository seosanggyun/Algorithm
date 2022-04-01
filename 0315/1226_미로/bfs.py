import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    Q = []
    Q.append((x, y))
    # 현재 좌표 벽으로 변경
    visited[x][y] = 1
    while Q:
        # FIFO를 위해 pop(0)
        x, y = Q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 16 > nx >= 0 and 16 > ny >= 0 and data[nx][ny] != 1 and not visited[nx][ny]:
                if data[nx][ny] == 3:
                    visited[nx][ny] = 3
                    return 1
                Q.append((nx, ny))
                # 이전에 방문한 값 + 1 == 이동한 거리
                visited[nx][ny] = visited[x][y] + 1
    return 0

for tc in range(1, 11):
    T = int(input())
    data = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if data[i][j] == 2:
                result = BFS(i, j)
                break
    print(f'#{tc} {result}')
