class Queue:

    # createQueue
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.rear = -1
        self.front = -1

    def enQueue(self, el):
        if self.isFull():
            # 여러가지 해결방법
            # 1. queue의 크기를 늘린다.
            # 2. 또다른 예외처리
            print('Queue is Full!!')
        else:
            self.rear += 1
            self.items[self.rear] = el

    def deQueue(self):
        if self.isEmpty():
            print('Queue is Empty!!')
        else:
            self.front += 1
            return self.items[self.front]

    def isEmpty(self):
        # 선형 큐에서 큐가 비어 있다는 뜻
        return self.rear == self.front

    def isFull(self):
        return self.rear == self.size - 1

    def QPeek(self):
        return self.items[self.front]

q = Queue(3)
print('='*10, '최초 생성시 비어있는지', '='*10)
print(q.isEmpty())

print('='*10, '값 최초 삽입', '='*10)
q.enQueue('A')
print(q.front, q.rear, q.items)

print('='*10, '값 최초 삭제', '='*10)
print(q.deQueue())
print(q.front, q.rear, q.items)
print(q.isEmpty())

print('='*10, '포화상태 확인', '='*10)
q.enQueue('B')
q.enQueue('C')
print(q.front, q.rear, q.items)
print(q.isFull())

q.enQueue('D')
print('='*10, '포화상태 재확인', '='*10)
print(q.deQueue())
print(q.front, q.rear, q.items)
print('='*10, 'D 재삽입', '='*10)
q.enQueue('D')
print(q.front, q.rear, q.items)
