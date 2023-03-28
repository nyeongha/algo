# import sys


# input=sys.stdin.readline


# L,C=map(int, input().split())
# CL=list(map(str,input().split()))

# CL.sort()
# m=["a", "e", "i", "o", "u"]

# s=[]
# ss=[]
# visit={i:0 for i in CL}

# def bt():
#     if len(s)==L:
#         k=sorted(s)
#         t=k
#         if k not in ss:
#             cnt=0
#             for a in k:
#                 if a in m:
#                     cnt+=1
#             if len(k)>=2 and cnt>=1:
#                 ss.append(t)
#         return
    

#     for i in CL:
#         if visit[i]==0:
#             s.append(i)
#             visit[i]=1
#             bt()
#             s.pop()
#             visit[i]=0


# bt()
# for i in ss:
#     print(*i)




from itertools import combinations
import sys
input=sys.stdin.readline


L,C=map(int, input().split())
CL=list(map(str,input().split()))

CL.sort()
m=["a", "e", "i", "o", "u"]

a=list(combinations(CL, L))

ss=[]

def bt(a):
    for i in a:
        cnt=0
        i=list(i)
        k=list(i)
        for j in k:
            if j in m:
                i.pop(i.index(j))
                cnt+=1
        if len(i)>=2 and cnt>=1:
            ss.append(k)
        


bt(a)
for i in ss:
    for k in i:
        print(k,end='')
    print(end="\n")