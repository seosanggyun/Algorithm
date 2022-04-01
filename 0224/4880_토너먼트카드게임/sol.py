import sys; sys.stdin = open('sample_input.txt')

T = int(input())


def rsp(lst, begin, end):
    if begin == end:
        return begin

    p = (begin + end) // 2
    match1 = rsp(lst, begin, p)
    match2 = rsp(lst, p+1, end)
    return winner(match1, match2)


def winner(a, b):
    if a == 1:
        if b == 1:
            return a
        elif b == 2:
            return b
        elif b == 3:
            return a
    elif a == 2:
        if b == 1:
            return a
        elif b == 2:
            return a
        elif b == 3:
            return b
    elif a == 3:
        return a



for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    begin = 1
    end = N
    print(f'#{tc} {rsp(lst, begin, end)}')

