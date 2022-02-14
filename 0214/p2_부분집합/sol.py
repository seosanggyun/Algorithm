import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    arr = list(map(int, input().split()))
