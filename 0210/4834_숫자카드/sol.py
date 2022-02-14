import sys

sys.stdin = open('input.txt')

# 카드의 숫자들을 리스트로 받고
# 가장 많은 카드에 적힌 숫자와 카드가 몇장인지 출력하기 위해
# count라는 리스트를 만들어서 카드 종류(index) 별 출현 빈도(value)를 저장하고
# 가장 높은 출현 빈도(value) 값과 그 카드 종류(index)를 출력할 거임



# 테스트 케이스의 수 입력받음
T = int(input())


# 테스트 케이스의 수 만큼 반복
for tc in range(T):
    # 카드 개수 입력
    N = int(input())
    # 카드 숫자들을 공백없이 받음
    ai = list(map(int, input()))
    # count 리스트 초기화
    count = [0] * 10

    # ai 리스트를 순회하면서
    # index가 i에 해당하는 count 리스트의 value에 1씩 더해줌
    for i in ai:
        count[i] += 1

    # count 리스트에서 최댓값을 찾기 위해 초기화
    count_max = count[0]
    # count 리스트에서 중복되는 최댓값이 나올 수 있으므로
    # 중복되는 값들도 저장하기 위해
    # count_max_list 라는 이름의 리스트도 초기화
    count_max_list = []

    # count에서 최댓값 찾기
    for j in count:
        if count_max < j:
            count_max = j

    # count 리스트를 enumerate 순회하여
    # value와 count_max 값이 같은 경우
    # count_max_list에 해당 index 값을 저장
    for k, value in enumerate(count):
        if value == count_max:
            count_max_list += [k]

    # count_max_list에서도 최댓값을 구해야 하므로
    # result 라는 변수에
    # count_max_list의 0번째 요소로 초기화
    result = count_max_list[0]

    # 최댓값 result 찾기
    for l in count_max_list:
        if result < l:
            result = l

    # 형식에 맞추어 출력
    print(f'#{tc+1} {result} {count_max}')













