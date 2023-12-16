def solution(numbers):
    answer = ''
    temp = []
    str_num = ''
    for num in numbers:
        str_num = str(num)*4
        str_num = str_num[:4]
        temp.append((str_num, num))
    
    temp.sort(reverse=True)
    
    if temp[0][1] == 0:
        return '0'
    else:
        for s, i in temp:
            answer += str(i)
        return answer

print(solution([3, 30, 34, 5, 9]))
print(solution([6, 10, 2]))