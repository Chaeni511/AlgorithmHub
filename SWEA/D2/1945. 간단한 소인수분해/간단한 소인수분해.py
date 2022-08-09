T= int(input())
s= 0
for s in range(T):
    result ={}
    num = int(input())
    for i in [2,3,5,7,11]:
        if num % i == 0:
            while num % i ==0:
                if i in result.keys():
                    result[i] += 1
                    num /= i
                else:
                    result[i] = 1
                    num/= i
        else:
            result[i] = 0
        val = list(result.values())
    print(f'#{s+1} {" ".join(map(str,val))}')