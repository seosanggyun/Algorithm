from queue import Queue
# 언제 쓰는거냐면
# 주로 멀티스레드 프로그래밍

q = Queue()

# 삽입
q.put('A')
q.put('B')
q.put('C')

# queue의 내용물
print(q.queue)
print(q.qsize())

# 조회 및 반환
print(q.get())
print(q.get())
print(q.get())

# print(help(Queue))
q = Queue(3)
q.put('A')
q.put('B')
q.put('C')
q.put('D')
print('멈췄니?')