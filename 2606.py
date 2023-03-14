import sys

dic=[]
n=int(sys.stdin.readline())
visited= [0] * (n + 1)

for i in range(n+1):
    dic.append([])

for i in range(int(sys.stdin.readline())):
    a,b=map(int,sys.stdin.readline().split())
    dic[a].append(b)
    dic[b].append(a)

def dfs(num):
    visited[num] = 1
    for i in dic[num]:
        if visited[i]==0:
            dfs(i)

dfs(1)
print(sum(visited)-1)







