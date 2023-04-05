import os
import re
from tqdm import tqdm
import time
from functions import *


def start_game():
    print("\n-------------Start Game - Tic-Tac-Toe-------------\n")

    print("Player 1 - X")
    name1 = input("Please Enter your name : ")
    create_user(name1)

    while True:
        player2_choice = input("Who would you like to play against:\n0 - Human Player\n1 - Computer\n")
        if re.match("^[01]$", player2_choice):
            break
        else:
            print("Invalid choice, please try again")

    if int(player2_choice) == 0:
        print("Player 2 - O")
        name2 = input("Please Enter your name : ")
        create_user(name2)
    else:
        print("You chose to play against the computer - Good Luck!\n")
        name2 = "COMP"

    players_dict = {"Player1": ['X', name1], "Player2": ['O', name2]}

    print("Who will go first?")
    # Add progress bar of 5 seconds
    shuffle_bar = tqdm(range(100), desc="Shuffling Players...")
    for _ in shuffle_bar:
        time.sleep(0.01)

    current_player = "Player1" if get_random_first_player() == 1 else "Player2"
    print(f"\n{current_player}, {players_dict[current_player][1]}, will go first!\n")

    print("Initializing board!")
    # Add progress bar of 5 seconds
    init_bar = tqdm(range(100), desc="Initializing...")
    for _ in init_bar:
        time.sleep(0.01)

    print()

    main_board = create_board()
    while True:
        # os.system('cls' if os.name == 'nt' else 'clear')

        print_board(main_board)

        if players_dict[current_player][1] == "COMP":
            free_cells = get_free_cells(main_board)
            rand_choice = random.choice(free_cells)
            print("Computer is making its move!\n")
            main_board[rand_choice.board][rand_choice.row][rand_choice.col] = players_dict[current_player][0]
        else:
            print(f"{current_player} - {players_dict[current_player][1]}, ", end="")
            print(f"where would you like to place your {players_dict[current_player][0]}?")
            while True:
                choose_board = input("choose your board [A, B, C]: ")
                if re.match("^[^ABCabc]$", choose_board):
                    print("Invalid input, Please try Again!")
                else:
                    break

            while True:
                row, col = input("choose your coordinates - Enter row and column numbers for your move: ").split()
                if re.match("^[123]$", row) and re.match("^[123]$", col):
                    if fix_spot(main_board[choose_board.upper()], int(row) - 1, int(col) - 1):
                        main_board[choose_board.upper()][int(row) - 1][int(col) - 1] = players_dict[current_player][0]
                        break
                    else:
                        print("Cell is already occupied!\nPlease provide different coordinates!")
                else:
                    print("Invalid input, Please try Again!")

        # checking whether current player has won or not
        if is_win(main_board, players_dict[current_player][0]):
            print(f"{current_player} - {players_dict[current_player][1]}, wins the game!\n")
            if players_dict[current_player][1] != "COMP":
                update_score_board(players_dict[current_player][1])
            break

        # checking whether the game is draw or not
        if is_board_filled(main_board):
            print("Match Draw!\n")
            break

        # swapping the turn
        current_player = swap_player_turn(current_player)


def main():
    title = '''
             _    _        _                 _             
            | |  (_)      | |               | |            
            | |_  _   ___ | |_   __ _   ___ | |_   __     ___ 
            | __|| | / __|| __| / _` | / __|| __| / _ \\  / _ \\
            | |_ | || (__ | |_ | (_| || (__ | |_ | (_) ||  __/
             \\__||_| \\___| \\__| \\__,_| \\___| \\__| \\___/  \\___|
             '''
    print(title)

    while True:
        print("------------MENU------------")
        print("1. Start New Game ")
        print("2. Display Score Board")
        print("3. Exit")
        print("----------------------------")
        choice = input("Please make your choice: ")

        if choice == "1":
            start_game()
        elif choice == "2":
            display_scores()
        elif choice == "3":
            print("GoodBye!")
            break
        else:
            print("Invalid input, please try again!")
        # os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()
