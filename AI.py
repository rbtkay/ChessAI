import random
from Move import Move
from game import is_king_dead
import coefficient as coef


def evaluate(board, does_need_coeficient):
    total_score = 0
    for i in board:
        if i is not None:
            if does_need_coeficient:
                total_score += (i.value) * coef.coeficient[i.piece_type][i.current_index]
            else:
                total_score += (i.value)

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
    board[origin] = None

    return board

def ai_move(board, is_smart: bool = False, depth: int = 1, does_need_coeficient: bool = False):
    move = None

    if is_smart:
        move, value = minmax(depth=depth, alpha=-999999, beta=999999, board=board, is_max=False, does_need_coeficient=does_need_coeficient)
    else:
        possible_moves = get_possible_moves(board, "black")
        move = random_move(possible_moves=possible_moves)
    

    return (move)


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



def minmax(depth, alpha, beta, board, is_max, does_need_coeficient):
    if depth <= 0:
        return (None, evaluate(board, does_need_coeficient)) # int

    color = "white" if is_max else "black"

    possible_pieces_to_moves = get_possible_moves(board, color)

    if is_max:
        # print("max")
        best_value = -9999
        best_move = None

        if len(possible_pieces_to_moves) == 0:
            return (None, -900)

        for piece in possible_pieces_to_moves:
            for i in piece["moves"]:
                new_board = board.copy()
                v_board = move_on_virtual_board(board=new_board, origin=piece["index"], destination=i)
                
                current_move, value = minmax(depth=(depth -1), alpha=alpha, beta=beta, board=v_board.copy(), is_max=(not is_max), does_need_coeficient=does_need_coeficient)

                if value > best_value:
                    best_value = value
                    previous_move = Move(piece["index"], i)
                    best_move = Move(piece["index"], i)
                
                alpha = best_value if best_value > alpha else alpha

                if(beta <= alpha):
                    return (best_move, best_value)

        return (best_move, best_value)

    if not is_max:
        best_value = 9999
        best_move = None

        if len(possible_pieces_to_moves) == 0:
            return (None, 900)

        for piece in possible_pieces_to_moves:
            print(piece["moves"])
            for i in piece["moves"]:
                new_board = board.copy()
                v_board = move_on_virtual_board(board=new_board, origin=piece["index"], destination=i)

                current_move, value = minmax(depth=(depth -1), alpha=alpha, beta=beta, board=v_board.copy(), is_max=(not is_max), does_need_coeficient=does_need_coeficient)

                if value < best_value:
                    best_value = value
                    best_move = Move(piece["index"], i)

                beta = best_value if best_value < beta else beta

                if(beta <= alpha):
                    return (best_move, best_value)
                    
        return (best_move, best_value)
        

                

        
        





# def mini
