import sys;

sys.stdin = open('sample_input.txt')
from pprint import pprint

T = int(input())

# 오른쪽과 아래쪽으로만 움직일 수 있으므로
# 델타 설정
dx = [0, 1]
dy = [1, 0]


def dfs(x, y):
    global result, tmp
    # result에 담긴 최소값보다
    # 현재 값이 크다면 탐색 중지
    if result < tmp:
        return

    # 도착지점이 x == N-1, y == N-1 이므로
    # 도착지점에 도달하면 결과값에 tmp 값 할당
    if x == N - 1 and y == N - 1:
        result = tmp
        return

    # 다음 탐색지점 델타로 계산
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
            # visited[nx][ny] == 0이면
            # 방문한 적이 없는 좌표이므로
            # 방문해주면서 값 더해줌
            visited[nx][ny] = 1
            tmp += data[nx][ny]
            dfs(nx, ny)
            # 경로가 막혔을 경우
            # 뒤로 돌아가야 하기 때문에
            # tmp에 더해준 값을 빼고
            # 방문처리를 무효
            tmp -= data[nx][ny]
            visited[nx][ny] = 0


for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    result = 10 * N * N
    tmp = data[0][0]
    dfs(0, 0)
    print(f'#{tc} {result}')

# def dfs(x, y, tmp):
#     global result
#
#     if x == N-1 and y == N-1:
#
#         tmp += data[x][y]
#
#         if tmp < result:
#             result = tmp
#             return
#
#     if tmp > result:
#         return
#
#     for i in range(2):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if x > N-1 or y > N-1:
#             continue
#
#         if not visited[x][y]:
#
#             visited[x][y] = 1
#
#             dfs(nx, ny, tmp + data[x][y])
#
#             visited[x][y] = 0
#
# for tc in range(1, T+1):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]
#
#     result = N*N*10
#
#     visited = [[0 for _ in range(N)] for _ in range(N)]
#
#     dfs(0,0,0)
