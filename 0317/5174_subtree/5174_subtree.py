import sys
sys.stdin = open('input.txt')

def add_cnt(node):
    global cnt
    if node:
        cnt += 1
        add_cnt(tree[node][0])
        add_cnt(tree[node][1])

T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    # L R V * E+2 (노드는 1부터 E+1까지)
    tree = [[0,0,0] for _ in range(E+2)]

    for i in range(E):
        parent, child = arr[i*2], arr[i*2+1]
        if tree[parent][0]:
            tree[parent][1] = child
        else:
            tree[parent][0] = child
        tree[child][2] = parent
    print(tree)

    cnt = 0
    add_cnt(N)
    print(f'#{tc} {cnt}')
