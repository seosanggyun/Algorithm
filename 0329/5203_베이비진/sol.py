import sys;

sys.stdin = open('sample_input.txt')
from pprint import pprint


def is_babygin(deck):                                       # babygin 판별 함수
    flag = 0                                                # flag에 0 할당
    count = [0 for _ in range(10)]                          # 카운트정렬처럼 카운트배열 초기화
    for i in deck:                                          # 카드 배열의 카드를 순회
        count[i] += 1                                       # 카드 번호에 해당하는 count배열의 인덱스에 +1
                                                            # 이러면 무슨 카드가 몇개 있는지 알 수 있음

    for i in range(8):                                                  # run 판별, 7까지 조회해야 789일경우 조회 가능
        if count[i] > 0 and count[i + 1] > 0 and count[i + 2] > 0:      # 연속해서 세개의 숫자가 있는 경우
            flag = 1                                                    # flag에 1 할당

    if 3 in count:                                                      # triplet 판별
        flag = 1                                                        # 카운트 배열에 3이 있으면 같은 카드가 3장 있다는 뜻
                                                                        # flag에 1 할당

    return flag


T = int(input())

for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    p1 = []
    p2 = []
    winner = 0
    for i in range(len(cards)):                         # 카드배열을 돌면서
        if i % 2 == 0:                                  # 짝수번째 인덱스의 카드는
            p1.append(cards[i])                         # player 1에게
            # print(p1)
            if is_babygin(p1):                          # player 1 babygin 판별
                winner = 1                              # babygin이면 for문 중지
                break
        else:
            p2.append(cards[i])                         # player 2도 마찬가지
            # print(p2)
            if is_babygin(p2):
                winner = 2
                break

    print(f'#{tc} {winner}')                            # 비겼을때는 winner 값이 안바뀌므로 0 출력
