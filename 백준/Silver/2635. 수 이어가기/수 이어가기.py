import sys
import math

N = int(sys.stdin.readline())
result = 2
N2 = 0
for i in range(math.ceil(N/2), N+1):
    cnt = 2
    x = i
    y = N - i
    while x - y >= 0:
        x, y = y, x-y
        if x >= y:
            cnt += 1
        else:
            cnt += 2
            '''
            N = 100
            100 62 38 24 14 10 4 6
            x, y = 4, 6 일 때 x,y가 cnt되지 않고 else로 넘어오기 때문
            '''
            if cnt > result:
                result = cnt
                N2 = i

print(result)
arr = [N, N2]
while len(arr) < result:
    arr.append(arr[-2] - arr[-1])
print(' '.join(map(str, arr)))
