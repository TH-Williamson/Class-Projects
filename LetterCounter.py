

s = input('please enter text: ')

d ={}

for char in s:
    if char not in d:
        d[char] = 1
    else:
        d[char] += 1

for k in d.keys():
    print(k, 'appears', d[k], 'times')

