import sys
arr = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
stack = []
stack2 = []
a = 1
b = 0
flag = True
while b != len(arr):
    if (stack2 and stack2[-1] == arr[b]) and arr[b] in stack2:
        stack.append('-')
        stack2.pop()
        b += 1
    elif stack2 and arr[b] in stack2 and stack2[-1] != arr[b]:
        flag = False
        break
    elif not stack2 or (stack2 and stack2[-1] != arr[b]):
        stack.append('+')
        stack2.append(a)
        a += 1
    elif stack2 and a == arr[b]:
        stack.append('+')
        stack2.append(a)
        stack.append('-')
        stack2.pop()
        a += 1
        b += 1


if stack2 or flag == False:
    print('NO')
else:
    print('\n'.join(stack[0:]))




