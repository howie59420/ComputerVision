import random

def get_computer_choice():
    return random.choice(['rock','paper','scissors'])

def get_user_choice():

    while True:
        answer=input('Please enter a valid choice from rock,paper, or scissors: ').lower()
        if answer in ['rock','paper','scissors']:
            return answer
            break


def get_winner():
    computer_choice=get_computer_choice()
    user_choice=get_user_choice()

    if computer_choice==user_choice:
        print('Draw, keep going!')
    
    elif (computer_choice=='rock' and user_choice=='paper') \
        or (computer_choice=='paper' and user_choice=='scissors') \
        or (computer_choice=='scissors' and user_choice=='rock'):
       print(f'user wins,computer was {computer_choice}')
    
    else:
        print(f'lose,computer was {computer_choice}')
        
        

def play():

    return get_winner()


play()