from collections import deque
d=deque()
for i in range(1,int(input())+1):
    d.append(i)
while len(d)!=1:
    d.popleft()
    k=d.popleft()
    d.append(k)
print(d.pop())
