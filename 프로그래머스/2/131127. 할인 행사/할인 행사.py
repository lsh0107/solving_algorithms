def solution(want, number, discount):
    answer = 0
    items = []

    for name, count in zip(want, number):
        items.extend([name]*count)

    for day in range(len(discount) - 9):
        check = discount[day:day+10]

        if sorted(check) == sorted(items):
            answer += 1
    
    return answer