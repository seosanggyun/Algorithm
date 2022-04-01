import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    result = -1
    # N이 1일때를 위해 N+1
    for i in range(1, N+1):
        if i**3 == N:
            result = i
            break
        if i**3 > N:
            break
    print(f'#{tc} {result}')
