from collections import deque
from pprint import pprint

q = deque()
pprint(dir(q))

q.append('A')
q.append('B')
print(q)
q.appendleft('C')
print(q)
print(q.popleft())
# print(q.pop())

print(q.pop(1))