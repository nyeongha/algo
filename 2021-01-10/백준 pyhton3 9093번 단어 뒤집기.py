import sys
for _ in range(int(sys.stdin.readline())):
    a=list(sys.stdin.readline().split())
    for _ in a:
        print(_[::-1],end=' ')