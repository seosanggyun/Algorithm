def process_solution(a, k, sum):
    global cnt

    for i in range(1, k + 1):
        if a[i]: 
            print(data[i], end=" ")
    print()
    cnt += 1



def construct_candidates(a, k, input, c):
    in_perm = [False] * NMAX

    for i in range(1, k):
        # 앞부분에서 사용된적이 있으면 True 로 체크
        in_perm[a[i]] = True
    ncandidates = 0
    for i in range(1, input + 1):
        # 사용된적이 없는 요소들을 기준으로 확인
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    print(c)
    return ncandidates

# a: 해당 원소를 사용 할 것(o) / 안할 것(x) 여부
# k: index
# input:
def backtrack(a, k, input):
    global total_cnt

    c = [0] * MAXCANDIDATES
    
    if k == input:
        for i in range(1, k+1):
            print(a[i], end= ' ')
        print()
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)

MAXCANDIDATES = 6
NMAX = 6
data = [range(10)]
a = [0] * NMAX
cnt = 0
total_cnt = 0
backtrack(a, 0, 5)
