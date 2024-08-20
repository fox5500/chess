# FEN Notation

# Black is lowecase, white is UPPER

start_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
fen = start_fen


#Fields of the Notation
fen_fields = fen.split()
piece_location = fen_fields[0]
active_color = fen_fields[1]
castling = fen_fields[2]
enpassant = fen_fields[3]
halfmove_clock = fen_fields[4]
move_number = fen_fields[5]
board = []
#def generate_fen





## Print the board function
for rank in piece_location.split('/'):
    row = []
    for char in rank:
        if char.isdigit():
            row.extend(['.'] * int(char))
        else:
            row.append(char)
    board.append(row)
for row in board:
    print(' '.join(row))
 
    
