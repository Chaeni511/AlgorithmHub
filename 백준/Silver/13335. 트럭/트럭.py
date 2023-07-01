n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

t = 0
res = 0

bridge = [0] * w
s = 0
e = w

while True:
    if t == n and sum(bridge[s:e]) == 0:
        break

    if t < n and sum(bridge[s + 1:]) + trucks[t] <= L:
        bridge.append(trucks[t])
        t += 1
    else:
        bridge.append(0)

    s += 1
    e += 1
print(len(bridge[w:]))