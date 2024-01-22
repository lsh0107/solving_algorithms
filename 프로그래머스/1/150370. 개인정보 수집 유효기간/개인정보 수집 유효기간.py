def solution(today, terms, privacies):
    answer = []
    dict = {term[0]: int(term[1:]) for term in terms}

    for idx, splitt in enumerate(privacies):
        data = splitt.split('.')
        privacies[idx] = data
    
    for d in privacies:
        temp = d[-1].split(' ')
        d.pop()
        d.append(temp[0])
        d.append(temp[1])

    for check in privacies:
        if int(check[1]) + dict[check[3]] > 12 and (int(check[1]) + dict[check[3]]) % 12 != 0:
            check[0] = int(check[0]) + (int(check[1]) + dict[check[3]])//12
            check[1] = (int(check[1]) + dict[check[3]]) % 12
            if int(check[2]) - 1 == 0:
                check[1] -= 1
                check[2] = 28
            else:
                check[2] = int(check[2]) - 1
        
        elif int(check[1]) + dict[check[3]] > 12 and (int(check[1]) + dict[check[3]]) % 12 == 0: 
            check[0] = int(check[0]) + (dict[check[3]] + int(check[1])) // 12 - 1
            check[1] = 12
            check[2] = int(check[2])
            if int(check[2]) - 1 == 0:
                check[1] -= 1
                check[2] = 28
            else:
                check[2] = int(check[2]) - 1
            
        else:
            check[0] = int(check[0]) 
            check[1] = int(check[1]) + dict[check[3]] 
            if int(check[2]) - 1 == 0:
                check[1] -= 1
                check[2] = 28
            else:
                check[2] = int(check[2]) - 1
    
    today = [int(x) for x in today.split('.')]
    
    for idx, person in enumerate(privacies):
        if person[0] - today[0] > 0:
            pass

        elif person[0] - today[0] >= 0 and person[1] - today[1] > 0:
            pass

        elif person[0] - today[0] >= 0 and person[1] - today[1] >= 0 and person[2] - today[2] >= 0:
            pass

        else:
            answer.append(idx + 1)
        
    return answer