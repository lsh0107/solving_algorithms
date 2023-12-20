def solution(k, m, score):
    answer = 0
    score.sort()
    bag = []
    cnt = 0
    while len(score) > 0:

        # if score:
        #     bag.append(score.pop())
    
        # if len(bag) == m:
        #     answer += min(bag)*m
        #     bag = []
        
        #     if len(score) < m:
        #         return answer
        
        
        if cnt < m:
            bag.append(score.pop())
            cnt += 1
                
        elif len(bag) == m:
            answer += min(bag)*m
            bag = []
            cnt = 0
    
    if len(bag) == m:
        answer += min(bag)*m
    return answer