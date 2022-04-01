import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())

memo = [[0 for _ in range(11)] for _ in range(11)]
print(memo)
for i in range(10):
    for j in range(i + 1):
        if j == 0 or i == j:
            memo[i][j] = 1
        else:
            memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]
pprint(memo)
for tc in range(1, T + 1):
    N = int(input())
    N = 10
    print(f'#{tc}')
    for i in range(N):
        for j in range(i + 1):
            print(f'{memo[i][j]}', end=" ")
        print()