def solution(n, lost, reserve):
    s = set(lost) & set(reserve)
    l = set(lost) - s
    r = set(reserve) - s

    answer = n
    for i in r:
        if i - 1 in l:
            l.remove(i - 1)
        elif i + 1 in l:
            l.remove(i + 1)
    return answer - len(l)