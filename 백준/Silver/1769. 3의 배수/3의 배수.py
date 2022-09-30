import sys
X = int(sys.stdin.readline())
Y = list(map(int, list(str(X))))
cnt = 0
while len(Y) != 1:
    cnt +=1
    Y = list(map(int, list(str(sum(Y)))))
print(cnt)
if Y[0] % 3 == 0:
    print('YES')
else:
    print('NO')