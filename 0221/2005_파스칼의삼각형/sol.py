import sys; sys.stdin = open('input.txt')

T = int(input())

# N*N개의 행렬을 0으로 다 채운 뒤
# arr[0][0] 에 1을 할당
# 이러면 안되네
# 모든 행의 0번째 열의 값은 1임

for tc in range(1, T+1):
    N = int(input())
    # N*N개의 행렬을 0으로 채움
    arr = [[0] * N for _ in range(N)]
    # 모든 행의 0번째 열의 값을 1로 채움
    for i in range(N):
        arr[i][0] = 1
    # a[0][0]이 아닐 때만
    # a[i][j]는 왼쪽 대각선 위의 요소 + 위의 요소
    for i in range(N):
        for j in range(i+1):
            if i != 0 and j != 0:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    # 어떻게 출력하지
    # print(arr)
    # 뭐 뭐 어떻게 하다보니 됐다
    print(f'#{tc}')
    for i in range(N):
        for j in range(i+1):
            print(arr[i][j], end=' ')
        print()




