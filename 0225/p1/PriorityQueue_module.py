from queue import PriorityQueue

q = PriorityQueue()

q.put(8)
q.put(4)
q.put(6)
q.put(9)
q.put(2)

print(q.queue)
print(q.qsize())
print(q.get())

print(help(PriorityQueue))