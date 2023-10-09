n,s=map(int,input().split())
p_val=list(map(int,input().split()))


visit=[0 for i in range(n)]
stack=[]

sum=0
sum_stack=[]
def dfs(p_val,s):
    for i in p_val:
        for j in p_val:
            if not visit[j]:
                sum+=i
                sum_stack.append(sum)
                print(sum_stack)

dfs(p_val,s)