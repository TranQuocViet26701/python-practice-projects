current_player = "X"

# TODO: Print board
board = ["-"] * 9
def print_board(board: list) -> None:
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print(f"-----------")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print(f"-----------")
    print(f" {board[6]} | {board[7]} | {board[8]}")

    
# TODO: Take player input    
def take_input(board: list, player: str) -> None:
    print(f"Player {player}")
    player_input = int(input("It's your turn, please choose a number from 1 -> 9: "))
    while not (player_input > 0 and player_input < 10):
        print("Wrong number, please choose again!")
        player_input = int(input("It's your turn, please choose a number from 1 -> 9: "))
        
    current_index = player_input - 1
    current_value = board[current_index]
    if current_value == "-":
        board[current_index] = player
    else:
        print("This number has chosen, please try again!")
        take_input(player)


# TODO: Check win
def check_win(board: list) -> bool:
    # Check column
    for i in range(0, 3):
        column = [board[i], board[i + 3], board[i + 6]]
        if "-" not in column and len(set(column)) == 1:
            return True
    
    # Check row
    i = 0
    while i < 9:
        row = board[i:i + 3]
        if "-" not in row and len(set(row)) == 1:
            return True
        else:
            i += 3
    
    # Check diagonal
    diagonal1 = [board[0], board[4], board[8]]
    diagonal2 = [board[2], board[4], board[6]]
    if "-" not in diagonal1 and len(set(diagonal1)) == 1:
            return True
    if "-" not in diagonal2 and len(set(diagonal2)) == 1:
            return True
    
    return False
    
    
# TODO: Check draw
def check_draw(board: list):
    return True if "-" not in board else False


# TODO: Switch player
def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


game_over = False
while not game_over:
    print_board(board=board)
    take_input(board, current_player)
    if check_win(board=board):
        print(f"Player {current_player} won!")
        break
    if check_draw(board=board):
        print("It's draw.")
        break
    switch_player()
    
