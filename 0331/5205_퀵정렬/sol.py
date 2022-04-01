import sys;

sys.stdin = open('sample_input.txt')


def qSort(arr, s, e):
    # 배열을 파티션 기준으로 나누는데
    # 나눴을 때의 요소가 1개가 되면
    # s == e 가 되므로 재귀 종료
    if s < e:
        p = hoare_partition(arr, s, e)
        qSort(arr, s, p - 1)
        qSort(arr, p + 1, e)


def hoare_partition(arr, left, right):
    # pivot : 배열의 맨 왼쪽 값
    pivot = arr[left]
    # i : 배열의 맨 왼쪽 index
    # j : 배열의 맨 오른쪽 index
    i = left
    j = right

    # i가 j를 역전하여 교차하기 전까지 반복
    while i <= j:
        # i 위치의 값이 pivot 값 보다 작거나 같다면
        # 즉 i 위치의 값이 pivot 값보다 큰 수를 찾을 때 까지
        # i += 1
        while i <= j and arr[i] <= pivot:
            i += 1
        # j 위치의 값이 pivot 값 보다 크거나 같다면
        # 즉 j 위치의 값이 pivot 값보다 작은 수를 찾을 때 까지
        # j -= 1
        while i <= j and arr[j] >= pivot:
            j -= 1

        # i와 j의 위치를 반복문을 통해 다 바꿨는데도
        # 교차가 되지 않은 상황
        # 즉 i 위치의 값이 pivot 보다 크고,
        # j 위치의 값이 pivot 보다 작을 때
        # 두 값 위치 바꿈
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # i와 j가 교차되면 pivot 과 j 위치의 값을 바꿈
    arr[left], arr[j] = arr[j], arr[left]
    # print(arr)
    return j


def lomuto_partition(arr, left, right):
    # pivot : 배열의 맨 오른쪽 값
    pivot = arr[right]
    # i : 배열의 맨 왼쪽 index - 1
    i = left - 1
    # j : 배열의 맨 왼쪽 index

    # j : 초기값부터 pivot 값 바로 전 index 까지 반복
    for j in range(left, right):
        # j 위치의 값이 pivot 값보다 커질때까지
        # i += 1
        # i 위치의 값과 j 위치의 값 바꾸기
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # j 가 pivot 바로 전까지 도착하면
    # pivot 값과 i + 1 위치의 값을 바꿈
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    # print(arr)
    return i + 1


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    # print(arr)
    e = len(arr) - 1
    s = 0
    qSort(arr, s, e)
    print(f'#{tc} {arr[N // 2]}')
