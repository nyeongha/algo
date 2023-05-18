from collections import deque


A,B=map(int,input().split())


ll=list(str(A))

visit=[False for _ in range(10)]



stack=[]
sy=[]

def back_t():
    if len(sy)==len(ll):
        a=''.join(sy)
        if len(a.lstrip("0")) ==len(ll):
            stack.append(int(a))
        
    for i in range(len(ll)):
        ll[i]=int(ll[i])
        if not visit[i]:
            visit[i]=True
            sy.append(str(ll[i]))
            back_t()
            sy.pop()
            visit[i]=False


back_t()
for mx in sorted(stack,reverse=True):
    if mx<B:
        print(mx)
        exit()
print(-1)

