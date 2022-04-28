import sys
sys.stdin = open('input.txt')

def dijkstra():
    # 방문 표시
    visited = [0] * (V+1)
    # 충분히 큰 값
    di = [E*100] * (V+1)

    # 시작점 0은 항상 0
    di[0] = 0

    # 전수 조사
    for _ in range(V):

        min_idx = -1
        min_value = E*100

        # 최솟값 찾기
        for i in range(V+1):
            if not visited[i] and min_value > di[i]:
                min_idx = i
                min_value = di[i]
        visited[min_idx] = 1

        # 다음 갱신 지점 찾기
        for j in range(V + 1):
            if not visited[j] and di[j] > di[min_idx]:
                di[j] = di[min_idx] + adj[min_idx][j]
    return di[V]


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    adj = [[E*100] * (V+1) for _ in range(V + 1)]

    # 시작점, 끝점, 가중치
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w
    print(dijkstra())

