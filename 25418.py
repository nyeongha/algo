from collections import deque
A,K=map(int,input().split())
kl=[0 for i in range(K+1)]

dq=deque([(A+1,1),(A*2,1)])

while dq:
    x,y=dq.popleft()
    if(x==K):
        print(y)
        break
    if(x+1<=K and not kl[x+1]):
        dq.append((x+1,y+1))
        kl[x+1]=1
        if(x+1==K):
            print(y+1)
            break
    if(x*2<=K and not kl[x*2]):
        dq.append((x*2,y+1))
        kl[x*2]=1
        if(x*2==K):
            print(y+1)
            break

