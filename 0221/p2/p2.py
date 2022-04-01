import sys
sys.stdin = open('input.txt')

class Stack:
    def __init__(self, arr):
        self.arr = arr
        self.top = -1

    def push(self, n):
        self.top += 1
        self.arr[self.top] = n

    def pop(self):
        self.top -= 1
        return self.arr[self.top+1]

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def peek(self):
        return self.arr[self.top]


T = int(input())

for tc in range(1, T+1):
    data = input()

    stack = Stack([0]*len(data))
    result = -1
    for i in range(len(data)):
        if stack.top == -1 and data[i] == '(':
            stack.push('(')
        elif data[i] == '(':
            stack.push('(')
        elif data[i] == ')':
            if stack.peek() == '(':
                stack.pop()
            else:
                break
        else:
            break
    else:
        if stack.is_empty():
            result = 1

    print('#{} {}'.format(tc, result))


