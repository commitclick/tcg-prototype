class Card:
    def __init__(
            self, name: str, 
            description: str, 
            species: list, 
            cost: int, 
            cost_type: int, # blood or mana 
            attack: int, 
            defence: int, 
            element: str, 
            effect: str
            ):
        self._name = name
        self._description = description
        self._card_type = card_type
        self._mana_cost = mana_cost

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def card_type(self):
        return self._type

    @card_type.setter
    def type(self, value):
        self._card_type = value

    @property
    def mana_cost(self):
        return self._mana_cost

    @mana_cost.setter
    def mana_cost(self, value):
        self._mana_cost = value
