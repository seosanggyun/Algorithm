import sys; sys.stdin = open('sample_input.txt')

T = int(input())

# 테스트 케이스 개수만큼 반복
for tc in range(T):
    # 2차원 배열 초기화
    arr = [[0] * 10 for _ in range(10)]
    # 색칠할 영역의 개수 입력
    N = int(input())
    # 색칠할 영역의 개수만큼 반복해서 색칠
    for n in range(N):
        # 입력값 입력
        x1, y1, x2, y2, c = map(int, input().split())
        # 해당 영역의 x축 범위만큼 반복
        for i in range(x1, x2+1):
            # 해당 영역의 y축 범위만큼 반복
            for j in range(y1, y2+1):
                # 같은 색은 칠하지 않으므로
                # 기존의 영역과 색이 같지 않을 때에만
                # 색을 더 해줌
                if arr[i][j] != c:
                    arr[i][j] += c
    # 보라색이 색칠된 영역
    # 빨간색 1 + 파란색 2 = 보라색 3
    # 즉 배열에서 3이 적힌 요소의 개수를 구해야 함
    # 카운트 초기화
    count = 0
    # 2차원 배열 탐색
    for k in arr:
        for l in k:
            # 3이 있다면 카운트 +1
            if l == 3:
                count += 1


    print(f'#{tc+1} {count}')