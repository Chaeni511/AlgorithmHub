import sys
def binary_search(x):
    start = 0
    end = N-1
    while start <= end:
        mid = (start+end)//2
        if x == arr[mid]:
            return 1
        elif x < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return 0


N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
M = int(sys.stdin.readline())
X = list(map(int,sys.stdin.readline().split()))

for x in X:
    print(binary_search(x))