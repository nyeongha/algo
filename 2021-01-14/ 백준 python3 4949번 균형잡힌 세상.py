import sys
pin=[]
while True:
    sen=str(sys.stdin.readline())
    arr=[]
    flag=True
    if sen[0]=='.':
        break
    else:
        for x in list(sen):
            if x=='(':
                arr.append(x)
            elif x==')':
                if arr and arr[-1]=='(':
                        arr.pop()
                else:
                    flag=False
                    break
            elif x=='[':
                arr.append('[')
            elif x==']':
                if arr and arr[-1]=='[':
                        arr.pop()
                else:
                    flag=False
                    break
        if not arr and flag==True:
            pin.append('yes')
        else:
            pin.append('no')

for x in pin:
    print(x)
