import sys
sys.stdin = open('input.txt')

# 탐색 시작점
def BFS(v):
    # 방문 가능 지점 = 정점의 개수
    visited = [0]*(V+1)
    queue = []
    # 탐색 시작점
    queue.append(v)
    # 작업할 일이 남아 있는 동안
    while queue:
        # print(queue, end=' ')
        # queue의 첫 번째 원소 반환
        v = queue.pop(0)
        # 방문 하지 않았다면,
        if not visited[v]:
            visited[v] = True
            print('{} {}'.format(v, visited))
            for w in range(1, V+1):
                if G[v][w] == 1 and visited[w] == 0:
                    queue.append(w)


V, E = map(int, input().split())
data = list(map(int, input().split()))

G = [[0 for _ in range(V + 1)] for _ in range(V + 1)]

for i in range(V + 1):
    '''
    G[data[0]][data[1]] = 1
    G[data[1]][data[0]] = 1

    G[data[2]][data[3]] = 1
    G[data[3]][data[2]] = 1
    '''
    G[data[i * 2]][data[i * 2 + 1]] = 1
    G[data[i * 2 + 1]][data[i * 2]] = 1

BFS(1)