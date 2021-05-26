import sys
import itertools
a,b=map(int,sys.stdin.readline().split())
event=itertools.combinations_with_replacement(range(1,a+1), b)
for x in event:
    print(*x)
