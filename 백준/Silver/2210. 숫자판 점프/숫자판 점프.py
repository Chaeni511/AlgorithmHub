def dfs(x, y):
    global temp
    if len(temp) == 6:
        nums.add(temp)
        return

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < 5 and 0 <= ny < 5:
            temp += arr[nx][ny]
            dfs(nx, ny)
            temp = temp[:len(temp)-1]


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

arr = [list(input().split()) for _ in range(5)]
# print(arr)
nums = set()
# nums = {}
for i in range(5):
    for j in range(5):
        temp = arr[i][j]
        dfs(i, j)
print(len(nums))