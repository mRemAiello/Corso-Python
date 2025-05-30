import item as it


class Weapon(it.Item):

    physicalAttack = 0
    magicAttack = 0

    def __init__(self, nome):
        super().__init__(nome)

    def __str__(self):
        stringa = super().__str__()
        stringa += ", Physical: {}, Magic: {}"
        return stringa.format(self.physicalAttack, self.magicAttack)