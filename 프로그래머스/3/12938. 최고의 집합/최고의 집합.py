def solution(n, s):
    answer = []
    r = 0
    if n > s:
        return [-1]
    
    while n > 0:
        r = s // n
        s = s - r
        n = n - 1
        answer.append(r)
        
    return answer