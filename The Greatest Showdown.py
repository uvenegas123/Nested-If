#Assignment 2 Task 1

# num1, num2, num3 = int(input('Enter any three numbers:\n')), int(input()), int(input())

# if num2 > num1 and num2 > num3:
#     print(f'{num2} is the largest number out of the three.')
# elif num1 > num2 and num1 > num3:
#     print(f'{num1} is the largest out of the three.')
# else:
#     print(f'{num3} is the largest out of the three')


#Assignment 2 Task 23
num1, num2, num3 = int(input("Enter three numbers:\n")), int(input()), int(input())

largest = max(num1, num2, num3)
smallest = min(num1,num2,num3)
if largest:
    print (f'the largeest number is {largest} and the smallest number is {smallest}')