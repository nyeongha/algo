import sys


ll = []
cnt=0
k, n = map(int, sys.stdin.readline().split())
for i in range(k):
    ll.append(int(sys.stdin.readline().strip()))
start=1
end=min(ll)
while (start <= end):
    mid = (start + end) // 2
    cnt = sum([x // mid for x in ll])

    if cnt >= n:
        start = mid + 1  # 자른개수가 많으면 더 크게 잘라야함
    else:
        end = mid - 1
print(end)


