x = input('Enter width: ')
y = input('Enter height: ')

try:
    x = int(x)
    y = int(y)

except ValueError:
    print('Oops... invalid number! Try again.')
    exit()

upper_line = '+'
lower_line = "|"

for i in range(x):
  upper_line += '---+'
  lower_line += '   |'

s = upper_line + '\n'

for j in range(y):
    s += lower_line + '\n'
    s += upper_line + '\n'

print(s)
