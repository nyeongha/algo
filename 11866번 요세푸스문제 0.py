from collections import deque
m,n=map(int,input().split())
d=deque()
k2=[]
for i in range(1,m+1):
    d.append(i)

for i in range(m):
    for x in range(n-1):
        k1=d.popleft()
        d.append(k1)
    k2.append(d.popleft())
print('<{0}>'.format(", ".join(map(str,k2))))
