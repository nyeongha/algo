import sys
pd={1:1,2:1,3:1}
def pado(n):
    for x in range(4,n+1):
        pd[x]=pd[x-2]+pd[x-3]
    return pd[n]
for y in range(int(sys.stdin.readline())):
    print(pado(int(sys.stdin.readline())))