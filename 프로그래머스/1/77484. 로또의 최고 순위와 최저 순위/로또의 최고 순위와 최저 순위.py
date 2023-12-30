def solution(lottos, win_nums):
    answer = []
    lottos = sorted(lottos, reverse=True)
    win_nums = sorted(win_nums, reverse=True)
    del_nums = []
    
    if lottos == win_nums:
        return [1, 1]
    
    else:
        for i in range(6):
            if lottos[i] in win_nums:
                del_nums.append(lottos[i])
                win_nums[win_nums.index(lottos[i])] = -1
                lottos[i] = -1
                
        if len(del_nums) == 0:
            if lottos.count(0) == 0:
                return [6, 6]
            
            else:
                return [7-lottos.count(0), 6]
        
        else:
            answer.append(7-len(del_nums))

    answer.append(7 - (lottos.count(0)+len(del_nums)))
    return sorted(answer)