import sys; sys.stdin = open('sample_input.txt')

T = int(input())

# 브루트포스 함수 정의
def BruteForce(p, t):
    i = 0
    j = 0
    # i는 텍스트의 인덱스, j는 패턴의 인덱스
    # i는 텍스트의 길이보다 작을때에만,
    # j는 패턴의 길이보다 작을때에만 반복
    while i < len(t) and j < len(p):
        # 텍스트의 i번째 요소가 패턴의 j번째 요소와 같지 않을 경우
        # = 찾는 패턴이 아닐 경우
        if str2[i] != str1[j]:
            # i는 탐색하기 전으로 돌아감
            i = i - j
            # j에 -1을 할당, 왜냐면
            # 뒤에서 j에 j+1을 할당해줄건데
            # 그때 j는 원점(0)이 되어야 하니까
            j = -1
        # 다음 탐색 시작점으로 이동
        i = i + 1
        j = j + 1
    # 패턴이 텍스트에 있다면, j는 -1로 초기화 되지 않고
    # 계속해서 증가할 것임
    # j가 패턴의 길이와 같아진다면
    # 텍스트 안에 패턴이 있는 것
    if j == len(p):
        return 1
    else:
        return 0

for tc in range(T):
    str1 = input()
    str2 = input()
    result = BruteForce(str1, str2)
    print(f'#{tc+1} {result}')

