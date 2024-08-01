def solution(cards1, cards2, goal):
    answer = 'No'
    maxLen = len(goal)
    idx1, idx2 = 0, 0
    words = ''
    for i in range(maxLen):
        word = goal[i]
        if idx1 < len(cards1) and cards1[idx1] == word:
            words += cards1[idx1] + ' '
            idx1 += 1
        elif idx2 < len(cards2) and cards2[idx2] == word:
            words += cards2[idx2] + ' '
            idx2 += 1
        
        if words.split() == goal:
            answer = 'Yes'
            break

    return answer