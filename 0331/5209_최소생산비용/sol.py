import sys;
import itertools
from pprint import pprint

sys.stdin = open('sample_input.txt')

# 순열로 풀면 안된다
# 무한반복 돔 순열 경우의수가 너무 커져서

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     result = 99 * N * N
#     factory_number = []
#     expense = [list(map(int, input().split())) for _ in range(N)]
#     pprint(expense)
#     for i in range(N):
#         factory_number += [str(i)]
#     pprint(factory_number)
#     factory_orders = itertools.permutations(factory_number)
#     factory_orders = list(factory_orders)
#     pprint(factory_orders)
#
#     for order in factory_orders:
#         tmp = 0
#         for i in range(N):
#             tmp += expense[i][int(order[i])]
#             if tmp >= result:
#                 break
#         if tmp < result:
#             result = tmp
#         print(result)

# n : 현재 들어간 깊이  k : 합
def gongjang(n, k):
    global result
    # 만약에 현재 더한 합이 result보다 크면 가지치기
    if k >= result:
        return
    # 작은데 n == N이면 result 갱신 후 return
    elif n == N:
        result = k
        return
    # 둘 다 아니라면 재귀 들어감
    else:
        # N가지 경우의 수를 다 돌아야 함
        for i in range(N):
            # 만약에 check이 0이라면 방문 안했기 때문에 방문
            if check[i] == 0:
                check[i] = 1
                # 체크 한 후 재귀 들어감, 합에 product[제품(1, 2, 3)][깊이(각 공장)]을 더해줌
                gongjang(n+1, k + expense[i][n])
                # 재귀에서 나오면 check 초기화
                check[i] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = 99 * N * N
    check = [0 for _ in range(N)]
    expense = [list(map(int, input().split())) for _ in range(N)]
    gongjang(0,0)




    print(f'#{tc} {result}')
