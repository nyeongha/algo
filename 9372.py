from collections import deque
def dfs():
    cnt=0
    d=deque()
    d.append(1)
    while d:
        cnt+=1
        a=d.pop()
        for i in t[a]:
            d.append(i)
    return cnt-1   
            
            
            
            
     
for i in range(int(input())):
    m,n=map(int,input().split())
    t=dict()
    for j in range(n):
        a,b=map(int,input().split())
        if a in t:
            t[a].append(b)
        else:t[a]=[b]
        if b in t:
            t[b].append(a)
        else:t[b]=[a]
    print(dfs())
