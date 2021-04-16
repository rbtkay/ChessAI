from tkinter import *
from Piece import Piece
from functools import partial
from AI import evaluate, get_possible_moves, move_on_virtual_board, ai_move
from game import is_check, display_virtual_board, get_virtual_board, move_piece_in_virtual_board
import random
from Move import Move

DOES_AI_MOVE = True
IS_AI_SMART = True
DOES_NEED_COEFICIENT = True
AI_DEPTH = 4

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


def get_color(is_selected):
    if is_selected == False: return None
    else: return 'yellow'


def change_turn():
    global playing_color    # row = int(move_chosen / 8)
    # column = move_chosen - int(row * 8)
    # move_piece(destination_index=move_chosen, row=(row+1), column=column)
    global current_selected

    playing_color = "black" if playing_color == "white" else "white"

    if playing_color == "black" and DOES_AI_MOVE: 
        move = ai_move(board.copy(), IS_AI_SMART, AI_DEPTH, does_need_coeficient=DOES_NEED_COEFICIENT)
        if move is None:
            print("check mate")
        else:
            current_selected = move.origin
            row = int(move.destination / 8)
            column = move.destination - int(row * 8)
            move_piece(destination_index=move.destination, row=(row+1), column=column)


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
    # virtula board
    board[destination_index] = board[current_selected]
    board[destination_index].set_index(destination_index)
    board[current_selected] = None
    
    move_piece_on_board(destination_index=destination_index, row=row, column=column)

    change_turn()

def move_piece_on_board(destination_index, row, column):
    # enemy get eaten if we pass over it
    if pieces_on_board[destination_index] is not None: 
        pieces_on_board[destination_index].grid_forget()
    
    # ui board
    btn = Button(root, image=board[destination_index].image, command=partial(handle_click,  piece=board[destination_index], index=destination_index, row=row, column=column))
    btn.grid(row=row, column=column)
    pieces_on_board[destination_index] = btn
    pieces_on_board[current_selected].grid_forget()


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
root.title("Chess Game")

labels = []
labels_initial_colors = []
possible_moves = []
pieces_on_board = [None]*64
current_selected = None
playing_color = "white"

board = init_game()

display_board(board)

root.mainloop()
