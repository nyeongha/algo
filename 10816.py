import sys
dict={}

sys.stdin.readline()
n=list(sys.stdin.readline().split())

for i in n:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
        
num_m=sys.stdin.readline()
m=list(sys.stdin.readline().split())

for i in m:
    if i in dict:
        print(dict[i],end=' ')
    else:
        print(0,end=' ')