from itertools import combinations
import sys
dic={}
for k in range(int(sys.stdin.readline())):
    dic[k]=sys.stdin.readline()
arr=list(combinations(dic, 3))
cnt=0
for x,y,t in arr:
    if dic[x]>dic[y]>dic[t]:
        cnt+=1
print(cnt)
