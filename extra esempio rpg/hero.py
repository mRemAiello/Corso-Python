import player as pl
import stats as st

"""Vigor 14 	Dexterity 9
Mind 9 	Intelligence 7
Endurance 12 	Faith 8
Strength 16 	Arcane 11"""


class Hero(pl.Player):

    def __init__(self, name):
        super().__init__(name)
        self.level = 7
        self.vigor = st.Stat(14)
        self.dexterity = st.Stat(9)
        self.mind = st.Stat(9)
        self.intelligence = st.Stat(7)
        self.endurance = st.Stat(12)
        self.strength = st.Stat(8)
        self.faith = st.Stat(8)
        self.arcane = st.Stat(11)
        self.calcolate_secondary_stats()
        self.calculate_vitals()
