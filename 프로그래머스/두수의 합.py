import sys

n = int(sys.stdin.readline())
a_list=list(map(int,sys.stdin.readline().split()))
xx = int(sys.stdin.readline())

cnt=0
a_list.sort()

start=0
end=n-1
while start<end:
    t=a_list[start]+a_list[end]
    if t<xx:
        start+=1
    elif t==xx:
        cnt+=1
        end-=1
    elif t>xx:
        end-=1

print(cnt)


