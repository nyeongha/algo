def wan(n):
    arr=[]
    for x in range(1,n//2+1):
        if n%x==0:
            arr.append(x)
        else:pass
    return arr

def hap(n):
    sum=0
    for x in range(1,n//2+1):
        if n%x==0:
            sum+=x
        else:pass
    return sum

while True:
    a=int(input())
    if a==-1:
        break
    elif a==hap(a):
        print(a,'=',' + '.join(map(str,wan(a))))
    elif a!=hap(a):
        print(a,'is NOT perfect.')