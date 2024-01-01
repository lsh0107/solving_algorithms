def solution(keymap, targets):
    answer = []

    for target in targets:
        ans = []      

        for t in target:
            temp = []
            
            for key in keymap:
                if t in key:
                    temp.append(key.find(t) + 1) 
                
            if len(temp) == 0:
                ans.append(-1)
                break
            
            else:
                ans.append(min(temp))
        
        if -1 in ans:
            answer.append(-1)
        
        else:    
            answer.append(sum(ans))
    
    return answer