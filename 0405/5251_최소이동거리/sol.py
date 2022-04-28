import sys
from pprint import pprint
sys.stdin = open('sample_input.txt')

def dijkstra():
    visited = [0 for _ in range(N+1)]

    di = [E*100 for _ in range(N+1)]

    # 출발점인 0번 노드는 0으로 설정,
    # 이후에 0번 노드부터 인접한 노드를 탐색하여
    # 다음 경로까지의 최솟값을 기록
    di[0] = 0



T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    # 큰 값으로 초기화한 이유는
    # 이후 그래프를 탐색하면서
    # 최솟값을 찾을 때
    # 연결되어 있지 않은 그래프는
    # 최솟값의 후보에서 벗어나도록 하기 위함
    adj = [[E*100 for _ in range(N+1)] for _ in range(N+1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w
    pprint(adj)

