from heapq import heappush, heappop


def func():
    while boxes:
        x, target = heappop(boxes)
        for kid in kids:
            if kid > target:
                return 0
            if target - kid:
                heappush(boxes, (-(target - kid), target - kid))
            kids.pop(0)
            break
    return 1


N, M = map(int, input().split())
gifts = list(map(int, input().split()))
kids = list(map(int, input().split()))
# kids.sort(reverse=True)
boxes = []
for gift in gifts:
    heappush(boxes, (-gift, gift))
print(func())
