import sys
from pprint import pprint
sys.stdin = open('input.txt')

# 시작 정점 위치를 인자로 받는다.
def DFS(start):
    # stack에 조사 위치를 쌓아 나간다.
    stack = []
    # 방문 정보를 담을수 있는 리스트가 필요하다.
    visited = [False] * (V+1)

    # 처음 시작 위치를 visited에 표시 한다.
    visited[start] = True
    print(start, visited)
    # print(visited)
    # 언제까지 조사를 할 것이냐
    # 다음 방문 노드가 없을 때 까지
    while start != 0:
        # 순회할 다음 위치는 무엇을 기준으로 잡느냐?
        for next in range(1, V+1):
            # 현재 위치에서 다음 위치의 인접 행렬 조사
            # 1이다 == 이동 가능하다.
            # 한번 갔었던 곳에 돌아가지는 않겠다.
            if G[start][next] == 1 and visited[next] == 0:
                # 현재 위치 저장
                stack.append(start)
                start = next
                print(start, visited)
                visited[start] = True
                break
        # 현재 위치 기준, 다음 조사 노드 없으면
        else:
            # 하지만 stack이 아직 남아 있다면
            if stack:
                start = stack.pop()
            else:
                start = 0



V, E = map(int, input().split())
data = list(map(int, input().split()))

print(data)
# 노드의 번호는 1번부터 시작하니, V+1
G = [[0 for _ in range(V+1)] for _ in range(V+1)]

# pprint(G)

for i in range(V+1):
    '''
    G[1][2] = 1
    G[2][1] = 1
    
    G[data[0]][data[1]] = 1
    G[data[1]][data[0]] = 1
    
    G[data[2]][data[3]] = 1
    G[data[3]][data[2]] = 1
    '''
    G[data[i*2]][data[i*2+1]] = 1
    G[data[i * 2 + 1]][data[i * 2]] = 1

pprint(G)
print('='*30)
DFS(1)