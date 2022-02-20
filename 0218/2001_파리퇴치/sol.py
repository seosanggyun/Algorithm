import sys; sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_flies = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            result = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    result += arr[k][l]
            if max_flies < result:
                max_flies = result

    print(f'#{tc} {max_flies}')


