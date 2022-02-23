import sys; sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    # 문자열 입력받음
    letter = input()

    # 스택 비어있는 리스트로 초기화
    stack = []

    # top 0으로 초기화
    top = 0

    # 문자열 순회하면서
    for i in letter:
        # 스택이 비어 있으면
        if len(stack) == 0:
            # 스택에 i번째 요소 추가
            stack.append(i)
        # 스택이 비어있지 않다면
        else:
            # 그리고 스택의 맨 위 요소가
            # 추가하고자 하는 문자열과 같다면
            if stack[-1] == i:
                # 스택에서 제거
                stack.pop()
            # 스택의 맨 위 요소가
            # 추가하고자 하는 문자열과 다르다면
            else:
                # 스택에 추가
                stack.append(i)
    print(f'#{tc} {len(stack)}')





