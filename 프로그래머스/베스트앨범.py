
def solution(genres, plays):
    answer=[]
    d = {}  # {"classic":[(0,500),...],...}
    dic = list(zip(plays, genres))  # [(500,classic)..]

    answer = []
    num = 0
    tot = {}
    for i in dic:
        print(i)
        if i[1] in d:
            d[i[1]].append((num, i[0]))
        else:
            d[i[1]] = ([(num, i[0])])

        if i[1] not in tot:
            tot[i[1]] = i[0]
        else:
            tot[i[1]] += i[0]
        num += 1

    for k,h in sorted(tot.items(),key=lambda x:x[1],reverse=True):
        for i,j in sorted(d[k],key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)
    return answer


genres=["classic", "pop", "classic", "classic", "pop"]
plays=[500, 600, 150, 800, 2500]
solution(genres,plays)