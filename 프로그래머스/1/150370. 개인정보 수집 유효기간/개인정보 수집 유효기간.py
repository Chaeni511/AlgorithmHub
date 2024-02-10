def solution(today, terms, privacies):
    answer = []

    # terms를 dictionary로 만듦
    td = {}
    for term in terms:
        tmpS, tmpI = term.split()
        td[tmpS] = int(tmpI)
    
    
    for n in range(len(privacies)):
        # 날짜와 약관을 분리, 날짜를 년월일 분리해서 숫자로
        tmpD, T = privacies[n].split()
        y, m, d = map(int, tmpD.split('.'))
        Y, M, D = map(int, today.split('.'))
        
        # 유효기간 구하기
        # 월
        exp = y * 12 * 28 + (m + td[T]) * 28 + d - 1       
        EXP = Y * 12 * 28 + M * 28 + D
        if exp < EXP:
            answer.append(n+1)
    return answer