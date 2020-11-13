import random

choices = ["Rock", "Paper", "Scissors"]

number = random.randrange(0,3)

computer = choices[number]

user_choice = input("Choose between Rock (1), Paper (2), Scissors (3) by typing the corresponding number and then 'Enter' : ")

while(user_choice != '1' and user_choice != '2' and user_choice != '3'):
    print("It seems like you have entered a number that is not between 1 and 3. Try again.")
    user_choice = input("Choose between Rock (1), Paper (2), Scissors (3) by typing the corresponding number and then 'Enter' : ")

if user_choice == '1':
    user_choice = 'Rock'
elif user_choice == '2':
    user_choice = 'Paper'
else:
    user_choice = 'Scissors'

if computer == user_choice:
    print('Oh we made the same choice !')
elif computer == 'Paper' and user_choice == 'Rock':
    print('I won !')
elif computer == 'Paper' and user_choice == 'Scissors':
    print('Oh, you won !')
elif computer == 'Rock' and user_choice == 'Paper':
    print('Oh you won !')
elif computer == 'Rock' and user_choice == 'Scissors':
    print('You loose !')
elif computer == 'Scissors' and user_choice == 'Rock':
    print('You lucky bitch ! You won..')
elif computer == 'Scissors' and user_choice == 'Paper':
    print('I\'m the best.')
else:
    pass
