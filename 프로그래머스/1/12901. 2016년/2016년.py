def solution(a, b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    days = 0
    for i in range(a-1):
        days += months[i]
    answer = day[((days+b)%7)-1]
    return answer