import sys;
from collections import deque
sys.stdin = open('sample_input.txt')

'''
연산 : +1, -1, *2, -10
Q에 연산결과와 count를 함께 넣어서 체크
'''

# 같은 숫자가 계속해서 나오는 반복상황을 막기 위해
# visited 배열 사용 (100만개짜리)
# ex) 1 + 1 = 2, 2 - 1 = 1 무한반복


def calc():
    global result
    while Q:
        number, count = Q.popleft()
        if number == M:
            result = count
            return
        for i in range(4):
            if i == 0:              # 첫번째 경우 +1
                if 1 <= number + 1 <= 1000000 and visited[number+1] == 0:
                    Q.append((number+1, count+1))
                    visited[number+1] = 1
            elif i == 1:            # 두번째 경우 -1
                if 1 <= number - 1 <= 1000000 and visited[number-1] == 0:
                    Q.append((number-1, count+1))
                    visited[number-1] = 1
            elif i == 2:            # 세번째 경우 *2
                if 1 <= number * 2 <= 1000000 and visited[number*2] == 0:
                    Q.append((number*2, count+1))
                    visited[number*2] = 1
            elif i == 3:            # 네번째 경우 -10
                if 1 <= number - 10 <= 1000000 and visited[number-10] == 0:
                    Q.append((number-10, count+1))
                    visited[number-10] = 1


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = 0
    visited = [0 for _ in range(1000001)]
    Q = deque()
    Q.append((N,0))
    calc()

    print(f'#{tc} {result}')