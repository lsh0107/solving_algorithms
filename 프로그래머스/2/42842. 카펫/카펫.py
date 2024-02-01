def solution(brown, yellow):
    total = brown + yellow
    t = int(total**0.5)
    answer = []
    while True:
        if ((total//t-2) * (t-2)) == yellow and total % t == 0:
            answer.append(total//t)
            answer.append(t)
            break
        else:
            t -= 1
    return answer