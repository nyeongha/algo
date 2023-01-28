from itertools import permutations

def solution(babbling):
    pm=["aya","ye","woo","ma"]
    pm2=[]
    answer=0
    for a in range(1,len(pm)+1):
        for b in permutations(pm,a):
            pm2.append(''.join(b))     
    for i in babbling:
        if i in pm2:
            answer+=1
    return answer