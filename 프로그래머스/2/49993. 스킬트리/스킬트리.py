def solution(skill, skill_trees):
    answer = 0
    
    for skills in skill_trees:
        i = 0
        valid_tree = True
        for s in skills:
            if s not in skill:
                continue
            
            else:
                if s == skill[i]:
                    i += 1
                    continue
            
                else:
                    valid_tree = False
                    break

        if valid_tree:
            answer += 1
                
    return answer