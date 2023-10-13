def solution(want, number, discount):
    answer = 0
    n_li={want:number for want,number in zip(want,number)}
    for i in range(len(discount)-9):
        nn_li=discount[i:i+10]
        cnt=0
        for w,n in n_li.items():
            if nn_li.count(w) == n:
                cnt+=1
                continue
            else:
                break
        if cnt==len(n_li):
            answer+=1
    return answer