import sys; sys.stdin = open('sample_input.txt')


# 정렬하고 배열 반환

def merge_sort(arr):
    # 요소가 하나면 안 나눠도 됨
    if len(arr) == 1:
        return arr

    # 전체를 절반으로 나누고
    mid = len(arr) // 2
    left = arr[:mid]    # == range(0, mid)
    right = arr[mid:]   # == range(mid, len(arr))

    # 나뉜 각각을 정렬하고
    left = merge_sort(left)
    right = merge_sort(right)

    # 정렬된 각각을 병합
    return merge(left, right)

# 나누어진 두 개의 배열을 하나로 합쳐주기(정렬하면서)
# 정렬된 배열 반환

def merge(left, right):
    global count    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력하기 위한 전역변수
    result = []
    i = j = 0
    left_length = len(left)
    right_length = len(right)
    
    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우에
    # count +1
    if left[-1] > right[-1]:    
        count += 1
    while i < left_length or j < right_length:
        # left와 right 둘다 요소가 남아있으면
        if i < left_length and j < right_length:
            if left[i] < right[j]:      
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        else: # 둘 중 하나는 비교할 요소가 없음
            if i < left_length:     # 왼쪽 요소가 남았을 때
                result.append(left[i])
                i += 1
            elif j < right_length:  # 오른쪽 요소가 남았을 때
                result.append(right[j])
                j += 1
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    count = 0
    arr = list(map(int, input().split()))
    result = merge_sort(arr)
    # print(result)

    print(f'#{tc} {result[N//2]} {count}')


