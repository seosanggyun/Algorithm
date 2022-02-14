import sys

sys.stdin = open('sol1.txt')

# 입력 받은 값이 홀수면 True
# 짝수면 False 출력
'''
 입력 값이 1이라면
 # True 출력
'''
N = int(input())
result = True if N%2 else False

print(f'# {result}')