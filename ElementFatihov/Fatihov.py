class ElementFatihov:
    def __init__(self, name='Титан', symbol='Ti', number='22'):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    @property
    def name(self):
        return self.__name
    @property
    def symbol(self):
        return self.__symbol
    @property
    def number(self):
        return self.__number
    def dump(self):
        print(f"Имя элемента: {self.name}")
        print(f"Символ: {self.symbol}")
        print(f"Атомный номер: {self.number}")
if __name__ == "__main__":
    element = ElementFatihov()
    element.dump()