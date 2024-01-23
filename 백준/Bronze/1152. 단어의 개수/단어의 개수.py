N = input()
N = N.split(' ')
count = 0
for i in N:
    if i.isalpha():
        count += 1
print(count)