q = []

my_chu = 20

next_person  = 1
q.append([1, 1])
print(q)
while 1:
    idx, num = q.pop(0)
    my_chu -= num 
    q.append([idx,num+1])
    next_person += 1
    q.append([next_person,1])
    

    # 엔터 칠때마다 정보 출력
    input()
    print("큐에 있는 사람 수 ", len(q))
    print("현재 나눠주는 사탕 수", num)
    print("현재까지 나눠 준 사탕 수", 20-my_chu)
    print(q, my_chu)

    if my_chu <= 0:
        break