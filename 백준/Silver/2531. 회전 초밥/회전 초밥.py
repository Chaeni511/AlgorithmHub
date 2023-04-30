import sys
# 접시 수, 초밥 가짓수, 연속해서 먹는 접시 수, 쿠폰 번호
n, d, k, c = map(int, sys.stdin.readline().split())
sushi = [int(sys.stdin.readline()) for _ in range(n)]

# for i in range(min(d, k), 0, -1):
#     print(i)


res = 0
e = k
flag = True
min_len = min(d, k+1)


def func():
    global e, res
    for s in range(n):
        if s < e:
            res = max(res, len(set(sushi[s:e]+[c])))
        else:
            res = max(res, len(set(sushi[s:] + sushi[:e] + [c])))
        if res >= min_len:
            return
        e = (e+1) % n


func()
print(res)
