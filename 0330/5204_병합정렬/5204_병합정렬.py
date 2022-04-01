import sys
sys.stdin = open('input.txt')

def merge(nums):
    global ans

    if len(nums) == 1: return nums

    mid = len(nums) // 2
    left = nums[:mid]       # 왼쪽 절반
    right = nums[mid:]      # 오른쪽 절반
    left = merge(left)      # 왼쪽 절반 정렬 -> base case는 요소가 하나 남는 순간
    right = merge(right)    # 오른쪽 절반 정렬 -> base case는 요소가 하나 남는 순간
    left_idx = right_idx = k = 0 # k는 왼쪽/오른쪽 요소 중 위치가 결정 되었을 때 해당 위치를 잡기 위한 값

    while left_idx < len(left) and right_idx < len(right):  # 좌 우 리스트에서 비교 대상이 남은 경우
        # print(nums, '1')
        # print(left, right)
        if left[left_idx] < right[right_idx]:               # 오른쪽 요소가 더 크다면
            nums[k] = left[left_idx]                        # 왼쪽 값을 먼저 넣고 (작은 값부터)
            left_idx += 1                                   # 왼쪽 idx 증가
        else:
            nums[k] = right[right_idx]                      # 반대면 오른쪽부터 넣고 idx 증가
            right_idx += 1
        k += 1
    # print(nums, '2')

    if left[-1] > right[-1]:              # 왼쪽 마지막 원소가 큰 경우 체크
        ans += 1
    if left_idx < len(left):              # 왼쪽 리스트가 남은 경우 다 털어 넣고
        nums[k:] = left[left_idx:]

    if right_idx < len(right):             # 오른쪽 리스트가 남은 경우 다 털어 넣자
        nums[k:] = right[right_idx:]
    # print(nums, '3')
    # print(ans)
    # print()
    return nums                            # 정렬된 왼쪽과 오른쪽이 합쳐진 최종 리스트
    

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    # print(nums, '0')
    ans = 0
    result = merge(nums)
    print(f'#{tc} {result[N//2]} {ans}')