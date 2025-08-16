def solution(schedules, timelogs, startday):
    def to_min(hhmm):
        hhmm = int(hhmm)
        return (hhmm // 100) * 60 + (hhmm % 100)

    answer = len(schedules)

    for sched, logs in zip(schedules, timelogs):
        sched_min = to_min(sched)
        deadline = sched_min + 10

        today = startday
        i = 0
        late = False

        for log in logs:
            if today in (6, 7):
                today = (today % 7) + 1
                continue

            actual_min = to_min(log)
            if actual_min > deadline:
                late = True
                break

            today = (today % 7) + 1

        if late:
            answer -= 1

    return answer
