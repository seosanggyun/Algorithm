import sys; sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N_list = [2, 3, 5, 7, 11]
    count_list = [0, 0, 0, 0, 0]

    for i in range(5):
        while N % N_list[i] == 0:
            count_list[i] += 1
            N //= N_list[i]

    print(f'#{tc}', end = ' ')
    print(*count_list)

