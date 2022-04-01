import sys
sys.stdin = open('input.txt')

def BFS(S, cnt):
    # 최종 결과 초기화
    result = [0,0]
    Q = []
    Q.append((S, cnt))
    # 출발지 방문 표시
    visited[S] = 1
    while Q:
        S, cnt = Q.pop(0)
        for w in range(101):
            # 다음 방문 지점 존재하고, 해당 지점 방문한적 없다면
            if data[S][w] and visited[w] == 0:
                # 해당 지점 방문 표시
                visited[w] = 1
                # 이전에 방문 한것 보다 더 많이 방문했다면
                if result[1] < cnt:
                    # 가장 마지막에 방문한 위치의 번호와
                    # 방문 횟수 기록
                    result = [data[S][w], cnt]
                # 이전에 방문한 횟수와 같고,
                # 이전에 방문한 위치의 번호보다 현재 방문 위치가 크다면
                # 최종 방문한 사람의 값들 중, 가장 큰 값이 가장 마지막에 기록
                elif result[1] == cnt and result[0] < data[S][w]:
                    # 해당 위치의 값과 방문 횟수 추가
                    result= [data[S][w], cnt]
                Q.append((w, cnt+1))
    return result

for tc in range(1, 11):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))

    # 방문 표시
    visited = [0]*101
    # 인접행렬 최대크기 101
    data = [[0]*101 for _ in range(101)]

    # 인접행렬 표시
    for i in range(N//2):
        data[arr[i*2]][arr[i*2+1]] = arr[i*2+1]

    # 시작점, 방문 횟수
    ans = BFS(S, 0)
    # 최종 방문지의 가장 마지막 값이 최댓값
    print(f'#{tc} {ans[0]}')