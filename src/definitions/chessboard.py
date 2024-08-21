# FEN Notation

# Black is lowecase, white is UPPER

start_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
fen = start_fen


class board_definition:
    def __init__(self,fen): ## this breaks up the fen into a commaed list so i can read each element indpendently
        #parse the fen string first
        fen_fields = fen.split()
        self.piece_location = fen_fields[0]
        self.active_color = fen_fields[1] # going to have to write a function to modify each section of the fen message based on player actions
        self.castling = fen_fields[2]
        self.enpassant = fen_fields[3]
        self.halfmove_clock = int(fen_fields[4])
        self.move_number = int(fen_fields[5])
        self.board = self.parseboard(self.piece_location)
 
    def parseboard(self, piece_location): ## this parses the data from position 1 i the fen array to then represent the board as an array
        board = []
        # define the fen notation parts and how to parse the message
        for rank in piece_location.split('/'):
            row = []
            for char in rank:
                if char.isdigit():
                    row.extend(['.'] * int(char))
                else:
                    row.append(char)
            board.append(row)
        return board    
    
    def print_active_turn(self):
        print(f"Current turn is {self.active_color}")
        return self.active_color
    
    def print_board(self): # this prints the board
        ## Print the board function 
        for row in self.board:
            print(' '.join(row))

 
class possible_moves:
    def __init__(self, board, active_color, castling, enpassant, halfmove_clock):
        self.board = board
        self.active_color = active_color
        self.castling = castling
        self.enpassant = enpassant
        self.halfmoveclock = halfmove_clock

    def bounds_check(self, rank, file):
        return 0 <= rank < 8 and 0 <= file < 8
    
    def moves(self, position):
        rank, file = position 
        moves = []

        piece = self.board[rank][file]
        if piece.lower() == 'p':
            print("Move is invalid")            

        



    

current_board = board_definition(fen)
current_board.print_board()
current_board.print_active_turn()
