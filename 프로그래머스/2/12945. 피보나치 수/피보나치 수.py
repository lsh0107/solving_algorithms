def solution(n):
    dp = [0, 1]
    t = 0
    while t < n:
        t += 1
        dp.append(dp[-2] + dp[-1])
        
    return dp[-2]%1234567