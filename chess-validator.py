def main():

    # A dict representation of a chessboard. Columns are dict keys, and a nested dict represents rows. That dicts keys are rows, and their values are pieces.
    chessboard = {
        "a": {
            1: "w_rook1",
            2: "w_knight1",
            3: "w_bishop1",
            4: "w_queen",
            5: "w_king",
            6: "w_bishop2",
            7: "w_knight2",
            8: "w_rook2",
        },
        "b": {
            1: "w_pawn1",
            2: "w_pawn2",
            3: "w_pawn3",
            4: "w_pawn4",
            5: "w_pawn5",
            6: "w_pawn6",
            7: "w_pawn7",
            8: "w_pawn8",
        },
        "c": {},
        "d": {},
        "e": {},
        "f": {},
        "g": {
            1: "b_pawn1",
            2: "b_pawn2",
            3: "b_pawn3",
            4: "b_pawn4",
            5: "b_pawn5",
            6: "b_pawn6",
            7: "b_pawn7",
            8: "b_pawn8",
        },
        "h": {
            1: "b_rook1",
            2: "b_knight1",
            3: "b_bishop1",
            4: "b_king",
            5: "b_queen",
            6: "b_bishop2",
            7: "b_knight2",
            8: "b_rook2",
        },
    }

    print(isValidChessboard(chessboard))


def isValidChessboard(board: dict) -> bool:
    """Check if a chessboard is valid."""

    white_pieces = 0
    black_pieces = 0
    w_king_found = 0
    b_king_found = 0

    for cols, rows in board.items():
        # Check if columns are not between a-h.
        if 97 > ord(cols) or ord(cols) > 104:
            return False

        """Why does this interval comparison not work?
        if 97 > ord(cols) > 104:
            return False#"""

        for chess_row, piece in rows.items():

            # Check if rows are not between 1-8.
            if 1 > chess_row or chess_row > 8:
                return False

            """Why does this interval comparison not work?
            if 1 > chess_row > 8:
                return False#"""

            # Check if a piece is black or white. And if it's a king. Increment check-variables above.
            if "b_" in piece:
                black_pieces += 1
                if "king" in piece:
                    b_king_found += 1
            elif "w_" in piece:
                white_pieces += 1
                if "king" in piece:
                    w_king_found += 1
            else:
                # A piece is not white or black? Something's fishy...
                return False

    # Return True if all checks are satisfied.
    if (
        white_pieces <= 16
        and black_pieces <= 16
        and w_king_found == 1
        and b_king_found == 1
    ):
        return True

    return False


if __name__ == "__main__":
    main()
