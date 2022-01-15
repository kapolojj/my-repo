import os
os.system("cls")
from colorama import Fore


# the Display is made using dictionary 
# in which keys will be the location(i.e : top-left,mid-right,etc.)
# and initialliy it's values will be numbered in the range from 1 - 9, after every move 
# we can change the value according to player's choice of move. 
Display = {'1': '1' , '2': '2' , '3': '3' ,
            '4': '4' , '5': '5' , '6': '6' ,
            '7': '7' , '8': '8' , '9': '9' }

Display_keys = []

for key in Display:
    Display_keys.append(key) 


# We will have to print the updated display after every move in the game
# so we need to print the printDisplay function
# so that we can easily print the board everytime by calling this function.

def printDisplay(display):
    print(display['1'] + '|' + display['2'] + '|' + display['3'])
    print('-+-+-')
    print(display['4'] + '|' + display['5'] + '|' + display['6'])
    print('-+-+-')
    print(display['7'] + '|' + display['8'] + '|' + display['9'])

# Now we'll write the main function which has all the gameplay functionality.
def main():

    turn = 'X'
    count = 0


    for i in range(10):
        printDisplay(Display)
        print(Fore.WHITE + f"{turn}'s turn to choose a square (1-9):")

        move = input()        

        if Display[move] == '1' or Display[move] == '2'or Display[move] == '3'or Display[move] == '4'or Display[move] == '5'or Display[move] == '6'or Display[move] == '7'or Display[move] == '8'or Display[move] == '9':
            Display[move] = turn
            count +=1
        else:
            print(Fore.RED + "That place is already filled.\nPlease select another number")
            continue

        # Checking if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if Display['7'] == Display['8'] == Display['9'] != ' ': 
                print(Fore.RED + "\nGame Over\n")                
                print(Fore.GREEN + " _________ " +turn + " won  _________ ")                
                break
            elif Display['4'] == Display['5'] == Display['6'] != ' ': 
                printDisplay(Display)
                print(Fore.RED + "\nGame Over\n")                
                print(Fore.GREEN + " _________ " +turn + " won _________ ")
                break
            elif Display['1'] == Display['2'] == Display['3'] != ' ': 
                printDisplay(Display)
                print(Fore.RED + "\nGame Over\n")                
                print(Fore.GREEN + "  _________  " +turn + " won  _________ ")
                break
            elif Display['1'] == Display['4'] == Display['7'] != ' ': 
                print(Fore.RED + "\nGame Over\n")                
                print(Fore.GREEN + "  _________  " +turn + " won  _________ ")
                break
            elif Display['2'] == Display['5'] == Display['8'] != ' ': 
                printDisplay(Display)
                print(Fore.RED + "\nGame Over\n")                
                print(Fore.GREEN + "  _________  " +turn + " won  _________ ")
                break
            elif Display['3'] == Display['6'] == Display['9'] != ' ': 
                printDisplay(Display)
                print(Fore.RED + "\nGame Over\n")                
                print(Fore.GREEN + "  _________  " +turn + " won  _________ ")
                break 
            elif Display['7'] == Display['5'] == Display['3'] != ' ':
                printDisplay(Display)
                print(Fore.RED + "\nGame Over\n")                
                print(Fore.GREEN + "  _________  " +turn + " won  _________ ")
                break
            elif Display['1'] == Display['5'] == Display['9'] != ' ': 
                printDisplay(Display)
                print(Fore.RED + "\nGame Over\n")                
                print(Fore.GREEN + "  _________  " +turn + " won  _________ ")
                break 

        # If neither X or O wins and the Display is full, we will declare the result as 'tie'.
        if count == 9:
            print("\nGame Over\n")                
            print(Fore.BLUE + "It's a Tie!!")
            restart = input(Fore.GREEN + "Do you want to play Tic-Tac-Toe?(y/n)")
            while restart =="y" :  
                for key in Display_keys:
                    Display[key] = key
                main()
            if restart == "n":
                print("Good game. Thanks for playing!")
            

        # changing player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart or end game

    restart = input(Fore.GREEN + "Do you want to play Tic-Tac-Toe?(y/n)")
    while restart =="y" :  
        for key in Display_keys:
            Display[key] = key
        main()
    if restart == "n":
        print("Good game. Thanks for playing!")
       

if __name__ == "__main__":
    main()