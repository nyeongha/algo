import sys

ar = {}
for x in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    if a not in ar:
        ar[a] = 1
    else:
        ar[a] += 1
for sar in sorted(ar.items()):
    for i in range(sar[1]):
        print(sar[0])


