import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    # 최종 결괏값 초기화 : 가능한 가장 큰 수
    result = sum(arr) - B

    # 모든 경우의 수 (공집합 제외)
    for i in range(1, 1<<N):
        tmp = 0
        for j in range(N):
            # 각 부분 집합
            if i & (1<<j):
                tmp += arr[j]
        # 점원 키의 합이 선반보다 큰 경우
        if tmp >= B:
            # 초기 설정값보다 작은 경우
            if tmp - B < result:
                # 결과 변경
                result = tmp - B
    print(f'#{tc} {result}')
