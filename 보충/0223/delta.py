# N = 10
# arr = [[0] * N for _ in range(N)]
# dr = [0, 1, 0, -1]  # 우 하 좌 상
# dc = [1, 0, -1, 0]
# r = c = 5
# for i in range(4):
#     nr = r + dr[i]
#     nc = c + dc[i]
#     arr[nr][nc] = i + 1
#
# for lst in arr:
#     print(*lst)
#=======================================
# 모든 위치에 대해서 적용
# N = 10
# arr = [[0] * N for _ in range(N)]
# dr = [0, 1, 0, -1]  # 우 하 좌 상
# dc = [1, 0, -1, 0]
#
# for r in range(N):
#     for c in range(N):
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             # 중요!!! 범위 체크가 필요하다.
#             if 0 <= nr < N and 0 <= nc < N:
#                 arr[nr][nc] = i + 1
#
#             if nr < 0 or nr == N or nc < 0 or nc == N:
#                 continue
#             arr[nr][nc] = i + 1
#
# for lst in arr:
#     print(*lst)
# ====================================
# 반복해서 적용
# N = 10
# arr = [[0] * N for _ in range(N)]
# r = c = 7
#
# # 우
# for i in range(c + 1, N):
#     arr[r][i] = 1
# # 하
# for i in range(r + 1, N):
#     arr[i][c] = 2
# # 좌
# for i in range(c - 1, -1, -1):
#     arr[r][i] = 3
# # 상
# for i in range(r - 1, -1, -1):
#     arr[i][c] = 4
#
# for lst in arr:
#     print(*lst)
# ======================================
# 원하는 만큼 반복
# N = 10
# arr = [[0] * N for _ in range(N)]
# r = c = 7
# k = 5
# # 우
# for i in range(c + 1, c + k):
#     if i >= N:
#         break
#     arr[r][i] = 1
# # 하
# for i in range(r + 1, r + k):
#     if i >= N:
#         break
#     arr[i][c] = 2
# # 좌
# for i in range(c - 1, c - k, -1):
#     if i < 0:
#         break
#     arr[r][i] = 3
# # 상
# for i in range(r - 1, r - k, -1):
#     if i < 0:
#         break
#     arr[i][c] = 4
#
# for lst in arr:
#     print(*lst)
# ===========================
# delta 반복해서 적용 N = 10
# N = 10
# arr = [[0] * N for _ in range(N)]
# dr = [0, 1, 0, -1]  # 우 하 좌 상
# dc = [1, 0, -1, 0]
# r = c = 7
#
# for i in range(4):
#     nr = r
#     nc = c
#     while True:
#         nr = nr + dr[i]
#         nc = nc + dc[i]
#         if nr < 0 or nr >= N or nc < 0 or nc >= N:
#             break
#         arr[nr][nc] = i + 1
#
# for lst in arr:
#     print(*lst)
#
# N = 10
# arr = [[0] * N for _ in range(N)]
# dr = [0, 1, 0, -1]  # 우 하 좌 상
# dc = [1, 0, -1, 0]
# r = c = 7
#
# for i in range(4):
#     nr = r + dr[i]
#     nc = c + dc[i]
#     while 0 <= nr < N and 0 <= nc < N:
#         arr[nr][nc] = i + 1
#         nr = nr + dr[i]
#         nc = nc + dc[i]
#
# for lst in arr:
#     print(*lst)
# ===========================================
# delta 를 원하는 만큼 반복
# N = 10
# arr = [[0] * N for _ in range(N)]
# dr = [0, 1, 0, -1]  # 우 하 좌 상
# dc = [1, 0, -1, 0]
# r = c = 7
# k = 4
# for i in range(4):
#     nr = r + dr[i]
#     nc = c + dc[i]
#     cnt = 0
#     while 0 <= nr < N and 0 <= nc < N and cnt < k:
#         arr[nr][nc] = i + 1
#         nr = nr + dr[i]
#         nc = nc + dc[i]
#         cnt += 1
#
# for lst in arr:
#     print(*lst)

# delta 반복 - for문으로
N = 10
arr = [[0] * N for _ in range(N)]
dr = [0, 1, 0, -1]  # 우 하 좌 상
dc = [1, 0, -1, 0]
r = c = 7
k = 4
for i in range(4):
    nr = r
    nc = c
    for _ in range(k):
        nr = nr + dr[i]
        nc = nc + dc[i]
        if nr < 0 or nr == N or nc < 0 or nc == N:
            break
        arr[nr][nc] = i + 1


for lst in arr:
    print(*lst)