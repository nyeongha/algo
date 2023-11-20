i=int(input())
arr=[]
for x in range(i):
    arr.append(input())
#print(arr)#배열에 뭐가 들어있는지 보기위해서 문제 외에 작성함
tot = 0
point = 0
for x in arr:
    for y in x:
        if y == 'O':
            point += 1
            tot += point
        elif y == 'X':
            point = 0

    print(tot)
    point = 0
    tot = 0
