N, X = map(int, input().split())
arr = list(map(int, input().split()))

res = sum(arr[:X])
temp = res
dic = {temp: 1}
s = 0
e = X

while e < N:
    temp -= arr[s]
    temp += arr[e]
    if temp >= res:
        if temp in dic:
            dic[temp] += 1
        else:
            dic[temp] = 1
        res = temp
    s += 1
    e += 1



if res == 0:
    print("SAD")
else:
    print(res)
    print(dic[res])