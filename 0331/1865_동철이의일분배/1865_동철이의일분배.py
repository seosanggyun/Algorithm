import sys

sys.stdin = open('input.txt')


def search(w, cnt):
    global result
    if cnt <= result:
        return
    if w == N:
        result = cnt
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            search(w + 1, cnt * arr[w][i])
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 모든 값들 %를 소수로 변환
    '''
    입력 받은 정수를 그대로 사용할 시,
    값을 곱할 수록 점점 값이 커져간다. -> 유망성 조사할 시점을 잡기 어렵다.
    확률은 곱할수록 값이 줄어든다. -> 20% * 20% = 4% | 0.2 * 0.2 = 0.04
    상황 A (직원 1, 2의 성공률) 가 상황 B (직원 1, 2, 3의 성공률) 보다 낮다면
    상황 A 에서 직원 3의 확률까지 곱해졌을 때 상황 B 보다 좋은 경우가 있을 수 없다.
    따라서 유망성 조사할 시점이 명확해 진다.
    그러므로 입력 받은 값들을 소수로 변환하여 계산한다.
    '''
    # arr = [list(map(lambda p: int(p)/100, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j] / 100

    visited = [0] * N
    result = 0
    search(0, 1)
    print(f'#{tc} {result * 100:6f}')