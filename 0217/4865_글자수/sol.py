import sys; sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(T):
    # str1 문자열에 포함된 글자들이 str2에 몇 개씩 들어있는지
    # 알아봐야 하므로
    # str1은 알파벳 하나하나 떨어뜨려서 조회할 수 있게
    # 리스트로 받아줌
    str1 = list(input())
    str2 = input()
    # str1의 알파벳 별로 카운트를 저장할 딕셔너리 초기화
    dic = {}
    # 딕셔너리의 밸류(카운트)들을 담을 리스트 초기화
    result = []
    # 딕셔너리의 밸류(카운트)들 중 최댓값을 저장할 변수 초기화
    max_count = 0

    # str1 리스트 순회
    for i in range(len(str1)):
        # 카운트 초기화
        count = 0
        # str2 문자열 순회
        for j in str2:
            # 만약에 str1 리스트의 1번째 요소(알파벳)가
            # str2 문자열에 존재한다면
            if str1[i] == j:
                # 카운트 +1
                count += 1
            # 딕셔너리에 str1 리스트의 요소 별 카운트 저장
            dic[str1[i]] = count
    # result 리스트에 딕셔너리의 밸류들을 저장
    result = dic.values()
    # result 리스트 요소 중 최댓값 찾기
    for j in result:
        if j > max_count:
            max_count = j
    # 출력
    print(f'#{tc+1} {max_count}')



