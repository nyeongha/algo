arr=[]
for i in range(int(input())):
    arr.append(list(map(int,input().split())))

for n1,x in enumerate(arr):
    for n2,i in enumerate(x):
        arr[n1][n2]=(sum(list(map(int,str(i)))))

for n,i in enumerate(arr):
    print("#{} {} {}".format(n+1,max(i),min(i)))

# 2
# 182 371 29 49 28 21 928 11 5 1
# 13 400 3010 2011 1111 40 4 103 301 100111