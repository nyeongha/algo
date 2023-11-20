def jg(list):
    if list[0]**2+list[1]**2==list[2]**2:
        return 'right'
    else:return 'wrong'

while True:
    a=sorted(list(map(int,input().split())))
    if a[0]==0 and a[1]==0 and a[2]==0:
        break
    else:
        print(jg(a))