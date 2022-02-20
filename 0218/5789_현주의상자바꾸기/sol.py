import sys; sys.stdin=open('sample_input.txt')

T = int(input())

for tc in range(T):
    N, Q = map(int, input().split())
    arr = [0 for _ in range(N)]
    for i in range(Q):
        li, ri = map(int, input().split())
        for j in range(li - 1, ri):
            arr[j] = i+1
    result = arr
    print(f'#{tc+1}', end=' ')
    print(*arr)



