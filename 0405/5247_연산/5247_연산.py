import sys
sys.stdin = open('input.txt')

def BFS(N, M):
    front = rear = -1
    visited[N] = 1  # 방문 기록
    rear += 1
    Q[rear] = N  # 큐에 시작 노드 인큐

    while front != rear:  # 큐가 비어있지 않으면
        front += 1
        n = Q[front]  # 다음 노드를 꺼내
        operator = [n + 1, n - 1, n * 2, n - 10]  # 인접 노드번호 계산

        for i in range(4):
            if operator[i] == M:  # 찾는 노드인 경우 거리 리턴
                return visited[n]
            if 0 < operator[i] <= 1000000:  # 유효한 노드 번호이므로
                if visited[operator[i]] == 0:  # 아직 방문하지 않은 노드면
                    visited[operator[i]] = visited[n] + 1  # 거리를 기록하고
                    rear += 1
                    Q[rear] = operator[i]

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Q = [0] * 1000001
    visited = [0] * 1000001
    print(f'#{tc} {BFS(N, M)}')