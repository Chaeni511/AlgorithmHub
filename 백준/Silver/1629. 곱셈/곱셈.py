import sys

def dnc(a, b):
    if b == 1:
        return a % C
    else:
        temp = dnc(a, b // 2)
        if b % 2 == 0:
            return temp * temp % C
        else:
            return temp * temp * a % C


A, B, C = map(int, sys.stdin.readline().split())
print(dnc(A, B))

