import player as pl
import stats as st

"""Level 5
Vigor 10 	Dexterity 13
Mind 11 	Intelligence 9
Endurance 10 	Faith 8
Strength 9 	Arcane 14"""


class Bandit(pl.Player):

    def __init__(self, name):
        super().__init__(name)
        self.level = 5
        self.vigor = st.Stat(10)
        self.dexterity = st.Stat(13)
        self.mind = st.Stat(11)
        self.intelligence = st.Stat(9)
        self.endurance = st.Stat(10)
        self.strength = st.Stat(9)
        self.faith = st.Stat(8)
        self.arcane = st.Stat(14)
        self.calcolate_secondary_stats()
        self.calculate_vitals()