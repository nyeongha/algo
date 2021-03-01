from itertools import combinations
import sys
dic={}
for x in range(int(sys.stdin.readline())):
    dic[x]=sys.stdin.readline()
arr=list(combinations(dic, 3))
cnt=0
for x,y,t in arr
    if dic[x]>dic[y]>dic[t]:
        cnt+=1
print(cnt)
