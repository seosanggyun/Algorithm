import sys
sys.stdin = open('input.txt')

def search(w, cost):
    global result
    # print(cost)
    # 현재 비용이 최솟값보다 커지면 더 조사할 필요 없음
    if cost > result:
        return
    
    # 모든 물품 조사시 비용 확인
    if w == N:
        if cost < result:
            result = cost
    else:
        # 다른 물품 비용 더하기
        for i in range(N):
            # 이전에 더하지 않은 상품만
            if not visited[i]:
                # 더하거나
                visited[i] = 1
                # 다음 공장, 현재까지 비용 + 현재 공장의 해당 물품
                search(w+1, cost + arr[w][i])
                # 안더하거나
                visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    
    visited = [0]*N
    # 최종 결과
    result = sum(sum(arr, []))
    # 0번 공장, 비용 0
    search(0, 0)
    print(f'#{tc} {result}')