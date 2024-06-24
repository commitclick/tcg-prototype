class Field:
    def __init__(self, name: str, element: str, effect: str):
        self._name = name
        self._element = element
        self._effect = effect

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def element(self) -> str:
        return self._element

    @element.setter
    def element(self, value: str):
        self._element = value

    @property
    def effect(self) -> str:
        return self._effect

    @effect.setter
    def effect(self, value: str):
        self._effect = value
