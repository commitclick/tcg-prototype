class Match:
    def __init__(self, 
                board, 
                player1, 
                player2,
                turn: int,
                phase: list
                ):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.turn = 0
        self.phase = []