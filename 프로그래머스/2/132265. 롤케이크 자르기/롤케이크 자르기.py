def solution(topping):
    answer = 0
    chul = set()
    su = {}
    for i in topping:
        if i in su:
            su[i] += 1
        else:
            su[i] = 1

    for i in topping:
        chul.add(i)
        su[i] -= 1

        if su[i] == 0:
            del su[i]
        
        if len(chul) == len(su.keys()):
            answer += 1
            
    return answer