from itertools import combinations
import sys
dic={}
for x in range(int(sys.stdin.readline())):
    dic[x]=sys.stdin.readline()
arr=list(combinations(dic, 3))
count=0
for x,y,z in arr:
    if dic[x]>dic[y]>dic[z]:
        count+=1
print(count)
