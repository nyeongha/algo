i=int(input())
arr=[]
arr[0:i]=map(int,input().split())
arr.sort()
print(arr[0],arr[i-1])