import sys; sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    # 코드를 리스트로 입력
    code = list(input())
    # 스택 초기화
    stack = []
    # top 초기화
    top = 0
    # 제대로 짝을 이루면 1, 안 이루면 0을 출력할
    # flag 1로 초기화
    flag = 1
    # 코드가 담긴 리스트를 순회
    for i in range(len(code)):
        # 코드의 요소가 ( { 일경우
        if code[i] == '(' or code[i] == '{':
            # 스택에 추가하고
            # top +1
            stack.append(code[i])
            top += 1
        # 만약 코드의 요소가 } 일 경우
        elif code[i] == '}':
            # 만약 스택에 아무것도 없을 경우
            # 여는 괄호 없이 닫는 괄호만 나온 경우이므로
            # 짝이 맞지 않음
            # flag = 0 할당
            if len(stack) == 0:
                flag = 0
            # 스택에 요소가 있을 경우
            else:
                # 만약 코드의 요소가 } 이고 앞의 값이 { 일 경우
                # { 제거
                # top -1
                if stack[top - 1] == '{':
                    stack.pop()
                    top -= 1
                # 그 외의 값이 있을 경우
                # 짝이 맞지 않는다는 뜻이므로
                # flag = 0
                else:
                    flag = 0

        # 만약 코드의 요소가 ) 일 경우
        elif code[i] == ')':
            # 만약 스택에 아무것도 없을 경우
            # 여는 괄호 없이 닫는 괄호만 나온 경우이므로
            # 짝이 맞지 않음
            # flag = 0 할당
            if len(stack) == 0:
                flag = 0
            # 스택에 요소가 있을 경우
            else:
                # 만약 코드의 요소가 )이고 앞의 값이 ( 일 경우
                # ( 제거
                # top -1
                if stack[top - 1] == '(':
                    stack.pop()
                    top -= 1
                # 그 외의 값이 있을 경우
                # 짝이 맞지 않는다는 뜻이므로
                # flag = 0
                else:
                    flag = 0

    # 이 과정을 거치고 스택에 괄호가 남아 있을 경우
    # 짝이 맞지 않은 경우임
    # flag = 0
    if stack:
        flag = 0

    print(f'#{tc} {flag}')


