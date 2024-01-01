def solution(num, total):
    answer = []
    n=total//num
    minus=num//2
    if num%2:
        for i in range(n-minus,n-minus+num):
            answer.append(i)
    else:
        for i in range(n-minus,n-minus+num+1):
            answer.append(i)
        answer.remove(sum(answer)-total)
    return answer