import sys

input = sys.stdin.readline
t = int(input())

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif dp[n] >= 2:
        return dp[n]
    else:
        dp[n] = fib(n-2) + fib(n-1)
        return dp[n]


for _ in range(t):
    dp = [0]*41
    dp[0] = 0
    dp[1] = 1
    input_ = int(input())
    fib(input_)
    if input_ == 0:
        print(1, 0)
    elif input_ == 1:
        print(0, 1)
    elif input_== 2:
        print(1, 1)
    else:
        print(dp[input_-1], dp[input_])