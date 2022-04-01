import sys
from pprint import pprint
sys.stdin = open('input.txt')


def DFS(now):
    visited[now] = 1
    print(now, visited)

    for next in range(1, V+1):
        if G[now][next] == 1 and visited[next] == 0:
            DFS(next)



V, E = map(int, input().split())
data = list(map(int, input().split()))

visited = [0] * (V+1)

G = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
for i in range(V + 1):
    G[data[i * 2]][data[i * 2 + 1]] = 1
    G[data[i * 2 + 1]][data[i * 2]] = 1

pprint(G)
print('=' * 30)
DFS(1)