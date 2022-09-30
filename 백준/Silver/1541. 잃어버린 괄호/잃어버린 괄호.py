import sys
x = sys.stdin.readline()
arr = x.split('-')          # ['55', '50+40']
result = 0

temp = sum(map(int, arr[0].split('+')))
if x[0] == '-':
    result -= temp
else:
    result += temp

for i in range(1, len(arr)):
    temp = sum(map(int, arr[i].split('+')))
    result -= temp

print(result)