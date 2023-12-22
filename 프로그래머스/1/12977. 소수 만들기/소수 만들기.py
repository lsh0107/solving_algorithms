import math


def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    
    return True


def solution(nums):
    answer = 0
    sorted(nums)

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                num = nums[i] + nums[j] + nums[k]
                
                if is_prime(num):
                    
                    answer += 1
                


    return answer