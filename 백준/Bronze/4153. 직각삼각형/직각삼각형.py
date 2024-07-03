import sys
input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0 and nums[1] == 0 and nums[2] == 0:
        break
    if nums[0] == 0 or nums[1] == 0 or nums[2] == 0:
        print('wrong')
        
    nums = sorted(nums)
    max_ = nums.pop()
    
    if max_**2 == nums[0]**2 + nums[1]**2:
        print('right')
    else:
        print('wrong')
    