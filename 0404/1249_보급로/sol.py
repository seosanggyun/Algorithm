import sys;
sys.stdin = open('input.txt')

def bfs(si,sj,ei,ej):
    Q = [] #1 [1] Q, visited 생성
    visited = [[100000] * N for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    Q.append((si,sj)) # [2] Q 초기데이터 삽입, visited 표시
    visited[si][sj] = arr[si][sj]

    while Q:
        ci,cj = Q.pop(0)

        # 4방향 / 8방향 / 숫자차이가 일정값 이하
        for i in range(4):
            ni, nj = ci + dx[i], cj + dy[i]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] > visited[ci][cj] + arr[ni][nj]:
                Q.append((ni,nj))
                visited[ni][nj] = visited[ci][cj] + arr[ni][nj]

    return visited[ei][ej]





T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    result = bfs(0,0,N-1,N-1)
    print(f'#{tc} {result}')