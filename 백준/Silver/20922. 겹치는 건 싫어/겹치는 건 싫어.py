N, K = map(int, input().split())
arr = list(map(int, input().split()))

res = temp = 0
dic = {}

s = 0
for i in range(N):
    if arr[i] not in dic:
        dic[arr[i]] = 1
        temp += 1
    else:
        if dic[arr[i]] < K:
            dic[arr[i]] += 1
            temp += 1
        else:
            if dic[arr[i]] >= K:
                res = max(res, temp)
                while dic[arr[i]] == K:
                    dic[arr[s]] -= 1
                    temp -= 1
                    s += 1
            dic[arr[s-1]] += 1
            temp += 1

res = max(res, temp)
print(res)