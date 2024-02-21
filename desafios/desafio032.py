year = int(input('Enter a year: '))

if year % 4 == 0 and year % 100 != 0:
    print(f'{year} is bissext.')
elif year % 400 == 0:
    print(f'{year} is bissext.')
else:
    print(f'{year} is not bissext.')
