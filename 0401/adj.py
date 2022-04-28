'''
마지막 정점번호, 간선 수
6 8
0 1 0 2 0 5 0 6 5 3 4 3 5 4 6 4
'''

def dfs1(v, V):
    visited[v] = 1
    print(v, end = ' ')
    for w in range(V+1):     # i에 인접한 모든 노드 w에 대해
        if adjM[v][w] and visited[w] == 0:      # 아직 방문하지 않은 곳이면
            dfs1(w, V)


def dfs2(v, V):
    visited[v] = 1
    print(v, end = ' ')
    for w in adjL[v]:     # i에 인접한 모든 노드 w에 대해
        if visited[w] == 0:      # 아직 방문하지 않은 곳이면
            dfs2(w, V)




V, E = map(int, input().split()) # V 마지막 정점 번호, E 간선 수
arr = list(map(int, input().split()))
adjM = [[0] * (V+1) for _ in range(V+1)]
adjL = [[] for _ in range(V+1)]

# 인접 행렬
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjM[n1][n2] = 1
    adjM[n2][n1] = 1    # 무향 그래프인 경우 이 행이 추가적으로 필요함

# 인접 리스트
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjL[n1].append(n2)
    adjL[n2].append(n1) # 무향 그래프인 경우에만 이 행이 추가적으로 필요함

visited = [0]*(V+1)

dfs1(0, V)
# dfs2(0, V)