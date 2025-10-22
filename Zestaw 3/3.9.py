li = [[], (5,7,73,9), [25,63,5], (4,9), [35,3,5,73,9]]

new_list = []

for i in li:
    s = 0
    for j in i:
        s += j
    new_list.append(s)

print(new_list)