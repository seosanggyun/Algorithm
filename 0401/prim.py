'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

def prim1(r, V):
    MST = [0]*(V+1)             # MST 포함여부
    key = [10000] * (V+1)       # 가중치의 최대값 이상으로 초기화. key[v]는 v가 MST에 속한 정점과 연결될 때의 가중치
    key[r] = 0                  # 시작정점의 key
    for _ in range(V):          # V+1개의 정점 중 V개를 선택
        # MST에 포함되지 않는 정점 중(MST[u]==0), key가 최소인 u 찾기
        u = 0
        minV = 10000
        for i in range(V + 1):
            if MST[i]==0 and key[i]<minV:
                u = i
                minV = key[i]
        MST[u] = 1              # 정점 u를 MST에 추가
        # u에 인접인 v에 대해, MST에 포함되지 않은 정점이면
        for v in range(V+1):
            if MST[v]==0 and adjM[u][v]>0:
                key[v] = min(key[v], adjM[u][v])
    return sum(key)

def prim2(r, V):
    MST = [0] * (V+1)           # MST 포함 여부
    MST[r] = 1
    s = 0
    for _ in range(V):
        u = 0
        minV = 10000
        for i in range(V+1):    # MST에 포함된 정점 i와 인접한 정점 j 중 MST()
            if MST[i] == 1:
                for j in range(V+1):
                    if 0 < adjM[i][j] < minV and MST[j]==0:
                        u = j
                        minV = adjM[i][j]

        s += minV
        MST[u] = 1

    return s


V, E = map(int, input().split())
adjM = [[0] * (V+1) for _ in range(V+1)]
# adjL = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w
    adjM[v][u] = w      # 가중치가 있는 무방향 그래프
    # adjL[u].append((v,w))
    # adjL[v].append((u,w))

print(adjM)
# print(adjL)
print(prim1(0,V))
print(prim2(0,V))
