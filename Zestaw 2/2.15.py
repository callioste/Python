L = [1, 2, 3, 4, 5, 6]
list1 = [str(word) for word in L]
s = ''.join(list1)
print(s)
print(isinstance(s, str))