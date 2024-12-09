class ElementSiraev:
    def __init__(self, name='Кальций', symbol='Ca', number='20'):
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
    element = ElementSiraev()
    element.dump()