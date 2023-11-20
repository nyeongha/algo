import math
a,b,v=map(int,input().split())
if (v-a)<(a-b):
    print(int(math.ceil((v-a)/(a-b))+1))
else:
    print(int(math.ceil((v-a)/(a-b))+1))