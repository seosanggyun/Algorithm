import sys; sys.stdin = open('input.txt')
from pprint import pprint 

password = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9
}


T = int(input())

def is_code_valid(x):
    
    hap = 0
    if (((int(x[0]) + int(x[2]) + int(x[4]) + int(x[6])) * 3) + (int(x[1]) + int(x[3]) + int(x[5])) + int(x[7])) % 10 == 0:
        for i in range(8):
            hap += int(x[i])
        return hap
    return hap

# print(is_code_valid('88012346'))

for tc in range(1,T+1):
    N, M = map(int, input().split())
    # arr = [list(map(str, input())) for _ in range(N)]
    arr = [input() for _ in range(N)]
    # pprint(arr)

    point_i = 0
    point_j = 0

    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
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
        if code[point_j-6:point_j+1] in password:
            result = '' + str(password[code[point_j-6:point_j+1]]) + result
            point_j -= 7
        else:
            point_j -= 1

    # print(result)
    print(f'#{tc} {is_code_valid(result)}')

                
    


