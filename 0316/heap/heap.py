V = 6
# 각 노드가 가지고 있는 값
arr = [9, 5, 3, 4, 8, 1]

# 주어진 노드를 트리에 순차적으로 집어 넣고
# heap 구조로 만들자.

# tree가 있어야 한다.
tree = [0 for _ in range(V+1)]
# 시작 노드 번호가 1이므로 라스트도 1로 시작
last = 1

for i in range(len(arr)):
    if not tree[last]:
        tree[last] = arr[i]
    else:
        last += 1
        child = last
        parent = child // 2

        tree[child] = arr[i]
        print(tree, parent, child)
        # 부모가 가진 값이 자식이 가진 값보다 큰동안
        while tree[parent] > tree[child]:
            # 부모와 자식의 값을 서로 바꾼다
            tree[parent], tree[child] = tree[child], tree[parent]
            # 자식 위치를 부모로 변경
            child = parent
            # 부모 위의 조상노드
            parent = parent // 2


print(*tree)


