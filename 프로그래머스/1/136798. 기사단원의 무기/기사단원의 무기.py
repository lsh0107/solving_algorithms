def solution(number, limit, power):
    attack_damage = []

    for i in range(1, number+1):
        div = num_divisor(i)
        attack_damage.append(div)
    
    for idx, dmg in enumerate(attack_damage):
        if dmg > limit:
            attack_damage[idx] = power

    return sum(attack_damage)


def num_divisor(n):
    div = []
    for i in range(1, int(n**0.5) + 1):
        if (n % i) == 0:
            div.append(i)
            if (i**2) != n:
                div.append(n // i)

    return len(div)