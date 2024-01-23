N = input()
dict = {}
for s in N:
    if s.lower() not in dict:
        dict[s.lower()] = 1
    else:
        dict[s.lower()] += 1
max_key = max(dict, key=dict.get)
MAX = max(list(dict.values()))
if list(dict.values()).count(MAX) > 1:
    print("?")
else:
    print(max_key.upper())
