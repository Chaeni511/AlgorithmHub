import sys

for ch in sys.stdin: #한 줄 씩 입력을 받는다
    if ch[0] == '.': #'.'만 들어오면 종료한다
        break
    stack = []
    flag = 0
    for c in ch:
        if c == '(':
            stack.append(c)
        elif c == '[':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0 or '(' != stack.pop():
                flag = 1
                break
        elif c == ']':
            if len(stack) == 0 or '[' != stack.pop():
                flag = 1
                break
    if flag == 0 and len(stack) == 0:
        print('yes')
    else:
        print('no')