def solution(word):
    from itertools import product
    answer = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(1, 6):
        answer += [''.join(perm) for perm in product(vowels, repeat=i)]
    answer.sort()
    return answer.index(word.lower())+1