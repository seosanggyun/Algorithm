q = []

my_chu = 20

next_person  = 1
# 1번이 줄을 선다
q.append([1, 1])
print(q)

while 1:
    # n번이 마이쮸를 받는다
    idx, num = q.pop(0)
    my_chu -= num 
    # n번이 다시 줄을 선다
    q.append([idx,num+1])
    next_person += 1
    # 새로이 next_person번이 들어와 줄을 선다
    q.append([next_person,1])
    print(q, my_chu)

    if my_chu <= 0:
        break