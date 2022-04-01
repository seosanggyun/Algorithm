import sys
sys.stdin = open('input.txt')

def cal(word, stack):
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
    return stack[-1]

for tc in range(1, 11):
    N = int(input())
    word = input()
    stack = []
    result = ''

    for char in word:
        if char in '*+':
            if not stack:
                stack.append(char)
            elif char in '*':
                while stack and stack[-1] in '*':
                    result += stack.pop()
                stack.append(char)
            elif char in '+':
                while stack:
                    result += stack.pop()
                stack.append(char)
        else:
            result += char

    while stack:
        result += stack.pop()
    result = cal(result, [])
    
    print(f'#{tc} {result}')