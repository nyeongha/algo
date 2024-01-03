def solution(park, routes):
    x,y=0,0
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j]=='S':
                x,y=i,j
                break

    dd={'E':(0,1),'W':(0,-1),'S':(1,0),'N':(-1,0)}
    for a,b,c in routes:
        flag=0
        if 0<=x+(int(c)*dd[a][0])<len(park) and 0<=y+(int(c)*dd[a][1])<len(park[0]):
            for i in range(1,int(c)+1):
                if park[x+(i*dd[a][0])][y+(i*dd[a][1])]=='X':
                    flag=1
                    break
            if flag==0:
                x,y=x+(int(c)*dd[a][0]),y+(int(c)*dd[a][1])
    answer=[x,y]
    return answer