# ##################### functions ###################################
def greeting():
    print("𝐰𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐄𝐲𝐚𝐥'𝐬 𝐓𝐈𝐂-𝐓𝐀𝐂-𝐓𝐎𝐄 𝐠𝐚𝐦𝐞")

def start_game():
    player_1 = str(input("player 1 please  enter your name or nickname"))
    player_2 = str(input("player 2 please  enter your name or nickname"))
    while True:
        board_size = input("please enter board size from 3 to 9")
        if board_size.isdigit():
            if int(board_size) < 2:
                print("board size must be between 3 to 9")
                continue
            else:
                break
        else:
            print("board size must be a number")
            continue
    board_size = int(board_size)
    board = [['_'] * board_size for i in range(board_size)]
    taken_moves = set()
    range_of_moves = [str(i) for i in range(len(board[0]))]
    while True:
        display_board(board)
        while True:
            invalidmove: bool = False
            player1 = input(f"it's {player_1} turn, choose (horizontal,column)")
            if player1 in taken_moves:
                invalidmove = True
                print("move already taken,choose another one")
            move1 = player1.split(',')
            if len(move1) != 2:
                invalidmove = True
                print("invalid move")
            else:
                if move1[0] not in range_of_moves or move1[1] not in range_of_moves:
                    invalidmove = True
                    print("invalid move")
            if player1 not in taken_moves and not invalidmove:
                break
        taken_moves.add(player1)
        board[int(move1[0])][int(move1[1])] = '❌'
        if check_board(board) == 1:
            display_board(board)
            print(f"{player_1} won!!")
            end_game()
        if board_full(board):
            display_board(board)
            print("ITS A-TIE!!")
            end_game()

        display_board(board)
        while True:
            invalidmove: bool = False
            player2 = input(f"it's {player_2} turn,choose(horizontal,column)")
            if player2 in taken_moves:
                print("move already taken,choose another one")
                continue
            move2 = player2.split(',')
            if len(move2) != 2:
                print("invalid move")
                continue
            else:
                if move2[0] not in range_of_moves or move2[0] not in range_of_moves:
                    print("invalid move")
                    continue
            if player2 not in taken_moves and not invalidmove:
                break
        taken_moves.add(player2)
        board[int(move2[0])][int(move2[1])] = '🟢'
        if check_board(board) == 2:
            display_board(board)
            print(f"{player_2} won!!")
            end_game()
        if board_full(board):
            display_board(board)
            print("ITS A-TIE!!")
            end_game()


def check_board(board):
    nums_to_win = len(board[0])
    # horizontal check:
    for row in board:
        x_count = count_moves(row, '❌')
        o_count = count_moves(row, '🟢')
        if x_count == nums_to_win:
            return 1
        if o_count == nums_to_win:
            return 2
    # check vertical:
    for i, col in enumerate(board):
        col_to_check = [col[i] for col in board]
        x_count = count_moves(col_to_check, '❌')
        o_count = count_moves(col_to_check, '🟢')
        if o_count == nums_to_win:
            return 2
        if x_count == nums_to_win:
            return 1
            # check left alahson:
        left_alahson = [column[i + 1] for i, column in enumerate(board, -1)]
        l_alahson_x_count = count_moves(left_alahson, '❌')
        l_alahson_o_count = count_moves(left_alahson, '🟢')
        if l_alahson_o_count == nums_to_win:
            return 2
        if l_alahson_x_count == nums_to_win:
            return 1
    # check right alahson:
        right_alahson = [column[eval('i') - 1] for i, column in enumerate(board)]
        right_alahson_x_count = count_moves(right_alahson, '❌')
        right_alahson_o_count = count_moves(right_alahson, '🟢')
        if right_alahson_o_count == nums_to_win:
            return 2
        if right_alahson_x_count == nums_to_win:
            return 1


def display_board(board):
    for i in range(len(board[0])):
        print(f'    {i}', end="")
    print()
    for i, j in enumerate(board):
        print(f"{i} {j}")
    print()


def board_full(board):
    for row in board:
        if '_' in row:
            return False
    return True


def end_game():
    while True:
        keep_playing = input("enter: 'ok' to play again or press enter to quit").lower().strip()
        if keep_playing == 'ok':
            start_game()
            break


def count_moves(array, move):
    count = 0
    for s in array:
        if s == move:
            count += 1
    return count


if __name__ == "__main__":
    greeting()
    start_game()
