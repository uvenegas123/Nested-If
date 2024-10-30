#Assignment 2 Task 1

# num1, num2, num3 = int(input('Enter any three numbers:\n')), int(input()), int(input())

# if num2 > num1 and num2 > num3:
#     print(f'{num2} is the largest number out of the three.')
# elif num1 > num2 and num1 > num3:
#     print(f'{num1} is the largest out of the three.')
# else:
#     print(f'{num3} is the largest out of the three')


#Assignment 2 Task 2
num1, num2, num3 = int(input('Enter any three numbers:\n')), int(input()), int(input())
if num1 > num2 and num1 > num3 and num2 > num3:
    print(f'{num1} is the largest out of the three, and {num3} is the smallest')
elif num2 > num1 and num2 > num3 and num1 < num3:
    print(f'{num2} is the largest number, and {num1} is the smallest')
elif num3 > num2 and num3 > num1 and num2 < num1:
   print(f'{num3} is the largest out of the three, and {num2} is the smallest')
else:
    print(f'{num3} is the largest, and {num1} is the smallest')
