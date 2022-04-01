import sys; sys.stdin = open('11315.txt')
dr = [0, 1, 1, 1]
dc = [1, 1, 0, -1]

def check():
    for r in range(N):
        for c in range(N):
            if arr[r][c] == '.':
                continue
            # 돌을 만났다. 기준점 = (r, c)
            for i in range(4):
                nr, nc = r, c
                for _ in range(4):
                    nr = nr + dr[i]
                    nc = nc + dc[i]
                    if nr < 0 or nr >= N or nc < 0 or nc >= N or arr[nr][nc] == '.':
                        break
                else:
                    return 'YES'
    return 'NO'

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]

    print(f'#{tc} {check()}')
