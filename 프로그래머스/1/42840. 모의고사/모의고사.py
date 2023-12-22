def solution(answers):
    answer = []
    person1 = [1,2,3,4,5]*2000 #5씩 반복 -> 10000번
    person2 = [2,1,2,3,2,4,2,5]*1250 #8씩 반복 -> 10000번
    person3 = [3,3,1,1,2,2,4,4,5,5]*1000 #10씩 반복 -> 10000번
    people = [person1,person2,person3]

    for order in range(3):
        count = 0
        for idx, i in enumerate(answers):
            if i == people[order][idx]:
                count += 1
        answer.append((order,count))
    
    sorted(answer, key=lambda x: (-x[1], x[0]))
    top = max(i[1] for i in answer)
    answer = [order[0] + 1 for order in answer if order[1] == top]
    return answer