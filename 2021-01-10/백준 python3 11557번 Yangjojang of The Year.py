for x in range(int(input())):
    dic={}
    for y in range(int(input())):
        a,b=input().split()
        dic[a]=int(b)
    b=sorted(dic.items(), key=lambda x: x[1], reverse=True)
    print(b[0][0])