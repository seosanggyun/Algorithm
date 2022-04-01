import sys
sys.stdin = open('input.txt')


# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(x, y):
    if x < 0 or x > N - 1 or y < 0 or y > N - 1:
        return False
    return True

def maze(x, y):
    # queue 초기화
    Q = []
    Q.append((x, y))
    # 현재 좌표 벽으로 변경
    visited[x][y] = 1
    while Q:
        # FIFO를 위해 pop(0)
        x, y = Q.pop(0)

        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 벽 체크
            if check(nx, ny):
                # 새로 부여한 좌표값이 통로이고, 방문한적 없으면
                if data[nx][ny] == 0 and visited[nx][ny] == 0:
                    # 작업 목록에 추가
                    Q.append((nx, ny))
                    # 이전에 방문한 값 + 1 == 이동한 거리
                    visited[nx][ny] = visited[x][y] + 1
                # 만약 도착지점을 만나면
                elif data[nx][ny] == 3:
                    visited[nx][ny] = visited[x][y] + 1
                    # 출발 - 도착 사이의 칸 수를 원하므로
                    # 시작점, 도착점의 2값을 빼준다.
                    return visited[nx][ny] -2
    # 모든 작업을 완수 했지만, 도착하지 못했다면 0을 반환
    return 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 0은 통로, 1은 벽, 2는 출발, 3은 도착
    data = [list(map(int, input())) for _ in range(N)]
    # 방문 정보
    visited = [[0]*N for _ in range(N)]

    # 출발 점 찾기
    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                x, y = i, j

    print(f'#{tc} {maze(x, y)}')