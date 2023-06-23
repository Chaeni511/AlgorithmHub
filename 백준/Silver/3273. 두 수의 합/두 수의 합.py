n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()
left = 0
right = n-1
res = 0

while left < right:
    if arr[left] + arr[right] == x:
        res += 1
        left += 1
        right -= 1
    elif arr[left] + arr[right] < x:
        left += 1
    else:
        right -= 1

print(res)