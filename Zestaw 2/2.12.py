line = "ala\nma\nkota i psa"
first_l = [wyraz[0] for wyraz in line.split()]
first_line = ''.join(first_l)

last_l = [wyraz[-1] for wyraz in line.split()]
last_line = ''.join(last_l)

print(first_line)
print(last_line)
