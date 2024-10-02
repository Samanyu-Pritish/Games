class ChessPiece:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def __str__(self):
        return f"{self.color[0].upper()}{self.name[0].upper()}"


class ChessBoard:
    def __init__(self):
        self.board = self.create_board()
        self.current_turn = "white"

    def create_board(self):
        board = [[None] * 8 for _ in range(8)]
        # Place pieces on the board
        for i in range(8):
            board[1][i] = ChessPiece("black", "pawn")
            board[6][i] = ChessPiece("white", "pawn")
        
        pieces = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]
        for i, piece in enumerate(pieces):
            board[0][i] = ChessPiece("black", piece)
            board[7][i] = ChessPiece("white", piece)
        
        return board

    def display(self):
        for row in self.board:
            print(" | ".join(str(piece) if piece else "  " for piece in row))
            print("-" * 32)

    def move_piece(self, start, end):
        start_row, start_col = start
        end_row, end_col = end

        piece = self.board[start_row][start_col]
        if piece and piece.color == self.current_turn:
            self.board[end_row][end_col] = piece
            self.board[start_row][start_col] = None
            self.current_turn = "black" if self.current_turn == "white" else "white"
        else:
            print("Invalid move.")

    def parse_position(self, pos):
        col = ord(pos[0]) - ord('a')
        row = 8 - int(pos[1])
        return row, col


def main():
    board = ChessBoard()
    board.display()

    while True:
        move = input(f"{board.current_turn.capitalize()}'s turn. Enter your move (e.g., e2 e4): ")
        if move.lower() == "quit":
            break
        try:
            start_pos, end_pos = move.split()
            start = board.parse_position(start_pos)
            end = board.parse_position(end_pos)
            board.move_piece(start, end)
            board.display()
        except (ValueError, IndexError):
            print("Invalid input. Please use the format 'e2 e4'.")


if __name__ == "__main__":
    main()
