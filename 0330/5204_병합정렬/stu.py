import sys
sys.stdin = open('input.txt')

def mergesort(arr):
    global cnt
    if len(arr) == 1 :
        return arr
    left = arr[0:len(arr)//2]
    right = arr[len(arr)//2:len(arr)]
    s_left = mergesort(left)
    s_right = mergesort(right)
    if s_left[-1] > s_right[-1] :
        cnt += 1
    m_arr = []

    while len(s_left) != 0 and len(s_right) != 0 :
        if s_left[0] <= s_right[0] :
            m_arr.append(s_left.pop(0))
        else :
            m_arr.append(s_right.pop(0))
    if len(s_left) != 0 and len(s_right) == 0 :
        m_arr.extend(s_left)
    elif len(s_left) == 0 and len(s_right) != 0:
        m_arr.extend(s_right)
    return m_arr


tc = int(input())

for t in range(tc):
    n = int(input())
    arr = list(map(int ,input().split()))
    cnt = 0
    new_arr = mergesort(arr)
    print(f'#{t+1} {new_arr[n//2]} {cnt}')