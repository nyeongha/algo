from itertools import combinations
dic={}
for x in range(int(input())):
    dic[x]=int(input())
arr=list(combinations(dic, 3))
count=0
for x,y,z in arr:
    if dic[x]>dic[y]>dic[z]:
        count+=1
print(count)
