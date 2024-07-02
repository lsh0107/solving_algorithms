def solution(sequence, k):
    answer = []
    # if k in sequence:
    #     index = sequence.index(k)
    #     return [index, index]
    
    prev_ = 0
    idx = 0
    sum_ = sequence[0]
    test = []
    while idx < len(sequence):
        if sum_ == k:
            answer.append([prev_, idx])
            sum_ -= sequence[prev_]
            prev_ += 1
            
        elif sum_ < k:
            idx += 1
            if idx < len(sequence):
                sum_ += sequence[idx]
            
        else:
            sum_ -= sequence[prev_]
            prev_ += 1
    
    answer.sort(key=lambda x: x[1]-x[0])
    return answer[0]


# print(solution([1, 1, 1, 2, 3, 4, 5], 9))