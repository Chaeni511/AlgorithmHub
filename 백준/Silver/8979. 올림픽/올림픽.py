N, K = map(int, input().split())
arr = [[0, 0, 0] for _ in range(N+1)]

for i in range(N):
    temp = list(map(int, input().split()))
    arr[temp[0]][0] = temp[1]
    arr[temp[0]][1] = temp[2]
    arr[temp[0]][2] = temp[3]
country = []
res = 0
for i in range(1, N+1):
    if i not in country and i != K and arr[i][0] > arr[K][0]:
        res += 1
        country.append(i)

for i in range(1, N + 1):
    if i not in country and i != K and arr[i][1] > arr[K][1]:
        res += 1
        country.append(i)

for i in range(1, N + 1):
    if i not in country and i != K and arr[i][2] > arr[K][2]:
        res += 1
        country.append(i)

print(res)