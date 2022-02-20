import sys; sys.stdin = open('input.txt')

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     sell_price = list(map(int, input().split()))
#     result = 0
#     start = 0
#     max_price = 0
#     while start < N:
#         max_price = start
#         for i in range(start, N):
#             if sell_price[max_price] < sell_price[i]:
#                 max_price = i
#         for i in range(start, max_price):
#             result += sell_price[max_price] - sell_price[i]
#         start = max_price + 1
#     print(f'#{tc} {result}')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    future = list(map(int, input().split()))
    start = 0
    iduk = 0
    while start < len(future):
        max_price = 0
        for i in range(start, len(future)):
            if future[i] > max_price:
                max_price = future[i]
        for j in range(start, len(future)):
            iduk += max_price - future[j]
            if future[j] == max_price:
                start = j+1
                break
    print(f'#{tc} {iduk}')





































