def solution(survey, choices):
    answer = ''
    dict = {"R": 0, "T": 0, "C": 0, "F": 0,
            "J": 0, "M": 0, "A": 0, "N": 0}
    
    for sur, choice in zip(survey, choices):
        left, right = sur[0], sur[1]

        if choice < 4:
            if choice == 3:
                dict[left] += choice - 2
            elif choice == 1:
                dict[left] += choice + 2
            else:
                dict[left] += choice
        
        if choice > 4:
            dict[right] += choice - 4

    value = list(dict.values())
    key = list(dict.keys())
    for i in range(0, len(value), 2):
        if i + 1 < len(value):
            left = value[i]
            right = value[i + 1]
        
        if left > right:
            answer += key[i]
        elif left < right:
            answer += key[i + 1]
        else:
            answer += key[i]

    return answer