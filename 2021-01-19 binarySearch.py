def binary(n,S,x):
    low=1
    high=n
    location=0
    while(low <= high and location==0):
        mid=(low+high)//2
        if (x==S[mid]):
            location=mid
        elif x<S[mid]:
            high=mid-1
        else:
            low=mid+1
    return location
m=[2,5,7,8,10]
print(binary(4,m,5))

