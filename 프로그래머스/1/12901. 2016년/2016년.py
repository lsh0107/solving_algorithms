def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    months = 0
    for i in range(a-1):
        months += days[i]
    answer = day[((months+b)%7)-1]
    return answer