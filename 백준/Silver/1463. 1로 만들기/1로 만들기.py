N = int(input())
cnt = 987654321


def dfs(n, c):
    global cnt
    if c > cnt:
        return

    if n == 1:
        cnt = min(c, cnt)
        return

    if n % 3 == 0:
        dfs(n // 3, c + 1)

    if n % 2 == 0:
        dfs(n // 2, c + 1)

    if n > 0:
        dfs(n - 1, c + 1)


dfs(N, 0)
print(cnt)
