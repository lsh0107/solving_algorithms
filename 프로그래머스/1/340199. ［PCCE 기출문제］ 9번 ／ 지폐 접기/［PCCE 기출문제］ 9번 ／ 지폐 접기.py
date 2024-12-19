def solution(wallet, bill):
    answer = 0
    bill_min, wall_min = min(bill), min(wallet)
    bill_max, wall_max = max(bill), max(wallet)
    while bill_min > wall_min or bill_max > wall_max:
        if bill[0] > bill[1]:
            bill[0] = bill[0] // 2
        else:
            bill[1] = bill[1] // 2
        answer += 1
        bill_min, wall_min = min(bill), min(wallet)
        bill_max, wall_max = max(bill), max(wallet)
    return answer