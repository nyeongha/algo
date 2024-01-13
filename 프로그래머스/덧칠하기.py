def solution(n, m, section):
    answer=0
    check_section=[0 for i in range(len(section))]
    for n,i in enumerate(section):
        if check_section[n]==0:
            check_section[n]=1
            if i!=section[-1]:
                for nn,j in enumerate(section[n+1:],start=n+1):
                    if j<=i+m-1:
                        check_section[nn]=1
                    else:break
            answer+=1
    return answer

