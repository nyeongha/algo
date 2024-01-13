def solution(babbling):
    answer=0
    an=["aya","ye","woo","ma"]
    for i in babbling:
        for j in an:
            if j*2 not in i:
                i=i.replace(j,"_"*len(j))
        if i=="_"*len(i):
            answer+=1
    return answer