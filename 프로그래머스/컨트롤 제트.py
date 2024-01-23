def solution(s):
    cnt=[]
    s=list(s.split(' '))
    for i in s:
        if i=="Z":
            cnt.pop()
        else:
            cnt.append(int(i))
    answer=sum(cnt)
    return answer