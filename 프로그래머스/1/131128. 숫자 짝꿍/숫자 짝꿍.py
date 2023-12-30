def solution(X, Y):
    answer = ''
    x_y = set(X) & set(Y)
    
    if not x_y:
        return '-1'
    
    elif len(x_y) == 1 and '0' in x_y:
        return '0'
    
    for digit in x_y:
        v = min(X.count(digit), Y.count(digit))
        answer += digit*v
        
    return ''.join(sorted(answer, reverse=True))