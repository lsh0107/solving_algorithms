def solution(n):
    num = 0
    nums = []
    i = n
    answer = 0

    while True:
        num = divmod(i, 3)
        nums.append(num[1])
        i = num[0]
        if i == 0:
            break

    i = 0
    while True:
        if len(nums) != 0:
            answer += nums[-1]*(3**i)
            nums.pop()
            i += 1
        else:
            break
    
    return answer