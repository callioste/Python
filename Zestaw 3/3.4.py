while True:
    x = input("Enter a real number (or 'stop' to quit): ")

    if x.lower() == 'stop':
        print('Program terminated.')
        break

    try:
        x = float(x)
        print('Your number is: ', x)
        print(x, ' to the third power is: ', pow(x, 3))
    except ValueError:
        print('Oops... Invalid number!')