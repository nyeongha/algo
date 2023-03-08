import sys
k, n = map(int, sys.stdin.readline().split())
ll = []
for i in range(k):
    ll.append(int(sys.stdin.readline().strip()))
start=1
end=max(ll)
cnt=0
while start<=end:
    cnt=0
    mid = (start + end) // 2
    for i in ll:
        cnt+=(i//mid)
    if cnt<n:
        end=mid-1
    else:
        start=mid+1
print(end)


