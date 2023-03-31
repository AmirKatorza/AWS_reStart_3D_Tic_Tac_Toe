import re
import pandas as pd
from functions import *


def main():
    df = pd.read_csv('score_board.csv')
    print("Player 1")
    name1 = input("Please Enter your name : ")
    if name1 in df['Name'].values:
        print(f"Welcome back {name1}\n")
    else:
        df.loc[len(df.index)] = [name1, 0]
        print(f"{name1} nice to meet you for the first time, have fun!")

    print("Player 2")
    name2 = input("Please Enter your name : ")
    if name2 in df['Name'].values:
        print(f"Welcome back {name2}\n")
    else:
        df.loc[len(df.index)] = [name2, 0]
        print(f"{name2} nice to meet you for the first time, have fun!")

    players_dict = {"Player1": ['X', name1], "Player2": ['O', name2]}
    current_player = "Player1" if get_random_first_player() == 1 else "Player2"
    print(f"{current_player} will go first!")

    main_board = create_board()
    print_board(main_board)

    choose_board = input(f"{players_dict[current_player][1]}, choose your board: ")
    while re.match("^[^ABC]$", choose_board):
        print("Invalid input, Please try Again!")
        choose_board = input(f"{players_dict[current_player][1]}, choose your board [A, B, C]: ")


def start(self):
    self.create_board()

    player = 'X' if self.get_random_first_player() == 1 else 'O'
    while True:
        print(f"Player {player} turn")

        self.show_board()

        # taking user input
        row, col = list(
            map(int, input("Enter row and column numbers to fix spot: ").split()))
        print()

        # fixing the spot
        self.fix_spot(row - 1, col - 1, player)

        # checking whether current player is won or not
        if self.is_player_win(player):
            print(f"Player {player} wins the game!")
            break

        # checking whether the game is draw or not
        if self.is_board_filled():
            print("Match Draw!")
            break

        # swapping the turn
        player = self.swap_player_turn(player)

    # showing the final view of board
    print()
    self.show_board()


if __name__ == "__main__":
    main()
