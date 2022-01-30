def isValidChessBoard(chess_board):

    Pieces = ["pawn", "knight", "bishop", "rook", "queen", "king"]
    players = ["w", "b"]

    chess_pieces = []
    for piece in Pieces:
        for player in players:
            chess_pieces.append(player + piece)

    valid_board = []
    for row in range(1, 9):
        for col in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            valid_board.append(str(row) + col)

    for chess_play in chess_board.keys():
        if chess_play not in valid_board:
            return False
    for chess_piece in chess_board.values():
        if chess_piece not in chess_pieces:
            return False
    return True


print(
    isValidChessBoard(
        {"1h": "bking", "6c": "wqueen", "2g": "bbishop", "5h": "bqueen", "3e": "wking"}
    )
)
