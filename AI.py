import random
from Move import Move
from game import display_virtual_board

def evaluate(board):
    total_score = 0
    for i in board:
        if i is not None:
            total_score += i.value

    return total_score


def get_possible_moves(board, color):
    available_moves = []
    for i in board:
        if i is not None and i.color == color:
            ai_legal_moves = i.get_legal_moves(board, color)
            if len(ai_legal_moves) > 0:
                move = {}
                move["index"] = i.current_index
                move["moves"] = ai_legal_moves
                available_moves.append(move)
    
    return available_moves

def move_on_virtual_board(board, origin, destination):
    board[destination] = board[origin]
    # board[destination].set_index(destination)
    board[origin] = None

    return board

def ai_move(board, is_smart: bool = False):
    move = None

    if is_smart:
        # move = smart_move(board=board)
        move, value = minmax(depth=4, alpha=-999999, beta=999999, board=board, is_max=False)
    else:
        possible_moves = get_possible_moves(board, "black")
        move = random_move(possible_moves=possible_moves)
    

    return move


def random_move(possible_moves):
    piece_chosen = random.randrange(0, len(possible_moves))
    move_chosen_index = random.randrange(0, len(possible_moves[piece_chosen]["moves"]))

    move = Move(
        possible_moves[piece_chosen]["index"],
        possible_moves[piece_chosen]["moves"][move_chosen_index]
    )

    return move


def smart_move(board):
    best_move = None
    best_value = 9999

    possible_moves = get_possible_moves(board, "black")

    for move in possible_moves:
        for i in move["moves"]:
            new_board = board.copy()
            v_board = move_on_virtual_board(board=new_board, origin=move["index"], destination=i)
            score = evaluate(v_board)

            if(score < best_value):
                best_value = score
                best_move = Move(move["index"], i)

            new_board = None

    return best_move


def minmax(depth, alpha, beta, board, is_max):
    if depth <= 0:
        return (None, evaluate(board)) # int

    if is_max:
        print("max")
        possible_moves = get_possible_moves(board, "white")
        best_value = -9999
        best_move = None

        for move in possible_moves:
            for i in move["moves"]:
                new_board = board.copy()
                v_board = move_on_virtual_board(board=new_board, origin=move["index"], destination=i)
                current_move, value = minmax(depth=(depth -1), alpha=alpha, beta=beta, board=v_board.copy(), is_max=(not is_max))

                if value > best_value:
                    best_value = value
                    best_move = Move(move["index"], i)
                
                alpha = best_value if best_value > alpha else alpha

                if(beta <= alpha):
                    return (best_move, best_value)

        return (best_move, best_value)

    if not is_max:
        print("min")
        possible_moves = get_possible_moves(board, "black")

        best_value = 9999
        best_move = None

        for move in possible_moves:
            for i in move["moves"]:
                new_board = board.copy()
                v_board = move_on_virtual_board(board=new_board, origin=move["index"], destination=i)
                current_move, value = minmax(depth=(depth -1), alpha=alpha, beta=beta, board=v_board.copy(), is_max=(not is_max))

                if value < best_value:
                    best_value = value
                    best_move = Move(move["index"], i)

                beta = best_value if best_value < beta else beta

                if(beta <= alpha):
                    return (best_move, best_value)
                    
        return (best_move, best_value)
        

                

        
        





# def mini
