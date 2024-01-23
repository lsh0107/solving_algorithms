s = input()

alphas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# alphas = {alpha: idx for idx, alpha in enumerate(alphas)}

for i in range(26):
    if alphas[i] in s:
        print(s.index(alphas[i]), end=' ')
    
    else:
        print(-1, end=' ')