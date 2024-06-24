class Deck:
    def __init__(self, name: str, creator: str):
        self._name = name
        self._creator = creator
        self._cards = []