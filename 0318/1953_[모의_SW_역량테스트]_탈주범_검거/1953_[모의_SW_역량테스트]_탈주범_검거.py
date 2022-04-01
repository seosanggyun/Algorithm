import sys
sys.stdin = open('input.txt')

# 터널 정보
turner = [
    [], # 0은 없음
    [(-1, 0), (1, 0), (0, -1), (0, 1)], # 1은 상하좌우
    [(-1, 0), (1, 0)],      # 상하
    [(0, -1), (0, 1)],      # 좌우
    [(-1, 0), (0, 1)],      # 상우
    [(1, 0), (0, 1)],       # 하우
    [(0, -1), (1, 0)],      # 좌하
    [(-1, 0), (0, -1)],     # 상좌
]

# 현재 나아가는 방향과
# 다음 위치 터널이 이어져 있는지 확인
def check(i, x, y, nx, ny):
    # 현재 터널 정보
    l = arr[x][y]
    # 다음 위치 터널 정보
    nl = arr[nx][ny]
    # 다음 위치 터널 정보 중
    for j in range(len(turner[nl])):
        # 현재 터널이 위로 향할때 각 값은 -1, 0
        # 다음 터널이 아래로 향할때 각 값은 1, 0
        # 각 좌표 값의 합이 모두 0 == 이어져 있음
        if turner[l][i][0] + turner[nl][j][0] == 0 and turner[l][i][1] + turner[nl][j][1] == 0:
            return True
    else:
        return False



def BFS(x, y, cnt):
    global result
    # 방문표시
    visited = [[0]*M for _ in range(N)]
    visited[x][y] = 1

    Q = []
    Q.append((x, y, cnt))

    while Q:
        x, y, cnt = Q.pop(0)
        if cnt == L:
            return
        # 현재 위치의 터널 정보
        t = arr[x][y]
        # 해당 터널 정보가 가진 이동 가능 방향
        for i in range(len(turner[t])):
            # 각 방향 좌표 설정
            nx = x + turner[t][i][0]
            ny = y + turner[t][i][1]

            # 범위 체크, 방문 체크
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                # 벽 체크, 터널 이어짐 체크
                if arr[nx][ny] and check(i, x, y, nx, ny):
                    # 방문 표시
                    visited[nx][ny] = 1
                    # 탈출범이 있을 수 있는 위치 + 1
                    result += 1
                    # 다음 위치 조사, 시간 증가
                    Q.append((nx, ny, cnt+1))

T = int(input())

for tc in range(1, T+1):
    # x, y, 시작 x, 시작 y, 소요시간
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 탈출범이 위치할 수 있는 장소의 수
    result = 1
    # 세로, 가로, 탈출시간
    BFS(R, C, 1)
    print(f'#{tc} {result}')