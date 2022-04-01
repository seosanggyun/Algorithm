import sys;

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = A.sort()

