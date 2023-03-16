import sys

n=(str(sys.stdin.readline().strip()))
visited=[0]*len(n)
s=[]
y=[]

def dfs():
    if len(n)==len(s):
        y.append(int(''.join(s)))
        return

    for i in range(len(n)):
        if visited[i]==0:
            s.append(n[i])
            visited[i]=1
            dfs()
            s.pop()
            visited[i]=0

dfs()
y.sort()
for x in y:
    if x > int(n):
        print(x)
        break;
    if x==y[-1]:
        print(0)
        break;

