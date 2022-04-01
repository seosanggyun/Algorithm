import sys; sys.stdin = open('1860.txt')

for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split()) # N:손님수, M:생산시간, K: 생산량
    arrival_times = list(map(int, input().split())) # 도착 시간

    arrival_times.sort()  # 손님들의 시간을 정렬

    ans = 'Possible'

    # 특정 초(sec)까지 붕어빵 생산량 = (sec // M) * K
    # 각 손님의 도착순서(i + 1), 도착시간(sec)
    for i, sec in enumerate(arrival_times):
        cnt = (sec // M) * K
        if i + 1 > cnt:
            ans = 'Impossible'
            break
    print(f'#{tc} {ans}')

