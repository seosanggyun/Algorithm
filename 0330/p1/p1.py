import sys
sys.stdin = open('input.txt')


def quick_sort(a, left, right):
    if left < right:
        mid = partition(a, left, right)
        quick_sort(a, left, mid - 1)
        quick_sort(a, mid + 1, right)


def partition(a, left, right):
    # 피봇보다 큰  구간 왼쪽 경계
    i = left - 1
    # 피봇 보다 큰 구간 오른쪽 경계
    j = left
    # 가장 오른 쪽 원소를 피봇으로 결정
    pivot = a[right]
    # 피벗에 다다르기 전까지 (pivot) j 를 변경
    while j < right:
        if pivot > a[j]:
            # 피봇보다 작으면 i 이동
            i += 1
            # i와 j가 다르면 피봇보다 큰 구간 존재
            if i < j:
                # 교환
                a[i], a[j] = a[j], a[i]
        j += 1
    # 피벗과 교환
    a[i + 1], a[right] = pivot, a[i + 1]
    return i + 1

for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    quick_sort(A, 0, N - 1)
    for i in A:
        print(i, end=' ')
    print()