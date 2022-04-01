import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    tree = [0 for _ in range(N+1)]
    last = 1

    for i in range(len(data)):
        if not tree[i]:
            tree[last] = data[i]
        else:
            last += 1
            child = last
            parent = child//2

            tree[child] = data[i]

            # 부모가 자식보다 큰 동안
            while tree[parent] > tree[child]:
                # 부모와 자식 위치 변경
                tree[parent], tree[child] = tree[child], tree[parent]
                # 자식 위치를 부모로 변경
                child = parent
                # 부모는 부모 // 2 => 조상 노드
                parent = parent // 2
    last = N
    result = 0
    # 현재 탐색 노드가 root 노드가 될 때까지
    while last > 0:
        # 내 현재 위치의 조상 노드 값을 result에 더해 나간다.
        result += tree[last//2]
        last = last // 2
    print('#{} {}'.format(tc, result))