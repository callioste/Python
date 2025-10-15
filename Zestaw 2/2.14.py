line = "ala\nma\nkota i psa"
l = line.split()
key1 = lambda k: len(k)
longest_word = max(l, key= key1)

print(longest_word)
print(len(longest_word))