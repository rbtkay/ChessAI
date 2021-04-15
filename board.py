from tkinter import *
from Piece import Piece
from functools import partial
from AI import evaluate, get_possible_moves, move_on_virtual_board, ai_move
from game import is_check, display_virtual_board, get_virtual_board, move_piece_in_virtual_board, init_game
import random
from Move import Move

def get_color(is_selected):
    if is_selected == False: return None
    else: return 'yellow'

def change_turn():
    global playing_color    # row = int(move_chosen / 8)
    # column = move_chosen - int(row * 8)
    # move_piece(destination_index=move_chosen, row=(row+1), column=column)
    global current_selected

    playing_color = "black" if playing_color == "white" else "white"

    if playing_color == "black": 
        # AI_possible_moves = get_possible_moves(board)

        # # ai chooses a move
        # piece_chosen = random.randrange(0, len(AI_possible_moves))
        # move_chosen_index = random.randrange(0, len(AI_possible_moves[piece_chosen]["moves"]))

        # current_selected = AI_possible_moves[piece_chosen]["index"]
        # move_chosen = AI_possible_moves[piece_chosen]["moves"][move_chosen_index]

        # move = ai_move(board)
        # v_board = move_on_virtual_board(board=board.copy(), origin=move.origin, destination=move.destination)
        # display_virtual_board(v_board)

        move = ai_move(board.copy(), True)

        # display_virtual_board(board)
        
        current_selected = move.origin
        row = int(move.destination / 8)
        column = move.destination - int(row * 8)
        move_piece(destination_index=move.destination, row=(row+1), column=column)

        
        # ai tries its different moves
        # minimum = 999999
        # optimal_move = {}
        # for move in AI_possible_moves:
        #     selected = move["index"]
        #     for i in move["moves"]:
        #         print(selected)
        #         print(i)
        #         v_board = board.copy()
        #         move_piece_in_virtual_board(v_board, selected, i)
        #         display_virtual_board(v_board)
        #         evaluation = evaluate(v_board)
        #         if evaluation < minimum:
        #             minimum = evaluation
        #             optimal_move["initial"] = selected
        #             optimal_move["destination"] = i

        # print(optimal_move)     

def display_board(board):
    global pieces_on_board
    row = 0
    column = 0
    current_color = 'white'

    for i in range(0, len(board)):
        current_color = 'black' if current_color == 'white' else 'white'

        if(i % 8 == 0):
            row += 1
            column = 0
            current_color = 'black' if current_color == 'white' else 'white'
        else:
            column += 1

        label = Label(root, width='10', height='5', bg=current_color, text=i)

        label.grid(row=row, column=column)

        label.bind("<Button>", partial(handle_label_click, row=row, column=column))

        labels.append(label)
        labels_initial_colors.append(current_color)

        if(board[i] is not None):
            btn = Button(root, image=board[i].image, command=partial(handle_click,  piece=board[i], index=i, row=row, column=column))
            btn.grid(row=row, column=column)
            pieces_on_board[i] = btn


def move_piece(destination_index, row, column):
    # enemy get eaten if we pass over it
    if pieces_on_board[destination_index] is not None: 
        pieces_on_board[destination_index].grid_forget()

    # virtula board
    board[destination_index] = board[current_selected]
    board[destination_index].set_index(destination_index)
    board[current_selected] = None

    # ui board
    btn = Button(root, image=board[destination_index].image, command=partial(handle_click,  piece=board[destination_index], index=destination_index, row=row, column=column))
    btn.grid(row=row, column=column)
    pieces_on_board[destination_index] = btn
    pieces_on_board[current_selected].grid_forget()

    # display_virtual_board(board)
    change_turn()

def handle_label_click(event, row, column):
    destination_index = (row-1) * 8 + column
    if destination_index in possible_moves:
        move_piece(destination_index=destination_index, row=row, column=column)

    remove_label_selection()


def remove_label_selection():
    global current_selected

    if current_selected is not None:
        for i in range(0, len(labels)):
            labels[i].config(bg=labels_initial_colors[i])
    
    current_selected = None


def handle_click(piece: Piece, index: int, row, column):
    global current_selected
    global possible_moves
    global playing_color

    # make sure the playing color only can play
    if piece.color != playing_color and current_selected is not None:
        if index in possible_moves:
            move_piece(destination_index=index, row=row, column=column)
            remove_label_selection()
        return
    elif piece.color != playing_color and current_selected is None: return

    possible_moves = []

    remove_label_selection()

    labels[index].config(bg='yellow')
    current_selected = index

    legal_moves = piece.get_legal_moves(board=board, playing_color=playing_color)

    if legal_moves is not None:
        for i in legal_moves:
            labels[i].config(bg='green')
            possible_moves.append(i)


root = Tk()

labels = []
labels_initial_colors = []
possible_moves = []
pieces_on_board = [None]*64
current_selected = None
playing_color = "white"

board = init_game()

display_board(board)
# display_virtual_board(board)

root.mainloop()


# [
# <tkinter.Button object .!button>,
# <tkinter.Button object .!button2>
#   <tkinter.Button object .!button3>
#   <tkinter.Button object .!button4>
#   <tkinter.Button object .!button5>
#   <tkinter.Button object .!button6>
#   <tkinter.Button object .!button7>
#   <tkinter.Button object .!button8>
#   <tkinter.Button object .!button9>
#   <tkinter.Button object .!button10>
#   <tkinter.Button object .!button11>
#   <tkinter.Button object .!button12>
#   <tkinter.Button object .!button13>
#   <tkinter.Button object .!button14>
#   <tkinter.Button object .!button15>
#   <tkinter.Button object .!button16>
#   None
#   None
#   None
#   None
#   None
#   None
#   None
#   None
#   None
#   None
#   None
#   None
#   None
#   None
#   None
#   None
#   None
#   None
#   None
#   None
#   None
#   None
#   None
#   None
#   None
#   None
#   None
#   None
#   None
#   None
#   None
#   None
#   <tkinter.Button object .!button17>
#   <tkinter.Button object .!button18>
#   <tkinter.Button object .!button19>
#   <tkinter.Button object .!button20>
#   <tkinter.Button object .!button21>
#   <tkinter.Button object .!button22>
#   <tkinter.Button object .!button23>
#   <tkinter.Button object .!button24>
#   <tkinter.Button object .!button25>
#   <tkinter.Button object .!button26>
#   <tkinter.Button object .!button27>
#   <tkinter.Button object .!button28>
#   <tkinter.Button object .!button29>
#   <tkinter.Button object .!button30>
#   <tkinter.Button object .!button31>
#   <tkinter.Button object .!button32>]