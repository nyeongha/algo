def solution(number, limit, power):
    answer = 0
    ll=[]
    for i in range(1,number+1):
        cnt=0
        arr=[]
        for j in range(1,int(i**0.5)+1):
            if i%j==0:
                arr.append(j)
                if (i//j) not in arr:
                    arr.append(i//j)
        ll.append(len(arr))
    for i in ll:
        if i<=limit:
            answer+=i
        else:
            answer+=power
    return answer