from PIL import Image, ImageTk
from game import is_check
from AI import move_on_virtual_board

KINGS = {
    "black": {"position": 4, "conditions": [5, 6], "rook": 7, "result": 6},
    "white": {"position": 60, "conditions": [61, 62], "rook": 63, "result": 62}
}


class Piece:
    def __init__(self, piece_type, color, index):
        self.piece_type = piece_type
        self.color = color
        self.selected = False
        self.current_index = index
        if color == "black":
            if piece_type == "Pawn":
                black_pawn = Image.open("images/black-pawn.png")
                self.image = ImageTk.PhotoImage(black_pawn)
            elif piece_type == "Knight":
                black_knight = Image.open("images/black-knight.png")
                self.image = ImageTk.PhotoImage(black_knight)
            elif piece_type == "Bishop":
                black_bishop = Image.open("images/black-bishop.png")
                self.image = ImageTk.PhotoImage(black_bishop)
            elif piece_type == "Rook":
                black_rook = Image.open("images/black-rook.png")
                self.image = ImageTk.PhotoImage(black_rook)
            elif piece_type == "Queen":
                black_queen = Image.open("images/black-queen.png")
                self.image = ImageTk.PhotoImage(black_queen)
            elif piece_type == "King":
                black_king = Image.open("images/black-king.png")
                self.image = ImageTk.PhotoImage(black_king)
        elif color == 'white':
            if piece_type == "Pawn":
                white_pawn = Image.open("images/white-pawn.png")
                self.image = ImageTk.PhotoImage(white_pawn)
            elif piece_type == "Knight":
                white_knight = Image.open("images/white-knight.png")
                self.image = ImageTk.PhotoImage(white_knight)
            elif piece_type == "Bishop":
                white_bishop = Image.open("images/white-bishop.png")
                self.image = ImageTk.PhotoImage(white_bishop)
            elif piece_type == "Rook":
                white_rook = Image.open("images/white-rook.png")
                self.image = ImageTk.PhotoImage(white_rook)
            elif piece_type == "Queen":
                white_queen = Image.open("images/white-queen.png")
                self.image = ImageTk.PhotoImage(white_queen)
            elif piece_type == "King":
                white_king = Image.open("images/white-king.png")
                self.image = ImageTk.PhotoImage(white_king)
        
        if piece_type == "Pawn":
            self.value = 10
        elif piece_type == "Knight" or piece_type == "Bishop":
            self.value = 30
        elif piece_type == "Rook":
            self.value = 50
        elif piece_type == "Queen":
            self.value = 90
        elif piece_type == "King":
            self.value = 900

        if self.color == "black": 
            self.value = self.value * (-1)

    def set_index(self, index):
        self.current_index = index

    def convert_index_to_coordinates(self):
        y = int(self.current_index / 8)
        x = int(self.current_index - (y * 8))
        return (x, y)


    def get_legal_moves(self, board, playing_color, is_response: bool = False):
        x, y = self.convert_index_to_coordinates()
        legal_moves = []

        if self.piece_type == "Pawn": # implement the en-passant
            new_y = y + 1 if self.color == "black" else y - 1
            new_x = x

            new_index = new_y * 8 + new_x
            if 0 <= new_y < 8 and 0 <= new_x < 8 and board[new_index] is None:
                legal_moves.append(new_index)
                if not is_response:
                    v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                    if is_check(playing_color=playing_color, board=v_board):
                        legal_moves.pop()

            new_x = x+1
            new_index = new_y *8 + new_x
            if 0 <= new_y < 8 and  0 <= new_x < 8 and board[new_index] is not None and board[new_index].color != self.color:
                legal_moves.append(new_index)
                if not is_response:
                    v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                    if is_check(playing_color=playing_color, board=v_board):
                        legal_moves.pop()

            new_x = x-1
            new_index = new_y *8 + (x-1)
            if 0 <= new_y < 8 and 0 <= new_x < 8 and board[new_index] is not None and board[new_index].color != self.color:
                legal_moves.append(new_index)
                if not is_response:
                    v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                    if is_check(playing_color=playing_color, board=v_board):
                        legal_moves.pop()

            if self.color == "black" and y == 1 and board[new_y * 8 + x] is None:
                new_y = y+2
                new_index = new_y * 8 + x
                if board[new_index] is None:
                    legal_moves.append(new_index)
                    if not is_response:
                        v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                        if is_check(playing_color=playing_color, board=v_board):
                            legal_moves.pop()
            elif self.color == "white" and y == 6 and board[new_y * 8 + x] is None:
                new_y = y-2
                new_index = new_y * 8 + x
                if board[new_index] is None:
                    legal_moves.append(new_index)
                    if not is_response:
                        v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                        if is_check(playing_color=playing_color, board=v_board):
                            legal_moves.pop()
        if self.piece_type == "Knight":
            possible_combinations = [
                [x+2, y+1],
                [x+2, y-1],
                [x-2, y+1],
                [x-2, y-1],
                [x+1, y+2],
                [x+1, y-2],
                [x-1, y+2],
                [x-1, y-2],
            ]

            for combinaison in possible_combinations:
                if 0 <= combinaison[0] < 8 and 0 <= combinaison[1] < 8:
                    new_index = combinaison[1] * 8 + combinaison[0]
                    if board[new_index] is None or board[new_index].color != playing_color:
                        legal_moves.append(new_index)
                        if not is_response:
                            v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                            if is_check(playing_color=playing_color, board=v_board):
                                legal_moves.pop()

        if self.piece_type == "Bishop":
            x_1 = x+1 
            y_1 = y+1
            new_index = y_1 * 8 + x_1
            while 0 <= x_1 < 8 and 0 <= y_1 < 8 and (board[new_index] is None or board[new_index].color != playing_color):
                legal_moves.append(new_index)
                if not is_response:
                    v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                    if is_check(playing_color=playing_color, board=v_board):
                        legal_moves.pop()
                if board[new_index] is not None and board[new_index].color != playing_color:
                    break
                x_1 += 1
                y_1 += 1
                new_index = y_1 * 8 + x_1

            x_2 = x-1 
            y_2 = y-1
            new_index = y_2 * 8 + x_2
            while 0 <= x_2 < 8 and 0 <= y_2 < 8 and (board[new_index] is None or board[new_index].color != playing_color):
                legal_moves.append(new_index)
                if not is_response:
                    v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                    if is_check(playing_color=playing_color, board=v_board):
                        legal_moves.pop()
                if board[new_index] is not None and board[new_index].color != playing_color:
                    break    
                x_2 -= 1
                y_2 -= 1
                new_index = y_2 * 8 + x_2


            x_3 = x+1 
            y_3 = y-1
            new_index = y_3 * 8 + x_3
            while 0 <= x_3 < 8 and 0 <= y_3 < 8 and (board[new_index] is None or board[new_index].color != playing_color):
                legal_moves.append(new_index)
                if not is_response:
                    v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                    if is_check(playing_color=playing_color, board=v_board):
                        legal_moves.pop()
                if board[new_index] is not None and board[new_index].color != playing_color:
                    break
                x_3 += 1
                y_3 -= 1  
                new_index = y_3 * 8 + x_3


            x_4 = x-1 
            y_4 = y+1
            new_index = y_4 * 8 + x_4
            while 0 <= x_4 < 8 and 0 <= y_4 < 8 and (board[new_index] is None or board[new_index].color != playing_color):
                legal_moves.append(new_index)
                if not is_response:
                    v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                    if is_check(playing_color=playing_color, board=v_board):
                        legal_moves.pop()
                if board[new_index] is not None and board[new_index].color != playing_color:
                    break
                x_4 -= 1
                y_4 += 1
                new_index = y_4 * 8 + x_4


        if self.piece_type == "Rook":
            x_1 = x 
            y_1 = y+1
            new_index = y_1 * 8 + x_1
            while 0 <= x_1 < 8 and 0 <= y_1 < 8 and (board[new_index] is None or board[new_index].color != playing_color):
                legal_moves.append(new_index)
                if not is_response:
                    v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                    if is_check(playing_color=playing_color, board=v_board):
                        legal_moves.pop()
                if board[new_index] is not None and board[new_index].color != playing_color:
                    break
                y_1 += 1
                new_index = y_1 * 8 + x_1

            x_2 = x 
            y_2 = y-1
            new_index = y_2 * 8 + x_2
            while 0 <= x_2 < 8 and 0 <= y_2 < 8 and (board[new_index] is None or board[new_index].color != playing_color):
                legal_moves.append(new_index)
                if not is_response:
                    v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                    if is_check(playing_color=playing_color, board=v_board):
                        legal_moves.pop()
                if board[new_index] is not None and board[new_index].color != playing_color:
                    break
                y_2 -= 1
                new_index = y_2 * 8 + x_2

            x_3 = x+1 
            y_3 = y
            new_index = y_3 * 8 + x_3
            while 0 <= x_3 < 8 and 0 <= y_3 < 8 and (board[new_index] is None or board[new_index].color != playing_color):
                legal_moves.append(new_index)
                if not is_response:
                    v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                    if is_check(playing_color=playing_color, board=v_board):
                        legal_moves.pop()
                if board[new_index] is not None and board[new_index].color != playing_color:
                    break
                x_3 += 1
                new_index = y_3 * 8 + x_3


            x_4 = x-1 
            y_4 = y
            new_index = y_4 * 8 + x_4
            while 0 <= x_4 < 8 and 0 <= y_4 < 8 and (board[new_index] is None or board[new_index].color != playing_color):
                legal_moves.append(new_index)
                if not is_response:
                    v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                    if is_check(playing_color=playing_color, board=v_board):
                        legal_moves.pop()
                if board[new_index] is not None and board[new_index].color != playing_color:
                    break
                x_4 -= 1
                new_index = y_4 * 8 + x_4


        if self.piece_type == "Queen":
            x_1 = x 
            y_1 = y+1
            new_index = y_1 * 8 + x_1
            while 0 <= x_1 < 8 and 0 <= y_1 < 8 and (board[new_index] is None or board[new_index].color != playing_color):
                legal_moves.append(new_index)
                if not is_response:
                    v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                    if is_check(playing_color=playing_color, board=v_board):
                        legal_moves.pop()
                if board[new_index] is not None and board[new_index].color != playing_color:
                    break
                y_1 += 1
                new_index = y_1 * 8 + x_1

            x_2 = x 
            y_2 = y-1
            new_index = y_2 * 8 + x_2
            while 0 <= x_2 < 8 and 0 <= y_2 < 8 and (board[new_index] is None or board[new_index].color != playing_color):
                legal_moves.append(new_index)
                if not is_response:
                    v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                    if is_check(playing_color=playing_color, board=v_board):
                        legal_moves.pop()
                if board[new_index] is not None and board[new_index].color != playing_color:
                    break
                y_2 -= 1
                new_index = y_2 * 8 + x_2

            x_3 = x+1 
            y_3 = y
            new_index = y_3 * 8 + x_3
            while 0 <= x_3 < 8 and 0 <= y_3 < 8 and (board[new_index] is None or board[new_index].color != playing_color):
                legal_moves.append(new_index)
                if not is_response:
                    v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                    if is_check(playing_color=playing_color, board=v_board):
                        legal_moves.pop()
                if board[new_index] is not None and board[new_index].color != playing_color:
                    break
                x_3 += 1
                new_index = y_3 * 8 + x_3

            x_4 = x-1 
            y_4 = y
            new_index = y_4 * 8 + x_4
            while 0 <= x_4 < 8 and 0 <= y_4 < 8 and (board[new_index] is None or board[new_index].color != playing_color):
                legal_moves.append(new_index)
                if not is_response:
                    v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                    if is_check(playing_color=playing_color, board=v_board):
                        legal_moves.pop()
                if board[new_index] is not None and board[new_index].color != playing_color:
                    break
                x_4 -= 1
                new_index = y_4 * 8 + x_4

            x_5 = x+1 
            y_5 = y+1
            new_index = y_5 * 8 + x_5
            while 0 <= x_5 < 8 and 0 <= y_5 < 8 and (board[new_index] is None or board[new_index].color != playing_color):
                legal_moves.append(new_index)
                if not is_response:
                    v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                    if is_check(playing_color=playing_color, board=v_board):
                        legal_moves.pop()
                if board[new_index] is not None and board[new_index].color != playing_color:
                    break
                x_5 += 1
                y_5 += 1 
                new_index = y_5 * 8 + x_5

            x_6 = x-1 
            y_6 = y-1
            new_index = y_6 * 8 + x_6
            while 0 <= x_6 < 8 and 0 <= y_6 < 8 and (board[new_index] is None or board[new_index].color != playing_color):
                legal_moves.append(new_index)
                if not is_response:
                    v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                    if is_check(playing_color=playing_color, board=v_board):
                        legal_moves.pop()
                if board[new_index] is not None and board[new_index].color != playing_color:
                    break
                x_6 -= 1
                y_6 -= 1     
                new_index = y_6 * 8 + x_6 

            x_7 = x+1 
            y_7 = y-1
            new_index = y_7 * 8 + x_7
            while 0 <= x_7 < 8 and 0 <= y_7 < 8 and (board[new_index] is None or board[new_index].color != playing_color):
                legal_moves.append(new_index)
                if not is_response:
                    v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                    if is_check(playing_color=playing_color, board=v_board):
                        legal_moves.pop()
                if board[new_index] is not None and board[new_index].color != playing_color:
                    break
                x_7 += 1
                y_7 -= 1  
                new_index = y_7 * 8 + x_7

            x_8 = x-1 
            y_8 = y+1
            new_index = y_8 * 8 + x_8
            while 0 <= x_8 < 8 and 0 <= y_8 < 8 and (board[new_index] is None or board[new_index].color != playing_color):
                legal_moves.append(new_index)
                if not is_response:
                    v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                    if is_check(playing_color=playing_color, board=v_board):
                        legal_moves.pop()
                if board[new_index] is not None and board[new_index].color != playing_color:
                    break
                x_8 -= 1
                y_8 += 1 
                new_index = y_8 * 8 + x_8


        if self.piece_type == "King":
            x_1 = x 
            y_1 = y+1
            new_index = y_1 * 8 + x_1
            if 0 <= new_index < 64 and (board[new_index] is None or board[new_index].color != playing_color):
                legal_moves.append(new_index)
                # if not is_response:
                #     v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                #     if is_check(playing_color=playing_color, board=v_board):
                #         legal_moves.pop()


            x_2 = x 
            y_2 = y-1
            new_index = y_2 * 8 + x_2
            if 0 <= new_index < 64 and (board[new_index] is None or board[new_index].color != playing_color):
                legal_moves.append(new_index)
                # if not is_response:
                #     v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                #     if is_check(playing_color=playing_color, board=v_board):
                #         legal_moves.pop()

            x_3 = x+1 
            y_3 = y
            new_index = y_3 * 8 + x_3
            if 0 <= new_index < 64 and (board[new_index] is None or board[new_index].color != playing_color):
                legal_moves.append(new_index)
                # if not is_response:
                #     v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                #     if is_check(playing_color=playing_color, board=v_board):
                #         legal_moves.pop()

            x_4 = x-1 
            y_4 = y
            new_index = y_4 * 8 + x_4
            if 0 <= new_index < 64 and (board[new_index] is None or board[new_index].color != playing_color):
                legal_moves.append(new_index)
                # if not is_response:
                #     v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                #     if is_check(playing_color=playing_color, board=v_board):
                #         legal_moves.pop()

            x_5 = x+1 
            y_5 = y+1
            new_index = y_5 * 8 + x_5
            if 0 <= new_index < 64 and (board[new_index] is None or board[new_index].color != playing_color):
                legal_moves.append(new_index)
                # if not is_response:
                #     v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                #     if is_check(playing_color=playing_color, board=v_board):
                #         legal_moves.pop()

            x_6 = x-1 
            y_6 = y-1
            new_index = y_6 * 8 + x_6
            if 0 <= new_index < 64 and (board[new_index] is None or board[new_index].color != playing_color):
                legal_moves.append(new_index)
                # if not is_response:
                #     v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                #     if is_check(playing_color=playing_color, board=v_board):
                #         legal_moves.pop()

            x_7 = x+1 
            y_7 = y-1
            new_index = y_7 * 8 + x_7
            if 0 <= new_index < 64 and (board[new_index] is None or board[new_index].color != playing_color):
                legal_moves.append(new_index)
                # if not is_response:
                #     v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                #     if is_check(playing_color=playing_color, board=v_board):
                #         legal_moves.pop()

            x_8 = x-1 
            y_8 = y+1
            new_index = y_8 * 8 + x_8
            if 0 <= new_index < 64 and (board[new_index] is None or board[new_index].color != playing_color):
                legal_moves.append(new_index)
                # if not is_response:
                #     v_board = move_on_virtual_board(board.copy(), self.current_index, new_index)
                #     if is_check(playing_color=playing_color, board=v_board):
                #         legal_moves.pop()

            # if playing_color == "black" and self.piece_type == "King":
            #     print("legal moves", legal_moves)

            # if playing_color == "black":
            #     print(legal_moves)
            
            # if self.current_index == KINGS[playing_color]["position"]:
            #     is_free = True
            #     for i in KINGS[playing_color]["conditions"]:
            #         if board[i] is not None:
            #             is_free = False

            #     if is_free:
            #         if board[KINGS[playing_color]["rook"]].piece_type == "Rook":
            #             legal_moves.append(KINGS[playing_color]["result"])
                        


            
                
        return legal_moves
    

        