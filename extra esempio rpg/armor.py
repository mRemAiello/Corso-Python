import item as it


class Armor(it.Item):

    physicalDefence = 0
    magicDefence = 0

    def __init__(self, nome):
        super().__init__(nome)

    def __str__(self):
        stringa = super().__str__()
        stringa += ", Physical Defence: {}, Magic Defence: {}"
        return stringa.format(self.physicalDefence, self.magicDefence)