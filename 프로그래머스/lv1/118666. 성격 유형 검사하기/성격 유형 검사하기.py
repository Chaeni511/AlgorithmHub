def solution(survey, choices):
    res = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A":0, "N": 0}
    
    answer = ''
    
    for i in range(len(survey)):
        agree, disagree = survey[i][0], survey[i][1]
        choice = choices[i]
        if choice == 1:
            res[agree] += 3
            
        elif choice == 2:
            res[agree] += 2
            
        elif choice == 3:
            res[agree] += 1
            
        elif choice > 4:
            res[disagree] += choice - 4
            
    if res["R"] >= res["T"]:
        answer += "R"
    else:
        answer += "T"
        
    if res["C"] >= res["F"]:
        answer += "C"
    else:
        answer += "F"
        
    if res["J"] >= res["M"]:
        answer += "J"
    else:
        answer += "M"
        
    if res["A"] >= res["N"]:
        answer += "A"
    else:
        answer += "N"
        
    return answer