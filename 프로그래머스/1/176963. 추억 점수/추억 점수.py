def solution(name, yearning, photo):
    answer = []
    dic = {name: yearning for name, yearning in zip(name, yearning)}
    for i in range(len(photo)):
        score = 0
        for j in range(len(photo[i])):
            if photo[i][j] in dic:
                score += dic[photo[i][j]]
        answer.append(score)
    return answer