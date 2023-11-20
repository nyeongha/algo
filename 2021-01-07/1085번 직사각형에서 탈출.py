
x,y,w,h=map(int,input().split())
arr=[abs(x-w),abs(y-h),abs(x),abs(y)]
b=sorted(arr)
print(b[0])