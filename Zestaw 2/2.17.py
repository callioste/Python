line = "ala\nma\nkota i psa"
l = line.split()
sorted_alph = sorted(l)

key1 = lambda k: len(k)
sorted_len = sorted(l, key=key1)

print(sorted_alph)
print(sorted_len)