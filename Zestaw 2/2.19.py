L = [1, 12, 123, 543, 65, 623, 3, 6, 433]
L_str = [str(num) for num in L]
L_padded = [num_s.zfill(3) for num_s in L_str]
s = str(L_padded)
print(s)
