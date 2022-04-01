import sys
sys.stdin = open('input.txt')

# 후위 순회
def postorder(node):
    if len(arr[node]) == 2:
        return arr[node][1]
    else:
        l = postorder(arr[node][2])
        r = postorder(arr[node][3])

        if arr[node][1] == '+':
            return l + r
        elif arr[node][1] == '-':
            return l - r
        elif arr[node][1] == '*':
            return l * r
        else:
            return l // r

for tc in range(1, 11):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    for data in arr:
        i = 0
        # 연산을 위해 모든 10잔수 정수로 변경
        while i < len(data):
            if data[i].isdecimal():
                data[i] = int(data[i])
            i += 1
    # node 번호가 1부터 시작 -> 0은 사용하지 않음
    arr.insert(0, 0)
    print(f'#{tc} {postorder(1)}')