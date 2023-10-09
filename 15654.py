# N개의 자연수 중에서 M개를 고른 수열

import sys
sys.setrecursionlimit(1000000000)


N,M=map(int,input().split())

N_list=list(map(int,input().split()))
visit=[0 for _ in range(N)]


N_list.sort()
stack=[]
def dfs():
    if len(stack)==M:
        print(*stack)
    for i in range(N):
        if not visit[i]:
            stack.append(N_list[i])
            visit[i]=1
            dfs()
            stack.pop()
            visit[i]=0


dfs()