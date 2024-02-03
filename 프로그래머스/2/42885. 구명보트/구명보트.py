def solution(people, limit):
    answer = 0
    count = 0
    people = sorted(people)
    front = 0
    rear = -1

    while True:
        if len(people) - count == 1:
            answer += 1
            break

        if limit - people[front] >= people[rear]:
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