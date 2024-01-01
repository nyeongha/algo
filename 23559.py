from heapq import heappush, heappop
import sys
input = sys.stdin.readline

Ah=[]


N,X=map(int,input().split())    #N일동안 X원 만큼 사용가능

sum=0   #맛

for i in range(N):
    A,B=map(int,input().split())
    heappush(Ah,(-(A-B),A-B)) #최대힙
    sum+=B
X-=N*1000

while X>=4000 and Ah[0][1]>0:
    sum+=heappop(Ah)[1]
    X-=4000
print(sum)







