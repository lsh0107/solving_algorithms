def solution(n):
    dp = [0, 1]
    t = 2
    while t <= n:
        t += 1
        dp.append(dp[-2] + dp[-1])
        
    return dp[-1]%1234567