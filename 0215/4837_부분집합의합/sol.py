import sys; sys.stdin = open('sample_input.txt')

T = int(input())
arr = list(range(1, 13))
n = len(arr)
for tc in range(T):
    gaesu, hap = map(int, input().split())
    bubuns = []
    for i in range(1 << n):
        bubun = []
        for j in range(n):
            if i & (1 << j):
                bubun.append(arr[j])
        bubuns += [bubun]
    count = 0
    for k in bubuns:
        sum = 0
        for l in k:
            sum += l
        if len(k) == gaesu and sum == hap:
            count += 1

    print(f'#{tc+1} {count}')
