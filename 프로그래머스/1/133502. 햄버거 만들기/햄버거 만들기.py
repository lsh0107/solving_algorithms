def solution(ingredient):
    answer = 0
    length = len(ingredient)
    idx = 0
    order = []
    while ingredient:
        
        if length < 4 or idx == len(ingredient):
            return answer
        
        if idx + 3 <= len(ingredient) and \
            ingredient[idx:idx+4] == [1,2,3,1]:
            answer += 1
            ingredient.pop(idx)
            ingredient.pop(idx)
            ingredient.pop(idx)
            ingredient.pop(idx)
            idx = idx - 2
            length = len(ingredient)

        else:
            idx += 1
    
    return answer