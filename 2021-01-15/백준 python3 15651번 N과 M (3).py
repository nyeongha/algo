import sys
import itertools
a,b=map(int,sys.stdin.readline().split())
event = list(itertools.product(range(1,a+1), repeat=b))
for x in event:
    print(*x)