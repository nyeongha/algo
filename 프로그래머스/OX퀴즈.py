def solution(quiz):
    answer = []
    for i in quiz:
        x=i.split()
        print(x)
        if '+' in x:
            if int(x[0])+int(x[2])==int(x[4]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(x[0])-int(x[2])==int(x[4]):
                answer.append("O")
            else:
                answer.append("X")
    return answer