import sys
from collections import deque
input = sys.stdin.readline



def solution():
    deque: deque=([])

    for _ in range(int(input())):
        
        x= input().split()
        if x[0] == 'push_front':
            deque.insert(0, x[1])
        elif x[0] == 'push_back':
            deque.append(x[1])
        elif x[0] == 'pop_front':
            print(deque.pop(0) if deque else -1)
        elif x[0] == 'pop_back':
            print(deque.pop() if deque else -1)
        elif x[0] == 'size':
            print(len(deque))
        elif x[0] == 'empty':
            print(0 if deque else 1)
        elif x[0] == 'front':
            print(deque[0] if deque else -1)
        elif x[0] == 'back':
            print(deque[-1] if deque else -1)


solution()
