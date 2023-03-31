import pandas as pd

df = pd.read_csv('score_board.csv')



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


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
