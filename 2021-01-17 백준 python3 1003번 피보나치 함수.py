import sys
for i in range(int(sys.stdin.readline())):
    zero = 1
    one = 0
    tmp = 0
    for _ in range(int(sys.stdin.readline())):
        tmp = one
        one = one + zero
        zero = tmp
    print(zero, one)