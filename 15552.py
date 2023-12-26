import sys

number = int(input())

for i in range(number):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
