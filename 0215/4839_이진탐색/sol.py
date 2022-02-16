import sys; sys.stdin = open('sample_input.txt')

T = int(input())

# 이진탐색 정의
def binarySearch(l, r, key):
    start = l
    end = r
    count = 0
    # start 값이 end 값 보다 커지지 않을 때까지
    while start <= end:
        # mid에 중간페이지 저장
        mid = (start + end) // 2
        # mid가 찾는 페이지 일 경우
        if mid == key:
            # count 출력
            return count

        # mid가 찾는 페이지보다 클 경우
        elif mid > key:
            # end에 mid값 할당
            end = mid
            # 카운트 +1
            count += 1
        # mid가 찾는 페이지보다 작을 경우
        else:
            # start에 mid값 할당
            start = mid
            # 카운트 +1
            count += 1
    # 못 찾을 경우에도 count 출력
    return count




for tc in range(T):
    page, a, b = map(int, input().split())
    # ac = a가 찾고자 하는 페이지를 찾는데에 걸린 카운트 값
    ac = binarySearch(1, page, a)
    # bc = b가 찾고자 하는 페이지를 찾는데에 걸린 카운트 값
    bc = binarySearch(1, page, b)

    # 카운트 값이 작은쪽이 이김
    if ac < bc:
        print(f'#{tc+1} A')
    elif ac > bc:
        print(f'#{tc+1} B')
    else:
        print(f'#{tc+1} 0')


