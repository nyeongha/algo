# 수빈이가 있는 위치 N
# 동생이 있는 위치 K
# 수빈이는 동생과 숨바꼭질을 하고 있다.
# 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
# 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
# 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.
#
# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
# (0 ≤ N ≤ 100,000)
# 5 17

from collections import deque

N,K=map(int,input().split())
count=[-1 for _ in range(100002)]

# def bfs():
#     q=deque([N])
#     visit[N]=1
#     while q:
#         x=q.popleft()

#         if x==K:
#             return print(visit[K]-1)

#         if 0<=2*x<=100000 and visit[2*x]==0:
#             visit[2*x]=visit[x]
#             q.append(2*x)

#         for i in [x-1,x+1]:
#             if 0<=i<=100000 and visit[i]==0:
#                 visit[i]=visit[x]+1
#                 q.append(i)
#
# bfs()

def bfs():
    q=deque([N])
    count[N] = 0
    while True:
        x = q.popleft()
        if x==K:
            return print(count[x])
            break
        for n,i in enumerate([2*x,x-1,x+1]):
            if 0<=i<100001:
                if n==0 and count[i]==-1:
                    count[i]=count[x]
                    q.append(i)
                elif (n==1 or n==2) and count[i]==-1:
                    count[i]=count[x]+1
                    q.append(i)



bfs()

