import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 몇 번째 피자인지 알아야 하므로 enumerate
    ci = [[idx+1, item] for idx, item in enumerate(list(map(int, input().split())))]

    # 오븐에 피자 넣기
    oven = []
    # 오븐의 크기만큼 반복
    for i in range(N):
        # 순서대로 넣어야 하므로 0번째 피자를 빼서 넣는다.
        oven.append(ci.pop(0))

    # 오븐에 마지막 피자가 남을때 까지 반복
    while len(oven) != 1:
        # 소요 시간 절반으로 만들기
        oven[0][1] = oven[0][1]//2

        # 치즈가 다 녹지 않았다면, 맨 뒤로
        if oven[0][1] != 0:
            oven.append(oven.pop(0))
        # 치즈가 다 녹았다면, 피자를 빼고,
        else:
            oven.pop(0)
            # 남아 있는 피자가 있다면 오븐에 추가
            if len(ci) != 0:
                oven.append(ci.pop(0))


    print(f'#{tc} {oven[0][0]}')