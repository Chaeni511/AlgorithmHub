N = int(input())
arr = [0] * 1001

for i in range(N):
    L, H = map(int, input().split())
    arr[L] = H
top = res = max(arr)
front = rear = 0

for i in range(arr.index(top)):
    if arr[i] <= top and arr[i] > front:
        front = arr[i]
    res += front

for i in range(1000, arr.index(top), -1):
    if arr[i] <= top and arr[i] > rear:
        rear = arr[i]
    res += rear
print(res)
