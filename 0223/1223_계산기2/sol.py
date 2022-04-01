import sys; sys.stdin = open('input.txt')

T = 10

# 중위 표기식에서 토큰을 읽고
# 토큰이 피연산자(숫자)이면 토큰을 후위 표기식에 출력
# 토큰이 연산자일 때, 이 토큰이 스택의 맨 위에 있는 연산자보다
# 우선순위가 높으면 스택에 push,
# 우선순위가 낮으면 스택의 맨 위에 잇는 연산자의 우선순위가
# 토큰의 우선순위보다 작아질 때 까지
# 스택에서 pop 한 후 토큰을 push
# 스택이 비어있으면 무조건 push
# 토큰에 여는괄호('(')가 나오면 무조건 스택에 push

# 우선순위를 어떻게 설정하지
# 딕셔너리

# 토큰이 닫는 괄호가 나오면 스택 top에 여는 괄호가 나올때까지
# popopopopop
# 여는 괄호를 만나면 여는 괄호는 후위표기식에 출력 안함

# 중위 표기식 끝까지 이 과정을 돌리고
# 다 끝났는데 스택에 연산자들이 남아있으면
# 걔네들 다 pop해서 후위표기식에 출력

####################
# 이 문제는 괄호가 없는데 내가 괄호를..
####################


for tc in range(1,T+1):
    N = int(input())
    susik = list(input())
    buho = ['+', '*']
    buho_dict = {'+': 1, '*': 2}

    stack = []
    hoowee = []

    for i in susik:
        if i not in buho:
            hoowee.append(i)
        else:
            buho_value = buho_dict.get(i)
            if stack != [] and buho_value > buho_dict.get(stack[-1]):
                stack.append(i)
            elif stack == []:
                stack.append(i)
            else:
                while stack != [] and buho_value <= buho_dict.get(stack[-1]):
                    hoowee.append(stack[-1])
                    stack.pop()
                stack.append(i)
    while stack != []:
        hoowee.append(stack[-1])
        stack.pop()


    hoowee = ''.join(hoowee)
    hoowee_cnt = len(hoowee)
    n_stack = []
    result = 0
    for i in range(hoowee_cnt):
        if hoowee[i] not in buho:
            n_stack.append(hoowee[i])
        else:
            if hoowee[i] == '+':
                n1 = int(n_stack.pop())
                n2 = int(n_stack.pop())
                new = n2 + n1
                n_stack.append(new)
            elif hoowee[i] == '*':
                n1 = int(n_stack.pop())
                n2 = int(n_stack.pop())
                new = n2 * n1
                n_stack.append(new)

    res = int(n_stack[0])

    print(f'#{tc} {res}')




