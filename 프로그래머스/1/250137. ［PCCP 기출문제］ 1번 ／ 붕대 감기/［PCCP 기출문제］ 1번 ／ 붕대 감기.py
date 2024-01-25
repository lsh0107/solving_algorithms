def solution(bandage, health, attacks):
    time = max(attacks)[0]
    consecutive_heal = 0
    max_health = health
    heal = bandage[1]
    additioinal_heal = bandage[2]
    attacks = sorted(attacks, reverse=True)

    for t in range(1, time+1):
        if t != attacks[-1][0]:
            if health + heal >= max_health:
                health = max_health
                consecutive_heal += 1
            else:
                health += heal
                consecutive_heal += 1

        if consecutive_heal == bandage[0]:
            health += additioinal_heal
            consecutive_heal = 0

        if t == attacks[-1][0]:
            health -= attacks[-1][1]
            if health <= 0:
                return -1
            
            attacks.pop()
            consecutive_heal = 0

    if health <= 0:
        return -1

    return health