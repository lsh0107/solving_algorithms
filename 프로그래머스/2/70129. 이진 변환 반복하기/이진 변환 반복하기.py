def solution(s):
    answer = [0, 0]

    while len(s) > 1:
        new_s = ''
        count = s.count('0')
        answer[0] += 1
        answer[1] += count
        s = s.replace('0', '')
        length = len(s)
        while length >= 1:
            r = length % 2
            length = length // 2
            new_s += str(r)
            
        s = new_s[::-1]

    return answer