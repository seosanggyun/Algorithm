import sys
sys.stdin = open('input.txt')

def findset(x):
    # 만약 내가 루트 노드라면
    if x == p[x]:
        # 나 자신을 반환
        return x
    else:
        # 내 루트 노드 찾으러 가기
        return findset(p[x])

def mst():
    c = 0 # 간선의 개수
    result = 0 # 가중치의 합
    i = 0

    # MST를 구성하는 V개의 간선
    while c < V:
        p1 = findset(arr[i][0])
        p2 = findset(arr[i][1])
        # 사이클이 생성되지 않을때
        if p1 != p2:
            # 가중치 더해 나가는 과정
            result += arr[i][2]
            # 간선을 하나 추가 했다
            c += 1
            # 두 노드 간의 관계를 나타낸다
            p[p2] = p1
        i += 1
        print(p)
    return result


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]

    # print(arr)
    arr.sort(key=lambda x : x[2])
    # print(arr)
    p = list(range(V+1))
    print(arr)
    print(p)
    print(mst())
    print('-'*30)