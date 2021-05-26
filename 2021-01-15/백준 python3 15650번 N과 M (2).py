import sys
import itertools
a,b=map(int,sys.stdin.readline().split())
event=list(itertools.combinations(range(1,a+1), b))
for x in event:
    print(*x)