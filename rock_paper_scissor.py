import random
def play():
    print("What's your guess?")
    print("Press 's' for scissor,'r' for rock and 'p' for paper")
    player = input()
    computer = random.choice(['s','p','r'])
    if player==computer:
        return "Tie"
    if is_win(player,computer):
        return "You won"
    return "You lost"

def is_win(player1,player2):
    if (player1=='r' and player2=='s') or (player1=='s' and player2 =='p') or (player1 == 'p' and player2 == 'r'):
        return True

print(play())