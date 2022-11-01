import random


def main():
    while True:
    # play()
     print(play())



    
def play():

        user = input("Press 'r' for rock, 'p' for papper,'s' for scissors: ").lower()
        computer = random.choice(['r', 'p', 's'])
        if user == computer:
            return "It's tie!!"
    #call player_wins function      
        if player_wins(user, computer): 
            return 'You won 😮️!!!'        
        return 'You lost 😢️!!'
        



def player_wins(player, opponent):

#return true if player wins
# r > s ,s > p, p > r
    if(player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == "p"):
        return True


main()
