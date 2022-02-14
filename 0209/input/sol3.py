'''
입력 받은 2차원 리스트의
(1,1) 좌표의 값을 출력하시오
'''

import sys
sys.stdin = open('sol3.txt')

'''
0 1 2 => [0, 1, 2]
3 4 5 => [3, 4, 5]

'''

'''
[[0, 1, 2], [3, 4, 5]...]
'''

N = int(input())
result = []
for _ in range(N):
    row = list(map(int, input().split())) # 0 1 2
    print(row)
    result.append(row)
print(result)
print(f'# {result[1][1]}')
