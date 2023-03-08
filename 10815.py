import sys

sys.stdin.readline()
a=set(sys.stdin.readline().split())
sys.stdin.readline()
b=list(sys.stdin.readline().split())

t=[1 if (i in a) else 0 for i in b]
print(*t)