def roman2int(s):
    di = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev = 0
    total = 0

    for ch in reversed(s):
        curr = di[ch]

        if curr < prev:
            total -= curr
        else:
            total += curr

        prev = curr

    return total

print(roman2int("III"))
print(roman2int("IX"))
print(roman2int("LVIII"))
print(roman2int("MCMXCIV")) #1994