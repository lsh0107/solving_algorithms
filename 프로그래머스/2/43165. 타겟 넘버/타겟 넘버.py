def solution(numbers, target):
    answer = dfs(0, 0, numbers, target)
    return answer

def dfs(index, curr_sum, numbers, target):
    if index == len(numbers):
        if curr_sum == target:
            return 1
        else:
            return 0
    
    return dfs(index + 1, curr_sum + numbers[index], numbers, target) + dfs(index + 1, curr_sum - numbers[index], numbers, target)
