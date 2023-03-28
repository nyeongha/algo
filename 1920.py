import sys

num_n=sys.stdin.readline()
n=set(sys.stdin.readline().split())
num_m=sys.stdin.readline()
m=list(sys.stdin.readline().split())

for i in m:
    print(1 if i in n else 0)
