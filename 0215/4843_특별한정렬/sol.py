import sys; sys.stdin = open('sample_input.txt')

T = int(input())

# 버블소트로 오름차순으로 정렬 한 다음
# 맨 뒤에서 하나, 맨 앞에서 하나씩 가져올거임

# 버블소트 정의
def BubbleSort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


# 테스트 케이스만큼 반복
for tc in range(T):
    # 정수의 개수 입력
    N = int(input())
    # N개의 정수들 리스트로 입력
    arr = list(map(int, input().split()))
    # N개의 정수들 버블소트로 오름차순 정렬
    arr = BubbleSort(arr, N)
    # 결과값을 저장할 result 리스트 초기화
    result = []
    # 10개만 출력하면 되니 5번 반복
    for i in range(5):
        # 맨뒤에서 하나씩 가져와서 result 리스트에 더해주기
        result.append(arr[N-1-i])
        # 맨 앞에서 하나씩 가져와서 result 리스트에 더해주기
        result.append(arr[i])

    # result는 리스트인데
    # 문자열 형태로 출력해야 함
    # result의 요소들을 하나하나 문자열로 바꿔줌
    result = list(map(str, result))
    # 공백을 기준으로 요소들을 문자열로 합침
    result = ' '.join(result)
    # 결과 출력
    print(f'#{tc+1} {result}')
