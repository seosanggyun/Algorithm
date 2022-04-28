import sys
sys.stdin = open('input.txt')

def search(now, gas, cnt):
    global result
    
    # 현재 위치가 도착지를 벗어난다면 (충분히 도착 가능하다면)
    if now >= len(station)-1:
        # 방문 횟수 최솟값 치환
        if cnt < result:
            result = cnt
    # 가스 소지량 만큼 계산
    else:
        if gas > 0:
            search(now+1, gas-1, cnt)
        # 가지치기 : 아직 충전해도 된다면
        if cnt < result:
            search(now+1, station[now]-1, cnt+1)

    

T = int(input())
for tc in range(1, T+1):
    # 0번째 -> 정류장 수 / 1번째 ~ N-1: 각 정류장 별 충전지
    arr = list(map(int, input().split()))
    station = arr[1:] + [0]
    # 최악의 경우 = 모든 정류장 방문
    result = arr[0]
    search(1, station[0]-1, 0)
    print(f'#{tc} {result}')