import sys; sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr1 = [[0] * N for _ in range(N)]
    arr2 = [[0] * N for _ in range(N)]
    arr3 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr1[i][j] = arr[N-1-j][i]
            arr2[i][j] = arr[N-1-i][N-1-j]
            arr3[i][j] = arr[j][N-1-i]
    print(f'#{tc}')
    for a1, a2, a3 in zip(arr1, arr2, arr3):
        print(f'{"".join(map(str, a1))} {"".join(map(str, a2))} {"".join(map(str, a3))}')