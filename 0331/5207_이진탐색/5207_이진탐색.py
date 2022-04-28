import sys
sys.stdin = open('input.txt')

def binary_search(L, R, T, direction):
    global cnt
    # 중간값
    mid = (L + R)//2
    # 타겟을 찾으면
    if T == A[mid]:
        cnt += 1
        return 
    # 타겟이 중간보다 크면
    elif T > A[mid]:
        # 이전 조사도 오른쪽이면 조사 종료
        if direction == 'RIGHT':
            return
        # 오른쪽 조사
        binary_search(mid+1, R, T, 'RIGHT')
    elif T < A[mid]:
        if direction == 'LEFT':
            return
        binary_search(L, mid-1, T, 'LEFT')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N개와 M개의 백만 이하의 양의 정수 -> A는 정렬
    A = sorted(list(map(int,input().split())))
    B = list(map(int, input().split()))

    # 최종결과
    cnt = 0

    # B의 모든 목록 대상 조사
    for i in range(M):
        # 왼쪽, 오른쪽, 타겟, 방향
        binary_search(0, N-1, B[i], 'START')
    print(f'#{tc} {cnt}')