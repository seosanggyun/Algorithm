import sys
sys.stdin = open('input.txt')

T = int(input())
# T 만큼 반복해서 로직을 수행해서
# 3개의 tc에 대한 답안 각각 출력
for tc in range(1, T+1):
    # 전체 개수
    N = int(input())
    # 각 건물당 높이를 리스트로
    numbers = list(map(int, input().split()))

    # 최종 결과값
    result = 0

    # 모든 상황에 대한 낙찻값 구하기 위한 순회
    for i in range(N):
        # i 번째의 최대 낙차 값은
        # 전체 길이 - 내 현재 위치 +1
        max_height = len(numbers) - (i+1)

        # i 번째 부터 끝까지 반복해서 더 큰값 찾기
        for j in range(i+1, len(numbers)):
            # i보다 큰 j 찾기
            # 찾으면 최대 낙차 -1
            if numbers[i] <= numbers[j]:
                max_height -= 1

        # 최종 최대 낙차 값을 도출
        if result < max_height:
            result = max_height
    print(f'#{tc} {result}')