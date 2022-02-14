import sys

sys.stdin = open('input.txt')

# 테스트 케이스의 개수 10개
for tc in range(10):
    T = int(input())
    # 2차원 배열 받아줄건데
    # 한 행에 100개의 요소
    # 그리고 100개의 열
    arr = [list(map(int, input().split())) for a in range(100)]
    # 합들을 리스트에 담아두고 최댓값 출력해줄거니까
    # 합들을 저장할 리스트 초기화
    sum_list = []
    # 결과값 초기화
    result = 0

    # 1. 행 검색
    for i in range(100):
        # 행마다 합이 초기화 되어야 함
        hap = 0
        for j in range(100):
            hap += arr[i][j]
        sum_list.append(hap)

    # 2. 열 검색
    for i in range(100):
        # 열마다 합이 초기화 되어야 함
        hap = 0
        for j in range(100):
            hap += arr[j][i]
        sum_list.append(hap)

    # 3. 좌상우하 대각선
    for i in range(100):
        hap = 0
        for j in range(100):
            # 좌상우하 대각선은
            # i와 j의 값이 같은 경우임
            if i == j:
                hap += arr[i][j]
        sum_list.append(hap)

    # 4. 우상좌하 대각선
    for i in range(100):
        hap = 0
        for j in range(100):
            # 우상좌하 대각선은
            # i와 j의 합이 99일 경우임
            if i + j == 99:
                hap += arr[i][j]
        sum_list.append(hap)

    # 합들이 저장된 리스트에서 최댓값 찾기
    for i in sum_list:
        if i > result:
            result = i

    print(f'#{tc+1} {result}')


