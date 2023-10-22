import board
b = board.Board(8)
def placeMoves():
    for move in b.getPossibleMoves():
        b.makeMove(move)
        if len(b.queenSpaces) == b.n:
            return True
        else:
            retVal = placeMoves()
            if retVal:
                return True
            else:
                b.removeMove(move)
    return False
if __name__ == "__main__":
    placeMoves()
    b.print()
