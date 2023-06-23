T = int(input())


def operate(ss):
    tmp = ss.replace(' ', '')
    if eval(tmp) == 0:
        print(ss)


def operator(s, num):
    if num == N+1:
        operate(s)
        return

    operator(s+' '+str(num), num + 1)
    operator(s+'+'+str(num), num + 1)
    operator(s+'-'+str(num), num + 1)


for tc in range(T):
    N = int(input())

    operator('1', 2)
    print()
