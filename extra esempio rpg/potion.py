import item as it


class Potion(it.Item):

    healing = 0

    def __init__(self, nome, healing):
        super().__init__(nome)
        self.healing = healing

    def use(self, player):
        player.heal(self.healing)

    def __str__(self):
        return super().__str__()