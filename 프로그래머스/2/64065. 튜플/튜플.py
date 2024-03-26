def solution(s):
    answer = []
    split_sets = s[2:-2].split("},{")
    parsed_sets = [list(map(int, s.split(","))) for s in split_sets]
    s = sorted(parsed_sets, key=lambda k: len(k))
    for i in range(len(s)):
        if len(s[i]) == 1:
            answer.append(s[i][0])
        
        else:
            num = set(s[i]) - set(answer)
            answer.append(num.pop())
    
    return answer