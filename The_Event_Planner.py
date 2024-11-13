# #Assignment 2 Task 1
# attendees = int(input("Enter number of attendees: "))
# venue = "large hall" if attendees > 100 else "conference room"
# print(venue)

# #Assignment 2 Task 2
# if venue == 'large hall':
#     print(f'{venue} with audio system')
# elif venue == 'conference room':
#     print(f'{venue} with projector')
# else:
#     pass



#Assignment 2 Task 3

vegetarian = str(input('Would you like vegetarian food?\n')).lower() == 'yes'

if vegetarian:
    print("I recommend trying 'Veggie Delight Caterers'")
elif not vegetarian:
    print("I recomend 'Gourmet Meals Caterers'")
else:
    pass