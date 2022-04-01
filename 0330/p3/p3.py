import sys
sys.stdin = open('input.txt')

"""
1. Tree에서는 정점의 개수만 알려줘도 간선은 V-1개로 알 수 있음
2. 1차원 배열 / 2차원 배열 모두 표현이 가능하지만 이 문제는 2차원으로 풀어보자

첫 줄에는 트리의 정점의 총 수 V가 주어진다. 그 다음 줄에는 V-1개 간선이 나열된다.
간선은 그것을 이루는 두 정점으로 표기된다. 간선은 항상 “부모 자식” 순서로 표기된다.
아래 예에서 두 번째 줄 처음 1과 2는 정점 1과 2를 잇는 간선을 의미하며 1이 부모, 2가 자식을 의미한다.
간선은 부모 정점 번호가 작은 것부터 나열되고, 부모 정점이 동일하다면 자식 정점 번호가 작은 것부터 나열된다.

다음 이진 트리 표현에 대하여 전위/중위/후회 순회하여 정점의 번호를 출력하시오
13 -> 정점의 개수
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

루트 노드 -> 부모가 없음 (루트가 주어지지 않은 경우 부모가 없는 노드를 찾으면 그게 루트 노드가 된다.)
잎/리프/터미널 노드 -> 자식이 없음
"""

# 전위 순회 (V -> L -> R)
def pre_order(node):
    global cnt
    if node != 0:
        # cnt += 1

        print('{}'.format(node), end=' ')
        # 그 다음 node의 왼쪽 방문
        pre_order(tree[node][0])
        # 오른쪽 방문
        pre_order(tree[node][1])

# 중위 순회 (L -> V -> R)
def in_order(node):
    if node != 0:
        # 왼쪽 먼저 방문하고
        in_order(tree[node][0])
        print('{}'.format(node), end=' ')
        # 오른쪽 방문
        in_order(tree[node][1])

# 후위 순회 (L -> R -> V)
def post_order(node):
    if node != 0:
        # 왼쪽 방문하고
        post_order(tree[node][0])
        # 오른쪽 방문하고
        post_order(tree[node][1])
        print('{}'.format(node), end=' ')

def print_tree():
    # 0은 생략
    for i in range(1, V+1):
        print('{} {} {} {}'.format(i, tree[i][0], tree[i][1], tree[i][2]))

# Tree에서의 간선 -> V-1
V, E = map(int, input().split())


# left, right, parent - 2차원 배열 준비 -> 0, 1, 2 필요
# 모두 0으로 초기화 / 1번 부터 시작하기 위해 V+1 (1번 ~ 13번)
tree = [[0 for _ in range(3)] for _ in range(V+1)]
"""
                1          2          3      ...
[[0, 0, 0], [2, 3, 0], [4, 0, 1], [5, 6, 1], ...]

1번 노드
- 왼쪽: 2번
- 오른쪽: 3번
- 부모: 없음

2번 노드
- 왼쪽: 4번
- 오른쪽: 없음
- 부모: 1번

3번 노드
- 왼쪽: 5번
- 오른쪽: 6번
- 부모: 1번
"""

# 정점 간 연결 정보(부모-자식)
temp = list(map(int, input().split()))
# 호출 횟수 (optional)
cnt = 0

# 간선의 수만큼 반복을 돌며
for i in range(E):
    # parent, child -> 노드 번호를 의미(1번 ~ 13번)
    # [0, 0, 0] -> 0번째: 왼쪽 자식 / 1번째: 오른쪽 자식 / 2번째: 부모 노드
    parent, child =  temp[i*2], temp[i*2+1]

    # parent 노드의 왼쪽 자식이 없다면 왼쪽 자식으로 넣고
    if not tree[parent][0]:
        tree[parent][0] = child

    # parent 노드의 왼쪽 자식이 있다면 오른쪽 자식으로 넣자
    else:
        tree[parent][1] = child

    # 이후에 부모 노드도 초기화하자
    tree[child][2] = parent

# print_tree()
print('-------------')

print('전위 순회 : ', end='')
pre_order(1)
# print(cnt)
print()

print('중위 순회 : ', end='')
in_order(1)
print()

print('후위 순회 : ', end='')
post_order(1)
print()