def solution(arr):
    answer = arr[0]

    for i in range(1, len(arr)):
        answer = lcm(answer, arr[i])

    return answer

def gcd(num1, num2):
    big = max(num1, num2)
    small = min(num1, num2)
    r = 1

    while r:
        r = big % small
        big = small
        small = r
    
    return big

def lcm(num1, num2):
    div = gcd(num1, num2)
    return num1 * num2 // div