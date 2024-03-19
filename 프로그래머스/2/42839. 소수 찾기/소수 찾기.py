def solution(numbers):
    from itertools import permutations
    answer = []
    permutation = []
    numbers = [num for num in numbers]
    
    for i in range(1, len(numbers)+1):
        permutation += list(permutations(numbers, i))
    
    permutation = [int(('').join(per)) for per in permutation]
    permutation = list(set(permutation))
    
    for num in permutation:
        if num > 1 and is_prime(num):
            answer.append(num)

    return len(answer)


def is_prime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return num
        