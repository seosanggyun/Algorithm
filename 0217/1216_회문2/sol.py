# 제가 쓴 코드를 어떻게든 뜯어고쳐 보고 있었지만
# 이제는 그냥 재준님 코드를 보고 따라해볼까 하는 유혹에
# 넘어가려고 하는 제 자신이 밉습니다 교수님
# 우선 제출 해놓고 나머지 정리해서 업데이트 하겠습니다
# 제출기한 넉넉하게 주셔서 감사합니다 교수님

import sys;

sys.stdin = open('input.txt')


def check_pal(p):
    for i in range(len(p) // 2):
        if p[i] != p[len(p) - 1 - i]:
            return False
        else:
            return True


for tc in range(10):
    T = int(input())
    arr = [list(input()) for i in range(100)]
    row_max = 0
    for l in range(len(arr), 0, -1):
        for i in range(len(arr)):
            for j in range(len(arr) - l + 1):
                p_row = []
                for k in range(l):
                    p_row.append(arr[i][j + k])
                if check_pal(p_row):
                    if row_max < len(p_row):
                        row_max = len(p_row)
                    break

    col_max = 0
    for l in range(len(arr), 0, -1):
        for i in range(len(arr)):
            for j in range(len(arr) - l + 1):
                p_col = []
            for k in range(l):
                p_col.append(arr[j + k][i])
            if check_pal(p_col):
                if col_max < len(p_col):
                    col_max = len(p_col)
                break

    if row_max > col_max:
        print(f'#{tc + 1} {row_max}')
    else:
        print(f'#{tc + 1} {col_max}')


# 재준님 코드
# 함수를 엄청 잘 쓰셔서 코드가 깔끔함


# import sys
# sys.stdin = open('input.txt')
#
# def palindrome(string):
#     l = len(string)
#     for i in range(l // 2):
#         if string[i] != string[l - 1 - i]:
#             return False
#     return True
#
# def find_palindrome_line(m, string):
#     for i in range(len(string) - m + 1):
#         check = string[i:i + m]
#         if palindrome(check):
#             return check
#
# def reverse_array(n, array):
#     for i in range(n):
#         for j in range(n):
#             if i < j:
#                 array[i][j], array[j][i] = array[j][i], array[i][j]
#
# def find_palindrome(n, m, array):
#     for i in range(2):
#         for i in range(n):
#             result = find_palindrome_line(m, array[i])
#             if result:
#                 return result
#
#         reverse_array(n,array)
#
# def find_biggest_palindrome(array):
#     for i in range(100, 0, -1):
#         result = find_palindrome(100, i, array)
#         if result:
#             return result
#
# for tc in range(1, 11):
#     n = int(input())
#     array = [list(input()) for i in range(100)]
#     print(f'#{tc} {len(find_biggest_palindrome(array))}')
