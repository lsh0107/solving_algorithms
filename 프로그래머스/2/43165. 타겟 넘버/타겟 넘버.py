def solution(numbers, target):
    def dfs(index, curr_sum):
        if index == len(numbers):
            if curr_sum == target:
                return 1
            
            else:
                return 0
        
        return dfs(index+1, curr_sum + numbers[index]) + dfs(index+1, curr_sum - numbers[index])
    
    answer = dfs(0, 0)
    return answer
    

