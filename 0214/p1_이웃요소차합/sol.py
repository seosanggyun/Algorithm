import sys

sys.stdin = open('input.txt')

# 델타검색 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 이웃한 요소와의 차(절대값)들의 합 구하는 함수 정의
def neighbor(x, y, N):
    cha_hap = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            cha_hap += abs(arr[nx][ny] - arr[x][y])
    return cha_hap

# 테스트케이스 입력
T = int(input())

# 테스트 케이스의 수 만큼 반복
for tc in range(T):
    # 행의 개수 입력
    hang = int(input())
    # 2차원 배열 입력받음
    arr = [list(map(int, input().split())) for a in range(hang)]
    result = 0
    for i in range(hang):
        for j in range(hang):
            result += neighbor(i, j, hang)

    print(f'#{tc+1} {result}')