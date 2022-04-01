import sys
sys.stdin = open('input.txt')
def BFS(s):
    # queue 초기화
    Q = []
    Q.append(s)
    # 방문 정보 갱신
    visited[s] = 1
    while Q:
        w = Q.pop(0)

        for i in range(V+1):
            # 간선이 존재하고, 방문한 적 없다면
            if field[w][i] == 1 and visited[i] == 0:
                # 새로운 작업 목록 추가
                Q.append(i)
                # 이전 방문 정보에 += 1 == 이동 한 거리
                visited[i] = visited[w] + 1

    # 만약 도착점에 방문 했다면
    if visited[G]:
        # 방문 정보가 1부터 시작했으므로 -1
        return visited[G]-1
    # 도착 못했다면 False 반환
    else:
        return visited[G]



T = int(input())
for tc in range(1, T+1):
    # 노드, 간선의 수
    V, E = map(int, input().split())
    # 간선의 수 만큼 주어진 양쪽 노드 번호 (방향성 X)
    line = [(list(map(int, input().split()))) for _ in range(E)]
    # 시작, 도착 노드 번호
    S, G = map(int, input().split())

    # 방문 정보
    visited = [0]*(V+1)
    # 인접 행렬
    field = [[0 for _ in range(V+1)]for _ in range(V+1)]

    for i in range(len(line)):
        field[line[i][0]][line[i][1]] = 1
        field[line[i][1]][line[i][0]] = 1

    print(f'#{tc} {BFS(S)}')