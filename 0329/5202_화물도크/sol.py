import sys;

sys.stdin = open('sample_input.txt')
from pprint import pprint

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    time_table = [0 for _ in range(24)]     # 시간표
    a_form = []                             # 신청서를 담을 리스트
    result = 0                              # 결과값 초기화
    for n in range(1, N + 1):
        s, e = map(int, input().split())    # s, e를 입력받음
        # print(s, e)
        a_form.append((e - s, s, e, n))     # 신청서에 (소요시간, 시작시간, 종료시간, 신청서번호)로 저장

    a_form.sort()                           # 최대한 많은 수의 화물차가 작업해야 하니까 신청서의 소요시간 순서대로 정렬
    # print(a_form)

    for form in a_form:                         # 신청서를 하나씩 보면서
        flag = 1                                # flag는 시간표 조사해보고
                                                # 겹치는 시간이 있으면 시간표에 못적도록 하기 위함

        for a_time in range(form[1], form[2]):  # 신청서의 시작시간부터 종료시간까지 모두 조사해서
            if time_table[a_time] != 0:         # 시간표의 시간이랑 하나라도 겹칠 경우
                flag = 0                        # flag를 0으로

        if flag == 1:                                   # flag가 1이라면 == 겹치는 시간이 없다면
            for r_a_time in range(form[1], form[2]):    # 신청서의 시작시간부터 종료시간까지
                time_table[r_a_time] = form[3]          # 시간표에 기재
            # print(time_table)
    # print(hour)
    for i in range(len(time_table)):              # 시간표를 조사해서
        if time_table[i] == 0:                    # 0일때는 넘기고
            continue
        else:                                           # 0이 아닌 숫자 종류의 갯수를 세면
            if time_table[i-1] != time_table[i]:        # 화물차의 수를 셀 수 있음
                result += 1

    print(f'#{tc} {result}')
