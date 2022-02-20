import sys; sys.stdin=open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    sample = input()
    count = 0
    total = 0
    for i in range(len(sample)):
        if sample[i] == '(':
            count += 1
        elif sample[i] == ')':
            if sample[i-1] == '(':
                count -= 1
                total += count
            else:
                count -= 1
                total += 1
    print(f'#{tc} {total}')
