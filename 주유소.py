import sys
from collections import deque
n=int(sys.stdin.readline())
distance=list(map(int,sys.stdin.readline().split()))
city_cost=list(map(int,sys.stdin.readline().split()))

dq=deque([])
for a,b in zip(city_cost,distance):
    dq.append((a,b))

sum=0
while dq:
    m=min(dq)[0]
    a,b=dq.pop()
    sum+=m*b

print(sum)

# 7
# 2 3 1 1 2 3
# 5 2 4 4 2 2 4

