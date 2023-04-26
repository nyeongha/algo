
import sys

l=[1,5,10,50]
n=int(sys.stdin.readline().strip())
v=[0]*4
s=[]
t=[]

def dfs():
    if len(s)==n:
        t.append(sum(s))
        return

    for i in range(4):
        if v[i]==0:
            s.append(l[i])
            dfs()
            s.pop()
dfs()
print(len(set(t)))




# import sys

# L=[1,5,10,50]
# n=int(sys.stdin.readline().strip())
# Answer=0
# visit=[False]*(10000)
# def BackTracking(count , start, total):
#     global Answer
#     if count==n:
#         if visit[total]==False:
#             visit[total]=True
#             Answer+=1
#         return

#     for i in range(start,4):
#         BackTracking(count+1 , i , total+L[i])

# BackTracking(0,0,0)
# print(Answer)




# import sys

# l=[1,5,10,50]
# n=int(sys.stdin.readline())
# s=[]
# t=[]

# def IVXL():
#     if len(s)==n:
#         t.append(sum(s))
#         return

#     for i in range(4):
#         s.append(l[i])
#         IVXL()
#         s.pop()


# IVXL()
# print(len(set(t)))





# import sys
# input=sys.stdin.readline

# result = []

# N = int(input()) #문자의 개수

# if N == 0 :
#     print(0)
#     exit(0)

# for i in range(N+1) :
#     for j in range(N+1-i) :
#         for k in range(N+1-i-j) :
#             temp = N-i-j-k
#             number = i + 5*j + 10*k + 50*temp
#             result.append(number)

# print(*result)




# import sys
# from itertools import combinations_with_replacement
# k=[]
# for cwr in combinations_with_replacement([1,5,10,50], int(sys.stdin.readline())):
#     k.append(sum(cwr))
# print(len(set(k)))





# import sys
# sys.setrecursionlimit(10**8)
# N=int(input())
# L=[1 , 5 , 10, 50]

# visit=[False]*(10000)
# total=0
# Answer=0

# def BackTracking(count , start, total):
#     global Answer
#     if count==N:
#         if visit[total]==False:
#             visit[total]=True
#             Answer+=1
#         return

#     for i in range(start,4):
#         BackTracking(count+1 , i , total+L[i])

# BackTracking(0,0,0)
# print(Answer)

end = time.time()

print(f"{end - start:.5f} sec")
 