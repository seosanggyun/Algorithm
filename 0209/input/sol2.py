# 입력 받은 값이 홀수면 True
# 짝수면 False 출력
'''
 입력 값이 1이라면
 #1 True 출력
 #2 False
 #3 True
'''

import sys

sys.stdin = open('sol2.txt')

T = int(input()) # -> 10

for tc in range(1, T+1):
    N = int(input())
    result = True if N % 2 else False
    print(f'#{tc} {result}')
