import sys

N = int(sys.stdin.readline())
solutions = list(map(int, sys.stdin.readline().strip().split()))

s, e = 0, N-1
ss, ee = 0, N-1

target = abs(solutions[s] + solutions[e])

while s < e:

    if abs(solutions[s] + solutions[e]) < target:
        target = abs(solutions[s] + solutions[e])
        ss, ee = s, e

    if target == 0:
        break

    elif solutions[s] + solutions[e] < 0:
        s += 1

    else:
        e -= 1

print(solutions[ss], solutions[ee])
