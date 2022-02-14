import sys

sys.stdin = open('input.txt')

T = int(input())

# N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하여
# 합이 가장 큰 경우과 가장 작은 경우의 차이를 출력해야함


# 테스트 케이스의 수만큼 반복 돌면서
for tc in range(T):

    # N 과 M을 입력받고
    # ai 리스트에 정수들을 입력받음
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))

    # 합들의 최댓값, 최솟값 구해야 하니
    # 합들을 저장할 리스트 초기화
    sum_list =[]

    # 이웃한 M개의 숫자를 더해야 하는데
    # 0부터 시작해서
    # 0, 1, ... 0+M-1을 더한 뒤 리스트에 저장하고
    # 1, 2, ... 1+M-1을 더한 뒤 리스트에 저장하고
    # ...
    for i1 in range(N-M+1):
        hap = 0
        for i2 in range(i1, i1+M):
            hap += ai[i2]
        sum_list += [hap]

    # sum_list의 최댓값과 최솟값을 구해주기 위해
    # 변수를 리스트의 0번째 값으로 초기화
    sum_min = sum_list[0]
    sum_max = sum_list[0]
    for j in sum_list:
        if j < sum_min:
            sum_min = j
    for k in sum_list:
        if k > sum_max:
            sum_max = k


    # 결과 출력
    print(f'#{tc+1} {sum_max - sum_min}')




