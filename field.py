class Field:
    def __init__(self, name: str, effect: str, description: str):
        self._name = name
        self._effect = effect
        self._description = description

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def effect(self) -> str:
        return self._effect

    @effect.setter
    def effect(self, value: str):
        self._effect = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = value