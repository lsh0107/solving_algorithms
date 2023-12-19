def solution(food):
    answer = ''
    for num in range(1, len(food)):
        answer += str(num)*(food[num]//2)

    answer += '0' + answer[::-1]
    return answer