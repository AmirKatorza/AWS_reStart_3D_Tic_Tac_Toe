import random


# Function to hold the logic of the 3D Board Game
def create_board() -> dict:
    board_names = ["A", "B", "C"]
    boards_dict = {}
    for board in board_names:
        boards_dict[board] = [[' ' for _ in range(3)] for _ in range(3)]
    boards_dict["B"][1][1] = '*'  # This Option will be invalid
    return boards_dict


# Function to print 3D Tic Tac Toe Game Board
def print_board(board_dict: dict):
    for board_name, board in board_dict.items():
        print(f"Board {board_name}:")
        print("\t    1   2   3")
        print("\t  +---+---+---+")
        print("\t1 | {} | {} | {} |".format(board[0][0], board[0][1], board[0][2]))
        print("\t  +---+---+---+")
        print("\t2 | {} | {} | {} |".format(board[1][0], board[1][1], board[1][2]))
        print("\t  +---+---+---+")
        print("\t3 | {} | {} | {} |".format(board[2][0], board[2][1], board[2][2]))
        print("\t  +---+---+---+")
        print()


def get_random_first_player() -> int:
    return random.randint(0, 1)


def fix_spot(board, row, col) -> bool:
    if not board[row][col] in ["X", "O", "*"]:
        return True
    else:
        return False


def __extract_all_boards(board_dict: dict) -> dict:
    alt_board_rows = ["D", "E", "F"]
    alt_board_cols = ["G", "H", "I"]
    alt_boards_dict = {}

    for i, letter in enumerate(alt_board_rows):
        tmp_board = []
        for board in board_dict.values():
            tmp_board.append(board[i])
        alt_boards_dict[letter] = tmp_board

    for i, letter in enumerate(alt_board_cols):
        tmp_board = []
        for board in board_dict.values():
            tmp_col = []
            for j in range(3):
                tmp_col.append(board[j][i])
            tmp_board.append(tmp_col)
        alt_boards_dict[letter] = tmp_board

    return alt_boards_dict


def chk_rows(board: list, player) -> bool:
    win = None
    for i in range(3):
        win = True
        for j in range(3):
            if board[i][j] != player:
                win = False
                break
        if win:
            return win
    return win


def chk_cols(board: list, player) -> bool:
    win = None
    for i in range(3):
        win = True
        for j in range(3):
            if board[j][i] != player:
                win = False
                break
        if win:
            return win
    return win


def chk_primary_diagonal(board: list, player) -> bool:
    win = True
    for i in range(3):
        if board[i][i] != player:
            win = False
            break
    return win


def chk_secondary_diagonal(board: list, player) -> bool:
    win = True
    for i in range(3):
        if board[i][3 - 1 - i] != player:
            win = False
            break
    return win


def is_win(board_dict: dict, player) -> bool:
    all_boards = board_dict | __extract_all_boards(board_dict)
    for board in all_boards.values():
        if chk_rows(board, player) or chk_cols(board, player) \
                or chk_primary_diagonal(board, player) or chk_primary_diagonal(board, player) or \
                chk_secondary_diagonal(board, player):
            return True
    return False


def is_board_filled(board_dict: dict) -> bool:
    for board in board_dict.values():
        for row in board:
            for item in row:
                if item == ' ':
                    return False
    return True


def swap_player_turn(player):
    return 'Player1' if player == 'Player2' else 'Player2'
