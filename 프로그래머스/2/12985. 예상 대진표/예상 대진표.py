def solution(n,a,b):
    answer = 0
    
    while b!=a:
        a = (a + 1) // 2
        b = (b + 1) // 2
        answer += 1

    return answer
