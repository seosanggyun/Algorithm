import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(nx, ny):
    if 0 <= nx < N and 0 <= ny < N:
        return True
    else:
        return False

def DFS(x, y, cnt, num):
    stack = []
    stack.append((x, y, cnt, num))

    while stack:
        x, y, cnt, num = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 벽체크, 다음 위치가 내 위치보다 1클때만
            # 다음 위치가 내 위치보다 1 클때만 이동할 것이므로
            # 별도의 방문처리 필요 없음
            if check(nx, ny) and arr[nx][ny] == arr[x][y]+1:
                # 현재까지의 각 방들의 합을 num에 할당
                num += arr[nx][ny]
                # 다음 위치 조사
                stack.append((nx, ny, cnt+1, num))
    return cnt, num



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 최종 결과 초기화
    # 출발 위치, 방문한 방의 개수, 각 방들의 숫자 합
    result = [0, 0, 0]

    # 전체 위치에서 조회
    for x in range(N):
        for y in range(N):
            cnt, num = DFS(x, y, 1, arr[x][y])
            # 방문한 방의 개수가 더 많다면
            if result[1] < cnt:
                # 최종 결과 변경
                result = [arr[x][y], cnt, num]
            # 방문한 개수가 같고, 각 방의 합이 현재 값보다 작을때만
            elif result[1] == cnt and result[2] > num:
                # 변경
                result = [arr[x][y], cnt, num]

    print(f'#{tc} {result[0]} {result[1]}')