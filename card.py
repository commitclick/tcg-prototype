class Card:
    def __init__(self, name: str, description: str, card_type: list, mana_cost: int):
        self._name = name
        self._description = description
        self._card_type = type
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
