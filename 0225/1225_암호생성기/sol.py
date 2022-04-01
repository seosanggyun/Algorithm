import sys; sys.stdin = open('input.txt')


T = int(input())
Q = list(map(int, input().split()))
front = -1
rear = 7


def enQ(item):
    global rear
    rear += 1
    Q[rear] = item


def deQ():
    global front
    front += 1
    return Q[front]