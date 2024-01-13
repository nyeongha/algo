def solution(routes):
    answer = 0
    routes.sort()
    a=30000
    for i in routes:
        if i==routes[-1]:
            answer+=1
        if i[1]<a:
            a=i[1]
        elif a<i[0]:
            a=i[1]
            answer+=1
    return answer