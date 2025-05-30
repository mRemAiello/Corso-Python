import hero as hr
import bandit as bd
import weapon as wp
import armor as am
import potion as pt


#
classe = int(input("Scegli una classe (0 Hero, 1 Bandit): "))
nome = input("Dai un nome al personaggio: ")
player = hr.Hero("")
if classe == 0:
    player = hr.Hero(nome)
elif classe == 1:
    player = bd.Bandit(nome)
else:
    print("Non hai inserito una classe valida")


#
weapon1 = wp.Weapon("Fire Knight's Shortsword")
weapon1.physicalAttack = 126
weapon1.magicAttack = 126


#
armor1 = am.Armor("Armatura")
armor1.physicalDefence = 100
armor1.magicDefence = 80


#
potion1 = pt.Potion("Healing Potion", 20)



#
player.currentHp -= 40
print(player)
print()


#
player.equip(weapon1)
player.equip_armor(armor1)
player.consumabili["1"] = potion1
player.use_item("1")


#
print(player)