def solution(lottos, win_nums):
    zero = correct = 0
    answer = []
    
    for lotto in lottos:
        if lotto == 0:
            zero += 1
        elif lotto in win_nums:
            correct += 1
            
    for i in [correct + zero, correct]:
        if i == 6:
            answer.append(1)
        elif i == 5:
            answer.append(2)
        elif i == 4:
            answer.append(3)
        elif i == 3:
            answer.append(4)
        elif i == 2:
            answer.append(5)
        else:
            answer.append(6)
    return answer