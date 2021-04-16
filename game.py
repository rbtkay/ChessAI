
def is_check(playing_color: str, board):
    for i in board:
        if i is not None and i.color == playing_color and i.piece_type == "King":
            king = board.index(i)
    try:
        king_y = int(king / 8)
        king_x = int(king - (king_y * 8))
    except:
        return True

    # print(playing_color)
    # print("king x", king_x)
    # print("king y", king_y)

    danger_zones = [
                [king_x+2, king_y+1],
                [king_x+2, king_y-1],
                [king_x-2, king_y+1],
                [king_x-2, king_y-1],
                [king_x+1, king_y+2],
                [king_x+1, king_y-2],
                [king_x-1, king_y+2],
                [king_x-1, king_y-2],
    ]

    for i in danger_zones:
        current_index = i[1] * 8 + i[0]
        # print("current index")
        # print(current_index)
        # print("danger coordinates")
        # print(i[0])
        # print(i[1])
        if 0 <= current_index < 64: 
            if board[current_index] is not None:
                if board[current_index].color != playing_color and board[current_index].piece_type == "Knight":
                    return True

    # check for Bishop
    x_1 = king_x+1 
    y_1 = king_y+1
    new_index = y_1 * 8 + x_1
    while 0 <= x_1 < 8 and 0 <= y_1 < 8:
        if board[new_index] is not None:
            if board[new_index].color != playing_color and board[new_index].piece_type == "Bishop":
                return True
            break
                    
        x_1 += 1
        y_1 += 1
        new_index = y_1 * 8 + x_1

    x_2 = king_x-1 
    y_2 = king_y-1
    new_index = y_2 * 8 + x_2
    while 0 <= x_2 < 8 and 0 <= y_2 < 8:
        if board[new_index] is not None:
            if board[new_index].color != playing_color and board[new_index].piece_type == "Bishop":
                return True
            break    
        x_2 -= 1
        y_2 -= 1
        new_index = y_2 * 8 + x_2


    x_3 = king_x+1 
    y_3 = king_y-1
    new_index = y_3 * 8 + x_3
    while 0 <= x_3 < 8 and 0 <= y_3 < 8:
        if board[new_index] is not None:
            if board[new_index].color != playing_color and board[new_index].piece_type == "Bishop":
                return True
            break
        x_3 += 1
        y_3 -= 1  
        new_index = y_3 * 8 + x_3


    x_4 = king_x-1 
    y_4 = king_y+1
    new_index = y_4 * 8 + x_4
    while 0 <= x_4 < 8 and 0 <= y_4 < 8:
        if board[new_index] is not None:
            if board[new_index].color != playing_color and board[new_index].piece_type == "Bishop":
                return True
            break
        x_4 -= 1
        y_4 += 1
        new_index = y_4 * 8 + x_4

    
    # check for rook
    x_1 = king_x 
    y_1 = king_y+1
    new_index = y_1 * 8 + x_1
    while 0 <= x_1 < 8 and 0 <= y_1 < 8:
        if board[new_index] is not None:
            if board[new_index].color != playing_color and board[new_index].piece_type == "Rook":
                return True
            break
        y_1 += 1
        new_index = y_1 * 8 + x_1

    x_2 = king_x 
    y_2 = king_y-1
    new_index = y_2 * 8 + x_2
    while 0 <= x_2 < 8 and 0 <= y_2 < 8:
        if board[new_index] is not None:
            if board[new_index].color != playing_color and board[new_index].piece_type == "Rook":
                return True
            break
        y_2 -= 1
        new_index = y_2 * 8 + x_2

    x_3 = king_x+1 
    y_3 = king_y
    new_index = y_3 * 8 + x_3
    while 0 <= x_3 < 8 and 0 <= y_3 < 8:
        if board[new_index] is not None:
            if board[new_index].color != playing_color and board[new_index].piece_type == "Rook":
                return True
            break
        x_3 += 1
        new_index = y_3 * 8 + x_3


    x_4 = king_x-1 
    y_4 = king_y
    new_index = y_4 * 8 + x_4
    while 0 <= x_4 < 8 and 0 <= y_4 < 8:
        if board[new_index] is not None:
            if board[new_index].color != playing_color and board[new_index].piece_type == "Rook":
                return True
            break
        x_4 -= 1
        new_index = y_4 * 8 + x_4


    # check for queen
    x_1 = king_x 
    y_1 = king_y+1
    new_index = y_1 * 8 + x_1
    while 0 <= x_1 < 8 and 0 <= y_1 < 8:
        if board[new_index] is not None:
            if board[new_index].color != playing_color and board[new_index].piece_type == "Queen":
                return True
            break
        y_1 += 1
        new_index = y_1 * 8 + x_1

    x_2 = king_x 
    y_2 = king_y-1
    new_index = y_2 * 8 + x_2
    while 0 <= x_2 < 8 and 0 <= y_2 < 8:
        if board[new_index] is not None:
            if board[new_index].color != playing_color and board[new_index].piece_type == "Queen":
                return True
            break
        y_2 -= 1
        new_index = y_2 * 8 + x_2

    x_3 = king_x+1 
    y_3 = king_y
    new_index = y_3 * 8 + x_3
    while 0 <= x_3 < 8 and 0 <= y_3 < 8:
        if board[new_index] is not None:
            if board[new_index].color != playing_color and board[new_index].piece_type == "Queen":
                return True
            break
        x_3 += 1
        new_index = y_3 * 8 + x_3

    x_4 = king_x-1 
    y_4 = king_y
    new_index = y_4 * 8 + x_4
    while 0 <= x_4 < 8 and 0 <= y_4 < 8:
        if board[new_index] is not None:
            if board[new_index].color != playing_color and board[new_index].piece_type == "Queen":
                return True
            break
        x_4 -= 1
        new_index = y_4 * 8 + x_4

    x_5 = king_x+1 
    y_5 = king_y+1
    new_index = y_5 * 8 + x_5
    while 0 <= x_5 < 8 and 0 <= y_5 < 8:
        if board[new_index] is not None:
            if board[new_index].color != playing_color and board[new_index].piece_type == "Queen":
                return True
            break
        x_5 += 1
        y_5 += 1 
        new_index = y_5 * 8 + x_5

    x_6 = king_x-1 
    y_6 = king_y-1
    new_index = y_6 * 8 + x_6
    while 0 <= x_6 < 8 and 0 <= y_6 < 8:
        if board[new_index] is not None:
            if board[new_index].color != playing_color and board[new_index].piece_type == "Queen":
                return True
            break
        x_6 -= 1
        y_6 -= 1     
        new_index = y_6 * 8 + x_6

    x_7 = king_x+1 
    y_7 = king_y-1
    new_index = y_7 * 8 + x_7
    while 0 <= x_7 < 8 and 0 <= y_7 < 8:
        if board[new_index] is not None:
            if board[new_index].color != playing_color and board[new_index].piece_type == "Queen":
                return True
            break
        x_7 += 1
        y_7 -= 1  
        new_index = y_7 * 8 + x_7

    x_8 = king_x-1 
    y_8 = king_y+1
    new_index = y_8 * 8 + x_8
    while 0 <= x_8 < 8 and 0 <= y_8 < 8:
        if board[new_index] is not None:
            if board[new_index].color != playing_color and board[new_index].piece_type == "Queen":
                return True
            break
        x_8 -= 1
        y_8 += 1 
        new_index = y_8 * 8 + x_8

    # check for Pawn
    new_y = king_y + 1 if playing_color == "black" else king_y - 1
    x_1 = king_x + 1
    x_2 = king_x - 1

    new_index = new_y * 8 + x_1
    if board[new_index] is not None and board[new_index].color != playing_color and board[new_index].piece_type == "Pawn":
        return True

    new_index = new_y * 8 + x_2
    if board[new_index] is not None and board[new_index].color != playing_color and board[new_index].piece_type == "Pawn":
        return True

    return False

def is_king_dead(playing_color, board):
    for i in board:
        if i is not None and i.color != playing_color and i.piece_type == "King":
            return False
    return True

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

    # print(result + "\n\n")


def move_piece_in_virtual_board(board, initial, destination):
    piece = board[initial]
    piece.current_index = destination
    board[initial] = None
    board[destination] = piece