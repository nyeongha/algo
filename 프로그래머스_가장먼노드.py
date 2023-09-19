from collections import deque
def solution(n, edge):
    sl=[[] for i in range(n+1)]
    for a,b in edge:
        sl[a].append(b)
        sl[b].append(a)
    print(sl)

    q=deque([1])
    ck=[0 for i in range(n+1)]
    ck[1]=1
    while q:
        x=q.popleft()
        for i in sl[x]:
            if not ck[i]:
                q.append(i)
                ck[i]=ck[x]+1
    answer=ck.count(max(ck))
    return answer