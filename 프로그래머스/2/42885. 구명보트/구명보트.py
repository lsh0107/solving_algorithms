def solution(people, limit):
    answer = 0
    min_ = 0
    max_ = 0
    count = 0
    people = sorted(people)
    front = 0
    rear = -1

    while True:
        min_ = people[front]
        max_ = people[rear]

        if len(people) - count == 1:
            answer += 1
            count += 1
            rear -= 1
            break

        if limit - max_ >= min_:
            answer += 1
            front += 1
            rear -= 1
            count += 2
        
        else:
            answer += 1
            rear -= 1
            count += 1

        if len(people) == count:
            break

    return answer