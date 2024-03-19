def solution(word):
    from itertools import product
    vowels = ['a','e','i','o','u']
    vowels_list = []
    for i in range(1, len(vowels)+1):
        vowels_list += [''.join(permutation) for permutation in product(vowels, repeat=i)]
    
    vowels_list.sort()
    answer = vowels_list.index(word.lower()) + 1
    return answer