def make_ruler(n):
    s = '|'

    for i in range(n):
        s += '....|'

    s += '\n'

    for i in range(n + 1):
        if i < 9:
            s += str(i)
            s += '    '
        else:
            s += str(i)
            s += '   '

    return s

def make_grid(rows, cols):
    upper_line = '+'
    lower_line = "|"

    for i in range(rows):
        upper_line += '---+'
        lower_line += '   |'

    s = upper_line + '\n'

    for j in range(cols):
        s += lower_line + '\n'
        s += upper_line + '\n'

    return s

print("Ruler: ")
print(make_ruler(12))

print("\nGrid: ")
print(make_grid(4, 2))






