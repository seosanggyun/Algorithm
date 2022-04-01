import sys; sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    susik = list(input().split())
    # 나중에 연산자에 해당하는 입력값이 들어왔을 때
    # 연산자임을 확인하고 다른 수행을 하기위한 부호 리스트 정의
    buho = ['+', '-', '*', '/']
    # 스택 초기화
    stack = []
    # 연산이 정확히 될 때를 제외하고는 모두 오류임
    # 따라서 error를 기본 결과값에 설정해놓고 시작
    result = 'error'
    # 입력받은 수식을 순회
    for i in susik:
        # 연산자가 아니라면 스택에 추가
        if i not in buho:
            stack.append(i)
        # 연산을 하려면 스택에 두개 이상의 숫자가 있어야 함,
        # 안 그러면 pop from empty list 뜸
        else:
            if len(stack) < 2:
                break
            # 더하기
            elif i == '+':
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                new = n1 + n2
                stack.append(new)
            # 빼기
            # 빼기와 나누기는 피연산자의 순서도 결과값에
            # 지대한 영향을 미치기 때문에
            # n2 n1값으로 따로 저장해서 연산한 뒤
            # 스택에 저장
            elif i == '-':
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                new = n1 - n2
                stack.append(new)
            # 곱하기
            elif i == '*':
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                new = n1 * n2
                stack.append(new)
            # 나누기
            elif i == '/':
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                new = n1 // n2
                stack.append(new)
    # 연산이 다 제대로 마무리 되면
    # 스택의 맨 마지막 요소는 .일 것이고
    # . 아래에 숫자 하나만 들어있을 것임
    # 그 경우가 아니라면 뭔가 잘못되었다는 뜻이므로
    # 그냥 result를 출력하면
    # error가 출력됨
    # 제대로 연산이 되었을 경우
    # result에 연산 결과가 들어갈 것임
    if stack[-1] == '.':
        stack.pop()
        if len(stack) == 1:
            result = stack.pop()

    print(f'#{tc} {result}')




