import sys

sys.stdin = open('input.txt')

# 버스는 0번에서 출발해 종점인 N번 정류장까지 이동
# 한번 충전으로 이동할 수 있는 정류장 수 K
# 충전기가 설치된 M개의 정류장 번호


T = int(input())

# for tc in range(T):
#     K, N, M = map(int, input().split())
#     charger = list(map(int, input().split()))
#     busstop = [0]*N
#     count = 0
#     for i in charger:
#         busstop[i] += 1
#     del(busstop[0])
#
#     busstop_list = []
#     for j in range(((N-1)//K+1)):
#         busstop_part = []
#         for k in range(K):
#             busstop_part += [busstop[K*j+k]]
#         busstop_list += [busstop_part]
#
#     for k in busstop_list:
#         if 1 in k:
#             count += 1
#         elif 1 not in k:
#             count = 0
#             break

for tc in range(T):
    K, N, M = map(int, input().split())
    charger = list(map(int, input().split()))
    busstop = [0] * N
    count = 0
    for i in charger:
        busstop[i] += 1
    for i in range(start+1, start+K+1):
        busstop[i] = 1
        start = i


    for j in range(len(charger)):
        if charger[j+1] - charger[j] > K:
            count = 0





    print(f'#{tc+1} {count}')