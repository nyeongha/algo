import sys
sys.stdin = open('../swea/1206_[S/input.txt')
for ii in range(10):
    n=int(input())
    arr=list(map(int,input().split()))
    sum=0

    for n,x in enumerate(arr[2:],start=2):
        ar=sorted(arr[n-2:n+3])





        print("#{} {}".format(n+1,sum))




