import sys
n = int(sys.stdin.readline())
target = [int(input()) for _ in range(n)]
push = []
pop = []
result = []
j = 0
for i in range(1, n + 1):
    push.append(i)
    result.append('+')
    while push and push[-1] == target[j]:
        pop.append(push.pop())
        result.append('-')
        j += 1
if push:
    print('NO')
else:
    for r in result:
        print(r)