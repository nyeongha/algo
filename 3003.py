ch1=[1,1,2,2,2,8]
ch2=list(map(int,input().split()))

for i,j in zip(ch1,ch2):
    print(i-j,end=' ')

         