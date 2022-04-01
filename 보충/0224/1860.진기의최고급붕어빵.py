import sys; sys.stdin = open('1860.txt')


for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split()) # N:손님수, M:생산시간, K: 생산량
    arrival_times = list(map(int, input().split())) # 도착 시간

    customer = [0] * (11112)
    for t in arrival_times:    # t 시간에 도착한 손님 수 카운팅
        customer[t] += 1

    ans = 'Possible'
    cnt = 0  # 붕어빵 개수
    for sec in range(0, 11111 + 1):
        if sec and sec % M == 0:
            cnt += K

        if customer[sec]:       # sec 시간에 손님이 도착했는지 판단
            if cnt < customer[sec]:
                ans = 'Impossible'
                break
            cnt -= customer[sec]
    print(f'#{tc} {ans}')


