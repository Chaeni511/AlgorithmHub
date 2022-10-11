import sys
N = int(sys.stdin.readline())
dasom = int(sys.stdin.readline())
cnt = 0
arr = []
for _ in range(N-1):
    arr.append(int(sys.stdin.readline()))

if N == 1:
    print(0)
else:
    while dasom <= max(arr):
        dasom += 1
        arr[arr.index(max(arr))] -= 1
        cnt += 1
    print(cnt)
