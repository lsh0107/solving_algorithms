def solution(n):
    answer = 0
    for denom in range(1, n+1):
        if n % denom == 0:
            answer += denom
    return answer