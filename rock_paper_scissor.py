import random
computer_choices = ['scissors', 'paper', 'rock']


def game(limit):
    if limit > 0:
        computer_choice = computer_choices[random.randint(0,2)]
        user_choice = input('Rock, paper, or scissors?')
        if computer_choice == user_choice:
            print('TIE')
            print(computer_choice)
        elif user_choice == 'rock' and computer_choice == 'scissors':
            print('WIN')
            print(computer_choice)
        elif user_choice == 'paper' and computer_choice == "rock":
            print('WIN')
            print(computer_choice)
        elif user_choice == 'scissors' and computer_choice == "paper":
            print('WIN')
            print(computer_choice)
        else:
            print('LOSE')
            print(computer_choice)
        game(limit-1)

rounds = int(input("How many rounds you wanna go?"))
game(rounds)