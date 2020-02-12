import random
import sys

user_score = 0
computer_score= 0
draw=0


def computer_turn():
    i = random.randint(1,3)
    if i == 1:
        return 'R'
    elif i==2:
        return 'P'
    elif i==3:
        return 'S'
        
def draw_result():
    global draw
    print('DRAW, No one scores.')
    draw = draw+1
    
    return

def computer_gain():
    global computer_score
    print()
    print('Looser, I scored.')
    computer_score = computer_score + 1
    return

def user_gain():
    global user_score
    print()
    print('Okay, You scored')
    user_score = user_score + 1
    return 

def score():
    global computer_score
    global user_score
    global draw
    print('Score: '+ 'Sachu: '+ str(computer_score)+ ' Tina: '+ str(user_score)+ ' Draw: '+ str(draw))
    print()
    return


print('Welcome to Rock Paper Scissors')
print('Enter (R) for Rock, (P) for Paper, (S) for Scissor,(Q) to Quit')


while(True):
    print()
    print("Tina:")
    user_input = input()
    if (user_input == 'Q'):
       break;

    if ((user_input == 'R') or (user_input == 'P') or (user_input =='S')):
    
        computer_input = computer_turn()
        print("Sachu: "+ computer_input)
        
            
        if (user_input == computer_input):
            draw_result()
            score()
            continue
        
        
        elif (user_input == 'R' and computer_input == 'P'):
            computer_gain()
            score()
            continue
        
        elif (user_input == 'R' and computer_input == 'S'):
            user_gain()
            score()
            continue

        elif (user_input == 'P' and computer_input == 'S'):
            computer_gain()
            score()
            continue

        elif (user_input == 'P' and computer_input == 'R'):
            computer_gain()
            score()
            continue

        elif (user_input == 'S' and computer_input == 'R'):
            user_gain()
            score()
            continue

        elif (user_input == 'S' and computer_input == 'P'):
            user_gain()
            score()
            continue
    else:
        print('Wrong Input, enter \'P\' or\'R\' or \'S\'')
        continue

print('Bye Bye')
sys.exit()      
        
        
        






