# Import random module to select a random value from 'rock', 'paper' or 'scissor'
import random

# Declare a list of the three options of our game
options = ['rock','paper','scissor']

# Define a function to play the game
def play_game(a):
    computer_choice = random.choice(options) # Computer randomly chooses from the list of options
    print(f'Computer chose: {computer_choice}') # Print the computer's choice for the Player
    if computer_choice == a: # Condition return 0  if both select the same option
        return 0
    elif (computer_choice == 'rock' and a == 'scissor') or (computer_choice == 'paper' and a == 'rock') or (computer_choice == 'scissor' and a == 'paper'):
        return 'Computer' # Condition returns 'Computer' if Computer wins this round
    elif (a == 'rock' and computer_choice == 'scissor') or (a == 'paper' and computer_choice == 'rock') or (a == 'scissor' and computer_choice == 'paper'):
        return 'Player' # Computer returns 'Player' if the player wins this round

def main(): # Main function
    computer_points = 0 # Initializing the points for Player and computer
    player_points = 0
    while computer_points < 5 and player_points < 5: # Playing the game until one reaches 5 points
        print("Select one of the following:") # Displaying the menu of options to choose from
        for i in options:
            print(i)
        try:
            selection = input()
            if selection not in options: # If user inputs something out of the options print error message and continue to ask again
                print("Invalid input.Enter correct value.")
                continue
            else:
                results = play_game(selection) # Call funtion with user's choice to play the game
                if results == 'Computer':
                    computer_points += 1 # Increment if computer wins the round
                elif results == 'Player':
                    player_points += 1 # Increment if Player wins the round
                else:
                    print(f'Computer Points:{computer_points}, Player Points:{player_points}') # Print current status
                    continue
                print(f'Computer Points:{computer_points}, Player Points:{player_points}')
        except ValueError:
            print("Incorrect Input")
            continue

    if computer_points > player_points: # Check points and declare the winner
        print(f'The computer won the game. The results are: Computer - {computer_points} || Player - {player_points}')
    else:
        print(f'Bravo! You won the game. The results are: Computer - {computer_points} || Player - {player_points}')

if __name__ =='__main__':
    main()