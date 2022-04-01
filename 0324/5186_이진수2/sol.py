import sys; sys.stdin = open('sample_input.txt')

T = int(input())

# 이진수로 만드는 함수

def binary(N):
    # 카운트가 12가 넘으면 overflow 출력을 위해
    # 카운트값 초기화
    count = 0

    # 결과값
    result = ''

    # 자릿수
    jaritsoo = 1

    # N이 0이 아닐때에만 while문 반복
    while N:
        # 예를들어 0.625의 경우
        # 2**-1, 즉 0.5보다 크므로
        # result에 1을 추가하고
        # 0.625에서 0.5를 뺀
        # 0.125로 다시 계산

        # 0.125는
        # 2**-2, 즉 0.25보다 작으므로
        # result에 0을 추가하고
        # 다음 단계로 넘어감

        if N < 2**-jaritsoo:
            result += '0'
        else:
            N -= 2**-jaritsoo
            result += '1'

        # 한번 계산 했으니 카운트에 1 더해줌
        count += 1

        # 카운트가 12를 초과할 때 overflow 반환
        if count > 12:
            return 'overflow'

        # 카운트가 12 초과 하지 않을 경우 자릿수 +1
        else:
            jaritsoo += 1

    # 결과 반환
    return result



for tc in range(1,T+1):
    N = float(input())
    print(f'#{tc} {binary(N)}')

