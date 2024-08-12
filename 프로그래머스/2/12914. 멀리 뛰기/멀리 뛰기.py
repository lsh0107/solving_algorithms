def solution(n):
    answer = 0
    dp = [0, 1]

    for i in range(2, n+2):
        dp.append(dp[i-1] + dp[i-2])

    return dp[-1]%1234567
