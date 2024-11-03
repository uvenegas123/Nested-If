year = int(input('Enter a year:\n'))
leap_year = True
if year % 400 == 0:
    leap_year = True
elif year % 100 == 0:
    leap_year = False
elif year % 4 == 0:
    leap_year = True
else:
    leap_year = False

if leap_year:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')

