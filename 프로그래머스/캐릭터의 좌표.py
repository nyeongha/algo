def solution(keyinput, board):
    x=board[0]//2
    y=board[1]//2
    n=[x,y]
    directions={'up':[0,1],'down':[0,-1],'left':[-1,0],'right':[1,0]}
    for i in keyinput:
        if 0<=n[0]+directions[i][0]<board[0] and 0<=n[1]+directions[i][1]<board[1]:
            n=[n[0]+directions[i][0],n[1]+directions[i][1]]
    answer =[n[0]-x,n[1]-y]
    return answer