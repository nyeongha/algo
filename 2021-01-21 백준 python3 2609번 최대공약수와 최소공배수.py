import sys


def gcd(a, b):
    if a == 0 or b == 0:
        return a if b == 0 else b
    elif a == b:
        return a
    else:
        return gcd(b % a, a) if a < b else gcd(a % b, b)


a, b = map(int, sys.stdin.readline().split())
print(gcd(a, b))
print((a * b) // gcd(a, b))
