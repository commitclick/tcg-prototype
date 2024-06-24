class Board:
    def __init__(self,
            fields: list,
            p1_Spells: list,
            p1_Monsters: list,
            p2_Spells: list,
            p2_Monsters: list
            ):
        self.fields = fields
        self.p1_Spells: list = p1_Spells
        self.p1_Monsters: list = p1_Monsters
        self.p2_Spells: list = p2_Spells
        self.p2_Monsters: list = p2_Monsters
    
    def showBoard(self):
        print(self.p1_Spells)
        print(self.p1_Monsters)
        print(self.fields)
        print(self.p1_Monsters)
        print(self.p1_Spells)

board = Board()

board.showBoard()