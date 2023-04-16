N, K = map(int, input().split())
arr = list(input())

res = 0
for i in range(N):
    flag = False
    if arr[i] == 'P':
        for j in range(i-K, i+K+1):
            if j != i and 0 <= j < N and arr[j] == 'H':
                res += 1
                arr[j] = 0
                flag = True
            if flag:
                break

print(res)
