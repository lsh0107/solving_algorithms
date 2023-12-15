def solution(array, commands):
    answer = []
    num = 0
    for i in range(len(commands)):
        temp = array
        temp = temp[commands[i][0]-1:commands[i][1]]
        temp = sorted(temp)
        num = temp[commands[i][2]-1]
        answer.append(num)
    return answer