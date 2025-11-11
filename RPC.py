import random

def play():
    user=input("Say Rock Paper Scissor ! 'r' for rock,'p' for paper,'s' for scissors :")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'It is tie'
    
    # r > s, s > p ,p > r
    if is_win(user,computer):
        return 'You Won !'
    
    return 'Computer is won'

def is_win(player,opponent):
    # return true if player is win
    # r > s, s > p ,p > r
    if(player == 'r' and opponent == 's') or(player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    
print(play())