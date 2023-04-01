import os
import re
import pandas as pd
import numpy as np
from IPython.display import display
from functions import *


def start_game():
    print("-------------Start Game - Tic-Tac-Toe-------------")

    df = pd.read_csv('score_board.csv')
    print("Player 1 - X")
    name1 = input("Please Enter your name : ")
    if name1 in df['Name'].values:
        print(f"Welcome back {name1}\n")
    else:
        df.loc[len(df.index)] = [name1, 0]
        print(f"{name1} nice to meet you for the first time, have fun!")

    print("Player 2 - O")
    name2 = input("Please Enter your name : ")
    if name2 in df['Name'].values:
        print(f"Welcome back {name2}\n")
    else:
        df.loc[len(df.index)] = [name2, 0]
        print(f"{name2} nice to meet you for the first time, have fun!")

    players_dict = {"Player1": ['X', name1], "Player2": ['O', name2]}

    print("Who will go first? Shuffling Players...")
    # TODO: Add progress bar of 10 seconds
    current_player = "Player1" if get_random_first_player() == 1 else "Player2"
    print(f"{current_player}, {players_dict[current_player][1]}, will go first!")

    print("Initializing board...")
    # TODO: Add progress bar of 10 seconds
    main_board = create_board()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print_board(main_board)

        print(
            f"{current_player} - {current_player[current_player][1]}, where would you like to place your {current_player[current_player][0]}?")
        while True:
            choose_board = input("choose your board [A, B, C]: ")
            if re.match("^[^ABCabc]$", choose_board):
                print("Invalid input, Please try Again!")
                # choose_board = input(f"{players_dict[current_player][1]}, choose your board [A, B, C]: ")
            else:
                break

        while True:
            row, col = input("choose your coordinates - Enter row and column numbers to fix a spot: ").split()
            if re.match("^[123]$", row) and re.match("^[123]$", col):
                if fix_spot(main_board[choose_board], int(row) - 1, int(col) - 1, players_dict[current_player][0]):
                    main_board[choose_board][int(row) - 1][int(col) - 1] = players_dict[current_player][0]
                    break
                else:
                    print("Cell is already occupied!\nPlease provide different coordinates!")
            else:
                print("Invalid input, Please try Again!")

    #         # checking whether current player is won or not
    #         if self.is_player_win(player):
    #             print(f"Player {player} wins the game!")
    #             break
    #
    #         # checking whether the game is draw or not
    #         if self.is_board_filled():
    #             print("Match Draw!")
    #             break
    #
    #         # swapping the turn
    #         player = self.swap_player_turn(player)
    #
    #     # showing the final view of board
    #     print()
    #     self.show_board()


def display_scores():
    df = pd.read_csv("score_board.csv")
    df.sort_values(by="Score", ascending=False, inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.index = np.arange(1, len(df) + 1)
    display(df)


def main():
    while True:
        title = '''
         _   _      _             _             
        | | (_)    | |           | |            
        | |_ _  ___| |_ __ _  ___| |_ ___   ___ 
        | __| |/ __| __/ _` |/ __| __/ _ \\ / _ \\
        | |_| | (__| || (_| | (__| || (_) |  __/
         \\__|_|\\___|\\__\\__,_|\\___|\\__\\___/ \\___|
         '''
        print(title)
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
            break
        else:
            print("Invalid input, please try again!")


if __name__ == "__main__":
    main()
