T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    temp = [0] * len(arr)
    arr.sort()

    temp[0] = arr.pop()
    temp[1] = arr.pop()
    temp[len(temp) - 1] = arr.pop()

    front = 1
    rear = len(temp) - 1
    while arr:
        target = arr.pop()
        front_gap = abs(temp[front] - target)
        rear_gap = abs(temp[rear] - target)
        if front_gap >= rear_gap:
            front += 1
            temp[front] = target
        else:
            rear -= 1
            temp[rear] = target
    ans = abs(temp[0] - temp[len(temp)-1])
    for i in range(len(temp)-1):
        ans = max(ans, abs(temp[i] - temp[i+1]))
    print(ans)


