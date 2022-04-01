import sys; sys.stdin = open('input.txt')

# 내가 가진 문자열 bit로부터
# 비교 대상인 password를 
# 어디에? 담아서 어떻게? 대조 할 것인가
password = {
    '001101' : 0,
    '010011' : 1,
    '111011' : 2,
    '110001' : 3,
    '100011' : 4,
    '110111' : 5,
    '001011' : 6,
    '111101' : 7,
    '011001' : 8,
    '101111' : 9
}


T = int(input())

for tc in range(1,T+1):
    arr = input()
    print(arr)

    # 전체를 4bit 2진수로 바꾼 값들을 모아둘 문자열

    bit = ''

    # 입력 받은 16진수 하나하나 순회해서 변경해 나갈 것임

    for i in range(len(arr)):
        # 각 값을 10진수로 먼저 바꿔야 함
        # print(int(arr[i], 16))
        tmp = int(arr[i], 16)

        # 10진수를 다시 2진수로 바꿔
        # 바뀐 tmp에 들어있는 값 == 0
        # 내가 바꿔야 하는 2진수 0 == 0000
        tmp = bin(tmp).replace('0b', '')

        # print(f'{tmp:04b}')
        # 이렇게도 됨


        # print(tmp)

        # 길이가 4인 2진수가 필요함
        while len(tmp) != 4:
            tmp = '0' + tmp
        # print(tmp)

        bit += tmp

    # print(bit)

    # 뒤에서 1 찾기
    for i in range(len(bit)-1, -1, -1):
        if bit[i] == '1':
            point = i
            break

    # 최종 출력 값
    result = ''

    while point - 6 > 0:
        if bit[point-5:point+1] in password:
            # 원래는 그냥 출력을 해버리고 싶은데
            # 뒤에서부터 조사중이라
            # 반대로 나옴

            # 그래서 뒷 번호부터 더해 나가려면...
            # 최종 모양은 0 2

            # ' ' + 2 + result
            # ' ' + 0 + ' 2'
            # ' 0 2'

            result = ' ' + str(password[bit[point-5:point+1]]) + result
            # print(password[bit[point-5:point+1]], end= '')

            # 패턴 찾았으니까 다음 패턴 조사
            # 문제 조건 중에 암호패턴이 연속되어있다고 했으니
            # 6글자 앞에 무조건 암호가 있을거임
            point -= 6
        else:
            # 못 찾은 상황에 대해서 다른 조건들
            # 더 만들어서 처리할 수도 있을 거임
            point -= 1

    print(result)
    print(result.lstrip())

