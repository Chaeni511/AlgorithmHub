import heapq

N = int(input())
H = []
for _ in range(N):
    temp = map(int, input().split())
    for i in temp:
        if len(H) < N:
            heapq.heappush(H, i)
        else:
            if H[0] < i:
                heapq.heappop(H)
                heapq.heappush(H, i)
print(H[0])



