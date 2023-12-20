def solution(nums):
    answer = 0
    cnt = len(nums)//2
    bag = list(set(nums))
    if len(bag) > cnt:
        for i in range(len(bag)-cnt):
            bag.pop()
    
    
    return len(bag)