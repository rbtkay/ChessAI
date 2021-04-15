from Piece import Piece

def init_game():
    board = [None]*64
    board[0] = Piece("Rook", "black", 0)
    board[7] = Piece("Rook", "black", 7)

    board[1] = Piece("Knight", "black", 1)
    board[6] = Piece("Knight", "black", 6)
    
    board[2] = Piece("Bishop", "black", 2)
    board[5] = Piece("Bishop", "black", 5)

    board[3] = Piece("Queen", "black", 3)
    board[4] = Piece("King", "black", 4)

    for i in range(8,16):
        board[i] = Piece("Pawn", "black", i)

    ### white pieces
    board[56] = Piece("Rook", "white", 56)
    board[63] = Piece("Rook", "white", 63)

    board[57] = Piece("Knight", "white", 57)
    board[62] = Piece("Knight", "white", 62)
    
    board[58] = Piece("Bishop", "white", 58)
    board[61] = Piece("Bishop", "white", 61)

    board[59] = Piece("Queen", "white", 59)
    board[60] = Piece("King", "white", 60)

    for i in range(48,56):
        board[i] = Piece("Pawn", "white", i)

    return board


def is_check(playing_color: str, board):
    print("in the check function")
    display_virtual_board(board)
    
    print("playing color -- ", playing_color)
    king_index = get_king_index(playing_color, board)
    
    opponent_moves = get_opponent_moves(playing_color=playing_color, board=board)
    print("opponent_moves")
    print(opponent_moves)



    print("in the check function")
    display_virtual_board(board)


    print(king_index)

    if king_index in opponent_moves:
        print("check")
        return True
    return False


def get_king_index(playing_color: str, board):
    for i in board:
        if i is not None and i.color == playing_color and i.piece_type == "King":
            return i.current_index


def get_opponent_moves(playing_color: str, board):
    opponent_moves = []
    for i in board:
        if i is not None and i.color != playing_color: 
            for move in i.get_legal_moves(board, playing_color, True):
                opponent_moves.append(move)

    return opponent_moves     

def get_virtual_board(board):
    v_board = board.copy()

    display_virtual_board(board)

    return v_board


def display_virtual_board(board):
    result = ""
    count = -1
    
    for i in board:
        if count == 7:
            enter = "\n" 
            count = 0
        else:
            enter = ""
            count += 1

        if i is not None:
            result += enter + "|"+ i.piece_type[0]
        else: result += enter + "| "

    print(result + "\n\n")


def move_piece_in_virtual_board(board, initial, destination):
    piece = board[initial]
    piece.current_index = destination
    board[initial] = None
    board[destination] = piece