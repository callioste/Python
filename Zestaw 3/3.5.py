x = input('Enter desired length: ')

try:
    if len(x) > 2:
        raise ValueError('Error. Your number has more than 2 digits!')

    x = int(x)

except ValueError:
    print('Error. Enter valid integer!')
    exit()

s = '|'

for i in range(x):
    s += '....|'

s += '\n'

for i in range(x+1):
    if i < 9:
        s += str(i)
        s += '    '
    else:
        s += str(i)
        s += '   '

print(s)
