stack = []
st = []
arr = []
flag = True
a = int(input())
for x in range(a):
    arr.append(int(input()))
t = 0
ty = 0
while True:
    if stack and (stack[-1] != arr[t]) and (arr[t] in stack):
        print('NO')
        flag = False
        break
    if not arr:
        stack.append(y)
        st.append('+')
        print(stack)
        print(st)
    elif stack[-1] == arr[t] and (y not in stack):
        stack.append(y)
        st.append('+')
        print(stack)
        print(st)
        stack.pop()
        st.append('-')
        arr.remove(arr[t])
        t += 1
        print(stack)
        print(st)

    elif y != arr[t] and (y not in stack):
        stack.append(y)
        st.append('+')
        print(stack)
        print(st)

    elif stack and (stack[-1] != arr[t]) and (arr[t] in stack):
        print('NO')
        flag = False
        break

if stack and flag == True:
    for x in st:
        print(x)




