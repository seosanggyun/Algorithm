import sys

sys.stdin = open('input.txt')

def Bubblesort(a, n):
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

for tc in range(10):
    dump = int(input())
    height = list(map(int, input().split()))
    Bubblesort(height, 100)
    count = 0
    while count != dump:
        height[0] += 1
        height[-1] -= 1
        count += 1
        Bubblesort(height, 100)
    max = height[-1]
    min = height[0]
    print(f'#{tc+1} {max - min}')

