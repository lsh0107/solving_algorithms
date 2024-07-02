import math
def solution(n, stations, w):
    answer = 0
    s, e = 0, 0
    f = 1
    for i in stations:
        s = max(1, i - w)
        e = min(n, i + w)
        answer += math.ceil((s - f)/(1+2*w))
        f = e + 1
    
    if f <= n:
        answer += math.ceil((n - f + 1)/(1+2*w))
        
    return answer