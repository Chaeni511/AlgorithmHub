X, Y, W, S = map(int, input().split())
X, Y = abs(X), abs(Y)
if Y > X:
    X, Y = Y, X
res = 0
if S > 2 * W:
    res += Y * 2 * W
else:
    res += Y * S

X -= Y
Y = 0


if X % 2 == 1:
    res += W
    X -= 1
res += X * min(W, S)

print(res)