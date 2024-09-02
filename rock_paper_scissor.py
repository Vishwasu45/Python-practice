import random


def print_func(printable):
    print(printable)

computer_choice = random.choice(['rock', 'paper', 'scissor'])
user_choice = input('Enter your choice: ')
you_win = 'You win!'
print_computer_choice = 'Computer choice: ' + computer_choice
print_user_choice = 'User choice: ' + user_choice

if user_choice == computer_choice:
    print('It is a tie!')
elif ((user_choice == 'rock' and computer_choice == 'scissor')
      or (user_choice == 'paper' and computer_choice == 'rock')
      or (user_choice == 'scissor' and computer_choice == 'paper')):
    print(print_computer_choice)
    print(print_user_choice)
    print(you_win)
    print_func(you_win)
else:
    print(print_computer_choice)
    print(print_user_choice)
    print('You lose!')