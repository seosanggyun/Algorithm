import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    # 트리 초기화
    tree = [0 for _ in range(N+1)]

    # 트리에 리프 노드 입력
    for i in range(M):
        tree[arr[i][0]] = arr[i][1]
    # 리프 노드 부터 부모 노드에 값 더해 나가기
    # 단, L번째 탐색이 시작되었을때 멈춤
    # 필요한 것은 tree의 L번째 값
    while N != L:
        tree[N//2] += tree[N]
        N -= 1
    print(f'#{tc} {tree[L]}')