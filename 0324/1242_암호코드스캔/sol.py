import sys; sys.stdin = open('sample_input.txt')

# 2차원 배열을 전부 2진수로 바꾼다

# 2차원 배열을 위, 뒤에서부터 탐색해서

# 맨 처음 1이 나오고 그 윗부분이 0인 위치를 찾는다

# 그 위치에서부터 몇자리? 를 10진수로 바꿔서

# 이 이진수 암호의 길이를 조사해서

# 어차피 이 길이는 7의 배수일 것이기 때문에

# code[i*7]의 값만 다시 code에 저장한다

# 그러면 비율 따로 계산 안해도 될듯

# codes 라는 배열에 넣는다

# 넣을 때 codes 안에 있는지 확인하고 같은 값이면 안넣는다

# 그러면 codes에는 암호들만 들어 있다

# 이 암호들의 유효성을 검사해서 정답을 낸다



password = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

T = int(input())


def is_code_valid(x):
    hap = 0
    if (((int(x[0]) + int(x[2]) + int(x[4]) + int(x[6])) * 3) + (int(x[1]) + int(x[3]) + int(x[5])) + int(
            x[7])) % 10 == 0:
        for i in range(8):
            hap += int(x[i])
        return hap
    return hap


# print(is_code_valid('88012346'))

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # arr = [list(map(str, input())) for _ in range(N)]
    arr = [input() for _ in range(N)]
    # pprint(arr)

    point_i = 0
    point_j = 0

    for i in range(N):
        for j in range(M - 1, -1, -1):
            if arr[i][j] != '0':
                point_i = i
                point_j = j
                break
        if point_i > 0:
            break

    # print(point_i)
    # print(point_j)

    code = arr[point_i]
    # print(code)

    result = ''

    while point_j - 7 > 0:
        if code[point_j - 6:point_j + 1] in password:
            result = '' + str(password[code[point_j - 6:point_j + 1]]) + result
            point_j -= 7
        else:
            point_j -= 1

    # print(result)
    print(f'#{tc} {is_code_valid(result)}')