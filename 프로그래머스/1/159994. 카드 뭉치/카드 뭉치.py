def solution(cards1, cards2, goal):
    answer = ''
    words = []
    idx = 0
    while idx < len(goal):
        if cards1 and goal[idx] == cards1[0]:
            words.append(cards1.pop(0))
            idx += 1
        
        elif cards2 and goal[idx] == cards2[0]:
            words.append(cards2.pop(0))
            idx += 1
        
        else:
            answer = 'No'
            return answer
            
    answer = 'Yes'
    return answer