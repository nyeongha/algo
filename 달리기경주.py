def solution(players, callings):
    players2={}

    for n,p in enumerate(players):
        players2[p]=n

    for i in callings:
        temp=players2[i]
        players2[i]-=1
        players2[players[temp-1]]+=1
        players[temp],players[temp-1]=players[temp-1],players[temp]
    answer= sorted(players2, key= lambda x:players2[x])

    return answer
