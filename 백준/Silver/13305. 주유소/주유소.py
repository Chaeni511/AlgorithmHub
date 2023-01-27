N = int(input())
distance = list(map(int, input().split()))
oil = list(map(int, input().split()))

city = res = 0
while city < N-1:
    for i in range(city + 1, N):
        if i == N-1:
            res += sum(distance) * oil[city]
            city = i
            break

        elif oil[i] < oil[city]:
            res += sum(distance[city: i]) * oil[city]
            city = i
            break
print(res)