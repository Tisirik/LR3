class ElementKhasyanova:
    def init(self, name='Хром', symbol='Cr', number='24'):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(f"Имя элемента: {self.name}")
        print(f"Символ: {self.symbol}")
        print(f"Атомный номер: {self.number}")

if name == "main":
    element = ElementKhasyanova()
    element.dump()