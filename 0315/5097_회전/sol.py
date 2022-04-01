import sys; sys.stdin = open('input.txt')

T = int(input())

front = -1
rear = -1

for tc in range(1, T+1):
    N, M = int(input().split())
    Q = [0] * N
    for n in range(N):
        enQ(input())


def enQ(item):
    global rear
    rear = rear + 1
    Q[rear] = item


def deQ():
    global front
    front = front + 1
    return Q[front]