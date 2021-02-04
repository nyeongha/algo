import sys
A=sys.stdin.readline().strip()
arr=[]
for x in range(int(sys.stdin.readline())):
    arr.append(sys.stdin.readline().strip())
for x in arr:
    if x in A:
        A=A.replace(x,'')
if A=='':
    print('1')
else:
    print('0')