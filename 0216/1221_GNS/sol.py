import sys; sys.stdin = open('GNS_test_input.txt')

# 외계행성에서 사용하는 숫자를 아라비아숫자로 정렬하기 위해
# 리스트에 넣어준 뒤
# 리스트의 인덱스를 사용하여 정렬할거임
dic = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

# 테스트 케이스
T = int(input())

# 테스트 케이스의 수 만큼 반복
for _ in range(T):
    # 입력값 받아줌
    tc, length = map(str, input().split())
    # 외계 숫자들을 리스트에 문자열 형태로 저장
    n_list = list(map(str, input().split()))
    # 외계 숫자들을 dic의 인덱스로 변환하여 저장할 리스트 초기화
    new_list = []

    # 외계숫자들을 받은 리스트 길이만큼 반복
    for i in range(int(length)):
        # 새 리스트에 외계숫자들을 dic의 인덱스로 변환한 값을 저장
        new_list.append(dic.index(n_list[i]))

    # 숫자니까 정렬 가능
    new_list.sort()

    # 다시 새 리스트의 인덱스들을
    # 외계숫자로 변환
    for j in range(int(length)):
        new_list[j] = dic[new_list[j]]

    # 출력
    # 이번에는 #tc가 주어지니까 그대로 출력하고
    # new_list에 있는 요소들을
    # 언패킹하여 출력
    print(tc)
    print(*new_list)




