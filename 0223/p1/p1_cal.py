import sys
sys.stdin = open('input_cal.txt')

T = int(input())

for tc in range(1, T+1):
    word = input()
    stack = []
    result = 0
    for char in word:
        if char not in '*/+-':
            stack.append(int(char))
        else:
            x = stack.pop()
            y = stack.pop()
            if char == '+':
                stack.append(y + x)
            elif char == '-':
                stack.append(y - x)
            elif char == '*':
                stack.append(y * x)
            elif char == '/':
                stack.append(y / x)
    print(f'#{tc} {stack[-1]}')