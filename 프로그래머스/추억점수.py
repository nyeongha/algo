def solution(name, yearning, photo):
    answer = []
    name_yearning = {n: y for n, y in zip(name, yearning)}
    for i in photo:
        an = 0
        for x in i:
            if x in name:
                an += name_yearning[x]
        answer.append(an)

    return answer