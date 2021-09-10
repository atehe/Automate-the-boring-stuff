

chessPieces = []
Pieces= ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
players = ['w', 'b']
for piece in Pieces:
    for player in players:
        chessPieces.append(player+piece)
print(chessPieces)

validBoard=[]
for row in range(1,9):
    for col in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        validBoard.append(str(row)+col)
print(validBoard)

def isValidChessBoard(chessBoard):
    for chessPlay in chessBoard.keys():
        if chessPlay not in validBoard:
            return False
    for chessPiece in chessPieces.values():
        if chessPiece not in chessPieces:
            return False
        
    
    
