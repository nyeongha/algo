# from itertools import permutations
#
# def solution(babbling):
#     pm=["aya","ye","woo","ma"]
#     pm2=[]
#     answer=0
#     for a in range(1,len(pm)+1):
#         for b in permutations(pm,a):
#             pm2.append(''.join(b))
#     for i in babbling:
#         if i in pm2:
#             answer+=1
#     return answer

def solution(babbling):
    answer = 0
    now=["aya","ye","woo","ma"]
    for i in babbling:
        c=len(i)
        for j in now:
            if i == '_' * c:
                break
            if j in i:
                cj=len(j)
                i=i.replace(j,'_'*cj)
        if i=='_'*c:
            answer+=1
    return answer