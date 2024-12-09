class ElementFatihov:
    def __init__(self, name='Титан', symbol='Ti', number='22'):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(f"Имя элемента: {self.name}")
        print(f"Символ: {self.symbol}")
        print(f"Атомный номер: {self.number}")

if __name__ == "__main__":
    element = ElementFatihov()
    element.dump()