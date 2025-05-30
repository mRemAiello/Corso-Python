import stats as st
import weapon as wp
import armor as am


class Player:

    level = 0
    name = ""

    # Primarie
    vigor = 0
    mind = 0
    endurance = 0
    strength = 0
    dexterity = 0
    intelligence = 0
    faith = 0
    arcane = 0

    # Secondarie
    currentHp = 0
    maxHp = 0
    currentStamina = 0
    maxStamina = 0
    currentMp = 0
    maxMp = 0

    # Terziarie
    physicalAttack = 0
    magicAttack = 0
    physicalDefence = 0
    magicDefence = 0

    #
    right_weapon_1 = wp.Weapon("")
    armor = am.Armor("")

    consumabili = {}

    def __init__(self, name):
        self.name = name
        self.level = 0
        self.vigor = st.Stat(0)
        self.mind = st.Stat(0)
        self.endurance = st.Stat(0)
        self.strength = st.Stat(0)
        self.dexterity = st.Stat(0)
        self.intelligence = st.Stat(0)
        self.faith = st.Stat(0)
        self.arcane = st.Stat(0)

    def calcolate_secondary_stats(self):
        self.calculate_starting_hp()
        self.calculate_starting_stamina()
        self.calculate_starting_mp()
        self.calculate_attack()
        self.calculate_defence()

    def calculate_vitals(self):
        self.currentHp = self.maxHp
        self.currentStamina = self.maxStamina
        self.currentMp = self.maxMp

    def calculate_starting_hp(self):
        # Si può migliorare inserendo il 300 in una classe a parte,
        # e il calcolo della statistica in una sottoclasse di Stat
        self.maxHp = 300 + (self.vigor.value * 10)

    def calculate_starting_stamina(self):
        self.maxStamina = 100 + (self.endurance.value * 5)

    def calculate_starting_mp(self):
        self.maxMp = 50 + (self.mind.value * 3)

    # E' possibile migliorarlo facendo in modo che tu possa equipaggiare più armi / armature
    def equip(self, weapon):
        self.right_weapon_1 = weapon
        self.calcolate_secondary_stats()

    def equip_armor(self, armor):
        self.armor = armor
        self.calcolate_secondary_stats()

    def use_item(self, position):
        if str(position) in self.consumabili:
            self.consumabili[str(position)].use(self)

    def heal(self, healing):
        self.currentHp += healing
        if self.currentHp > self.maxHp:
            self.currentHp = self.maxHp

    def calculate_attack(self):
        self.physicalAttack = (2 * self.strength.value) + self.right_weapon_1.physicalAttack
        self.magicAttack = (2 * self.mind.value) + self.right_weapon_1.magicAttack

    def calculate_defence(self):
        self.physicalDefence = self.strength.value + self.armor.physicalDefence
        self.magicDefence = self.mind.value + self.armor.magicDefence

    def __str__(self):
        stringa = "Name: {}\n"
        stringa += "Level: {}\n"
        stringa += "Vigor: {}, Mind: {}, Endurance: {}, Strength: {}, Dexterity: {}, "
        stringa += "Intelligence: {}, Faith: {}, Arcane: {}\n"
        stringa += "Current HP: {}, Max HP: {}\n"
        stringa += "Current Stamina: {}, Max Stamina: {}\n"
        stringa += "Current MP: {}, Max MP: {}\n"
        stringa += "Physical: {}, Magic: {}\n"
        stringa += "Physical Def: {}, Magic Def: {}"

        return stringa.format(self.name, self.level, self.vigor, self.mind, self.endurance, self.strength,
                              self.dexterity, self.intelligence, self.faith, self.arcane, self.currentHp, self.maxHp,
                              self.currentStamina, self.maxStamina, self.currentMp, self.maxMp, self.physicalAttack,
                              self.magicAttack, self.physicalDefence, self.magicDefence)




