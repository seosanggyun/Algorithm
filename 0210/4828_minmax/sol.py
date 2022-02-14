import sys

sys.stdin = open('input.txt')

# 리스트로 받은 양수들의
# 최솟값과 최댓값을 찾은 뒤
# 최댓값에서 최솟값을 뺀 값을 출력

# 테스트 케이스의 수 입력
T = int(input())

# 테스트 케이스의 수 만큼 반복
for tc in range(T):
    # 케이스의 첫 줄에 양수의 개수 N 입력받음
    N = int(input())
    # 케이스의 둘째 줄에 양수들 리스트로 입력받음
    ai = list(map(int, input().split()))
    # 리스트의 최솟값과 최댓값을
    # 리스트의 첫번째 요소로 초기화
    ai_min = ai[0]
    ai_max = ai[0]
    # 양수의 개수 만큼 반복
    for i in range(N):
        # ai의 i번째 요소가 ai_min 보다 작다면
        # i번째 요소를 ai_min에 저장
        if ai_min > ai[i]:
            ai_min = ai[i]
        # ai의 i번재 요소가 ai_max 보다 크다면
        # i번째 요소를 ai_max에 저장
        if ai_max < ai[i]:
            ai_max = ai[i]
    # result 값 저장 후 형식에 맞게 출력
    result = ai_max - ai_min
    print(f'#{tc+1} {result}')

