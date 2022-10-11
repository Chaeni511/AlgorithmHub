import sys
N = list(sys.stdin.readline())
N.pop()
arr = [0]*9
for n in N:
    if n == '9':
        arr[6] += 1
    else:
        arr[int(n)] += 1
if arr[6] % 2 == 0:
    arr[6] //= 2
else:
    arr[6] //= 2
    arr[6] += 1
print(max(arr))