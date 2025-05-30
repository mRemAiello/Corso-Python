class Item:

    name = ""

    def __init__(self, name):
        self.name = name

    def use(self, player):
        print()

    def __str__(self):
        return "Nome: " + self.name