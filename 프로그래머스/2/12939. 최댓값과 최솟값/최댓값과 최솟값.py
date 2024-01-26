def solution(s):
    answer = ''
    s = s.split()
    nums = [int(x) for x in s]
    answer += str(min(nums)) + ' ' + str(max(nums))
    return answer