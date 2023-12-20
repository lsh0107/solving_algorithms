def solution(k, score):
    answer = []
    top_k = []
    while score:
        if len(top_k) < k:
            top_k.append(score.pop(0))
            top_k.sort(reverse=True)
            answer.append(top_k[-1])
        
        else:
            top_k.sort(reverse=True)
            if score[0] >= top_k[-1]:
                top_k.pop()
                top_k.append(score.pop(0))
                top_k.sort(reverse=True)
                answer.append(top_k[-1])
            else:
                score.pop(0)
                answer.append(top_k[-1])
    return answer