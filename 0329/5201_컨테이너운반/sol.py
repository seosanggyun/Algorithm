import sys;

sys.stdin = open('sample_input.txt')
from pprint import pprint

T = int(input())

for tc in range(1, T + 1):

    # 데이터 입력
    N, M = map(int, input().split())

    # 리스트로 입력받음
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))

    # 리스트를 내림차순으로 정렬
    wi.sort(reverse=True)
    ti.sort(reverse=True)
    print(wi)
    print(ti)

    # 결과값 초기화
    result = 0

    # wi와 ti에 요소가 있을동안 반복
    while wi and ti:
        # ti의 0번째 요소가 wi의 0번째 요소보다
        # 크거나 같을 경우
        # 즉 트럭이 화물을 운반할 수 있는 경우
        if ti[0] >= wi[0]:
            # result에 wi의 첫번째 요소를 pop해서 합산
            result += wi.pop(0)
            # ti의 첫번째 요소 pop
            ti.pop(0)
        # 그 외의 경우, 즉 화물이 너무 무거워서
        # 트럭이 옮길 수 없는 경우
        else:
            # wi의 0번재 요소 pop
            wi.pop(0)

    print(f'#{tc} {result}')