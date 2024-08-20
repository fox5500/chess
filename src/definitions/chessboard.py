# FEN Notation

# Black is lowecase, white is UPPER

start_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
fen = start_fen


class gamestate:
    def __init__(self,fen):
        #parse the fen string first
        fen_fields = fen.split()
        self.piece_location = fen_fields[0]
        self.active_color = fen_fields[1] # going to have to write a function to modify each section of the fen message based on player actions
        self.castling = fen_fields[2]
        self.enpassant = fen_fields[3]
        self.halfmove_clock = fen_fields[4]
        self.move_number = fen_fields[5]
        self.board = self.parseboard(self.piece_location)

    def parseboard(self, piece_location):
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

    def print_board(self):
        ## Print the board function
        for row in self.board:
            print(' '.join(row))
    

game = gamestate(fen)
game.print_board()
