import random
import traceback
import tkinter
#

top = tkinter.Tk()
class die_roller():

    def __init__(self, number, sides):

        self.number = number
        self.sides = sides
        self.roll()

    def roll(self):

        self.rand = random.randint(self.number, self.sides)
        return self.rand


#dice roller 1
d100 = die_roller(1,101)
d20 = die_roller(1, 21)
d12 = die_roller(1, 13)
d10 = die_roller(1, 11)
d8 = die_roller(1, 9)
d6 = die_roller(1, 7)
d4 = die_roller(1, 4)

d12min6 = die_roller(6, 13)
d10min5 = die_roller(5, 11)
d10min4 = die_roller(4, 11)
d8min4 = die_roller(4, 9)
d8min3 = die_roller(3, 9)
d6min2 = die_roller(3, 9)

attr = {

    "strg": 0,
    "dex": 0,
    "con": 0,
    "wis": 0,
    "intl": 0,
    "cha": 0

    }



print("What are you?")
race = input("|B| |T| |C| |L| |I| |X|\n")
print("What is your name?: ")
name = input()
print("ok", name,"would you like to roll or have me do it?\n")


class Race_bns():

    def __init__(self, attr_bns1, attr_bns2):

        self.attr_bns1 = attr_bns1
        self.attr_bns2 = attr_bns2

        if race == "X":

            self.attr_bns3 = 2
            self.attr_bns4 = 1

        elif race == "C":

            self.attr_bns3 = +1

        else:

            ('')


bulletor_bns = Race_bns(+2, -2)
tyjearus_bns = Race_bns(+2, +2)
climberdom_bns = Race_bns(+1, +2)
lienus_bns = Race_bns(2, 2)
indu_bns = Race_bns(2, 2)
xcelerite_bns = Race_bns(+1, -2)

dec = ''



while dec != "y" and dec != "m":

    dec = input("m/y: ")

    if dec == "y":

        attr["strg"] = d20.roll()
        attr["con"] = d20.roll()
        attr["dex"] = d20.roll()
        attr["wis"] = d20.roll()
        attr["intl"] = d20.roll()
        attr["cha"] = d20.roll()

    elif dec == "m":

        attr["strg"] = int(input("STR: "))
        attr["con"] = int(input("DEX: "))
        attr["dex"] = int(input("CON: "))
        attr["wis"] = int(input("WIS: "))
        attr["intl"] = int(input("INT: "))
        attr["cha"] = int(input("CHA: "))

    else:

        print("what?")

abilites = {

    "Sight": {},
    "Trans": {},
    "Special": {}

    }

if race == "B":

    attr["strg"] = attr["strg"] + bulletor_bns.attr_bns1
    attr["cha"] = attr["cha"] + bulletor_bns.attr_bns2

elif race == "T":

    attr["intl"] = attr["intl"] + tyjearus_bns.attr_bns1
    attr["dex"] = attr["dex"] + tyjearus_bns.attr_bns2

elif race == "C":

    attr["dex"] = attr["dex"] + climberdom_bns.attr_bns1
    attr["cha"] = attr["cha"] + climberdom_bns.attr_bns2
    attr["wis"] = attr["wis"] + climberdom_bns.attr_bns3

elif race == "L":

    attr["wis"] = attr["wis"] + lienus_bns.attr_bns1
    attr["con"] = attr["con"] + lienus_bns.attr_bns2

elif race == "I":

    attr["intl"] = attr["intl"] + indu_bns.attr_bns1
    attr["con"] = attr["con"] + indu_bns.attr_bns2

elif race == "X":

    attr["strg"] = attr["strg"] + xcelerite_bns.attr_bns1
    attr["con"] = attr["con"] + xcelerite_bns.attr_bns2
    attr["dex"] = attr["dex"] + xcelerite_bns.attr_bns3
    attr["wis"] = attr["wis"] + xcelerite_bns.attr_bns4

else:

    print ("what?")
    race = input()

print (attr)


class moder():

    def __init__(self, attrs):

        self.attrs = attrs

        self.mods = 0

        if self.attrs == 0:

            self.mods = -6

        elif self.attrs == 1:

            self.mods = -5

        elif self.attrs == 2 or self.attrs == 3:

            self.mods = -4

        elif self.attrs == 4 or self.attrs == 5:

            self.mods = -3

        elif self.attrs == 6 or self.attrs == 7:

            self.mods = -2

        elif self.attrs == 8 or self.attrs == 9:

            self.mods = -1

        elif self.attrs == 10 or self.attrs == 11:

            self.mods = 0

        elif self.attrs == 12 or self.attrs == 13:

            self.mods = 1

        elif self.attrs == 14 or self.attrs == 15:

            self.mods = 2

        elif self.attrs == 16 or self.attrs == 17:

            self.mods = 3

        elif self.attrs == 18 or self.attrs == 19:

            self.mods = 4

        elif self.attrs == 20:

            self.mods = 5

        elif self.attrs == 21 or self.attrs == 22 or self.attrs == 23 or self.attrs == 24:

            self.mods = 6

        else:

            print("error")

class tile_maker():

    def __init__(self, tile_mod):

        self.tile_mod = tile_mod

        self.tiles = 0

        if self.tile_mod == -5:

            self.tiles = 0

        elif self.tile_mod == -4 or self.tile_mod == -3:

            self.tiles = 1

        elif self.tile_mod == -2 or self.tile_mod == -1:

            self.tiles = 1

        elif self.tile_mod == 0:

            self.tiles = 1

        elif self.tile_mod == 1 or self.tile_mod == 2:

            self.tiles = 2

        elif self.tile_mod == 3 or self.tile_mod == 4:

            self.tiles = 3

        elif self.tile_mod == 5:

            self.tiles = 4

        elif self.tile_mod == 6:

            self.tiles = 5

        else:

            print('IMPOSSIBLE')

#converter
strg = attr.get("strg")
dex = attr.get("dex")
con = attr.get("con")
wis = attr.get("wis")
intl = attr.get("intl")
cha = attr.get("cha")

#moder
strg_temp = moder(strg)
dex_temp = moder(dex)
dex_temp2 = tile_maker(dex_temp.mods)
con_temp = moder(con)
wis_temp = moder(wis)
intl_temp = moder(intl)
cha_temp = moder(cha)

#mods
modis = {

    "strg_modi": strg_temp.mods,
    "dex_modi": dex_temp.mods,
    "con_modi": con_temp.mods,
    "wis_modi": wis_temp.mods,
    "intl_modi": intl_temp.mods,
    "cha_modi": cha_temp.mods

   }

hgt = float(0)
wgt = float(0)

class size_maker():

    def __init__(self, max_hgt, max_wgt):

        self.max_hgt = max_hgt
        self.max_wgt = max_wgt

        self.wgt = float(0)
        self.hgt = float(0)

        if race == 'C':

            if con <= 11:

                self.hgt = 2

            elif con == 12:

                self.hgt = 3

            elif con == 13:

                self.hgt = 4

            elif con == 14:

                self.hgt = 5

            elif con == 15:

                self.hgt = 6

            elif con == 16:

                self.hgt = 7

            elif con == 17:

                self.hgt = 8

            elif con == 18:

                self.hgt = 9

            elif con >= 19:

                self.hgt = 10

            else:

                print("wrong answer")

            if strg_temp.mods >= 4:

                self.wgt = self.max_wgt

            elif strg_temp.mods == 3:

                self.wgt = self.max_wgt - 150

            elif strg_temp.mods == 2:

                self.wgt = self.max_wgt - 250

            elif strg_temp.mods == 1:

                self.wgt = self.max_wgt - 400

            elif strg_temp.mods <= 0:

                self.wgt = self.max_wgt - 480

            else:

                print("afgadf")

        elif race != 'C':

            if con_temp.mods >= 4:

                self.hgt = self.max_hgt

            elif con_temp.mods == 3:

                self.hgt = self.max_hgt - 0.5

            elif con_temp.mods == 2:

                self.hgt = self.max_hgt - 1

            elif con_temp.mods == 1:

                self.hgt = self.max_hgt - 1.5

            elif con_temp.mods <= 0:

                self.hgt = self.max_hgt - 2

            else:

                print("also wrong answer")


            if race == 'L':

                if strg_temp.mods >= 4:

                    self.wgt = self.max_wgt

                elif strg_temp.mods == 3:

                    self.wgt = self.max_wgt - 100

                elif strg_temp.mods == 2:

                    self.wgt = self.max_wgt - 200

                elif strg_temp.mods == 1:

                    self.wgt = self.max_wgt - 300

                elif strg_temp.mods <= 0:

                    self.wgt = self.max_wgt - 400

                else:

                    print("eggg")


            elif race == 'T':

                if strg_temp.mods >= 4:

                    self.wgt = self.max_wgt

                elif strg_temp.mods == 3:

                    self.wgt = self.max_wgt - 50

                elif strg_temp.mods == 2:

                    self.wgt = self.max_wgt - 100

                elif strg_temp.mods == 1:

                    self.wgt = self.max_wgt - 125

                elif strg_temp.mods <= 0:

                    self.wgt = self.max_wgt - 150

                else:

                    print("but how?")

            elif race == "B" or race == "X" or race == "I":

                if strg_temp.mods >= 4:

                    self.wgt = self.max_wgt

                elif strg_temp.mods == 3:

                    self.wgt = self.max_wgt - 50

                elif strg_temp.mods == 2:

                    self.wgt = self.max_wgt - 100

                elif strg_temp.mods == 1:

                    self.wgt = self.max_wgt - 150

                elif strg_temp.mods <= 0:

                    self.wgt = self.max_wgt - 200

                else:

                    print("but how?")

            else:

                print("we don't know")

        else:

            print("interesting")

if race == 'C':

    climberdom_sz = size_maker(10, 500)
    hgt = climberdom_sz.hgt
    wgt = climberdom_sz.wgt

elif race == 'B':

    bulletor_sz = size_maker(6, 300)
    hgt = bulletor_sz.hgt
    wgt = bulletor_sz.wgt

elif race == 'T':

    tyjearus_sz = size_maker(7, 200)
    hgt = tyjearus_sz.hgt
    wgt = tyjearus_sz.wgt

elif race == 'L':

    lienus_sz = size_maker(7, 600)
    hgt = lienus_sz.hgt
    wgt = lienus_sz.wgt

elif race == 'X':

    xcelerite_sz = size_maker(6, 300)
    hgt = xcelerite_sz.hgt
    wgt = xcelerite_sz.wgt

elif race == 'I':

    indu_sz = size_maker(6, 450)
    hgt = indu_sz.hgt
    wgt = indu_sz.wgt
else:

    print("ehhh")

sz_class = hgt + wgt
min_dmg = 0
melee_dmg = ''
min_hlt = 0
nat_arm = 0

if sz_class <= 53.5:

    sz_class = "X-Small"
    min_hlt = 0
    nat_arm = 5
    min_dmg = 0
    melee_dmg = "1D4-1"

elif sz_class <= 104.5 and sz_class >= 54:

    sz_class = "Small"
    min_hlt = 0
    nat_arm = 10
    min_dmg = 1
    melee_dmg = "1D4"

elif sz_class <= 306.5 and sz_class >= 105:

    sz_class = "Medium"
    min_hlt = 10
    nat_arm = 15
    min_dmg = 2
    melee_dmg = "1D6"

elif sz_class <= 508.5 and sz_class >=307:

    sz_class = "Large"
    min_hlt = 15
    nat_arm = 20
    min_dmg = 3
    melee_dmg = "1D8"

elif sz_class <= 509:

    sz_class = "X-Large"
    min_hlt = 20
    nat_arm = 25
    min_dmg = 4
    melee_dmg = "1D10"

else:

    print("blah")


class hlt_maker(die_roller):

    def __init__(self, cons, szs):

        self.cons = cons
        self.szs = szs

    def con_roll(self):

        self.rollh = 0
        self.rollstop = 0


        if self.cons == -5:

            self.rollh = d4.roll()

        elif self.cons == -4:

            self.rollh = 4

        elif self.cons == -3:

            self.rollh = d6.roll()

        elif self.cons == -2:

            self.rollh = d6.roll()

        elif self.cons == -1:

            self.rollh = d6min2.roll()

        elif self.cons == 0:

            self.rollh = d6.roll() * 2

        elif self.cons == 1:

            self.rollh = d6min2.roll() * 2

        elif self.cons == 2:

            self.rollh = d8min3.roll() * 2

        elif self.cons == 3:

            self.rollh = d8min4.roll() * 2

        elif self.cons == 4:

            self.rollh = d10min4.roll() * 2

        elif self.cons == 5:

            self.rollh = d10min5.roll() * 2

        elif self.cons == 6:

            self.rollh = d12min6.roll() * 2

        else:

            print("ehhhh")

        return self.rollh

class wound_maker():

    def __init__(self, bdy_hlt):

        self.bdy_hlt = bdy_hlt
        self.main_wnd = 0
        self.sec_wnd = 0

        if self.bdy_hlt < 10:

            self.main_wnd = 0

        elif self.bdy_hlt >= 10 and self.bdy_hlt < 20:

            self.main_wnd = 2

        elif self.bdy_hlt >= 20 and self.bdy_hlt < 30:

            self.main_wnd = 4

        elif self.bdy_hlt >= 30 and self.bdy_hlt < 40:

            self.main_wnd = 6

        elif self.bdy_hlt >= 40 and self.bdy_hlt < 50:

            self.main_wnd = 8

        elif self.bdy_hlt >= 50 and self.bdy_hlt < 60:

            self.main_wnd = 10

        else:

            print("psht")

        if self.bdy_hlt < 10:

            self.sec_wnd = 0

        elif self.bdy_hlt >= 10 and self.bdy_hlt < 20:

            self.sec_wnd = 1

        elif self.bdy_hlt >= 20 and self.bdy_hlt < 30:

            self.sec_wnd = 2

        elif self.bdy_hlt >= 30 and self.bdy_hlt < 40:

            self.sec_wnd = 3

        elif self.bdy_hlt >= 40 and self.bdy_hlt < 50:

            self.sec_wnd = 4

        elif self.bdy_hlt >= 50 and self.bdy_hlt < 60:

            self.sec_wnd = 5

        else:

            print("psht2")


my_hlt = hlt_maker(con_temp.mods, sz_class)

#healths
hlt_nest = {

    "Main": {"Head": my_hlt.con_roll() + min_hlt, "Torso": my_hlt.con_roll() + min_hlt},
    "Legs": {"Left Legs":my_hlt.con_roll() + min_hlt, "Right Legs": 0},
    "Arms": {"Left Arms": my_hlt.con_roll() + min_hlt, "Right Arms": 0},
    "Misc": {},
    "Main Misc": {}

    }
#wounds
headw = wound_maker(hlt_nest["Main"]["Head"])
torsow = wound_maker(hlt_nest["Main"]["Torso"])
armsw = wound_maker(hlt_nest["Arms"]["Left Arms"])
legsw = wound_maker(hlt_nest["Legs"]["Left Legs"])
miscw = wound_maker(min_hlt)

wounds = {

    "Main": {"Head Wounds": headw.main_wnd, "Torso Wounds": torsow.main_wnd},
    "Legs": {"Left Legs Wounds": legsw.sec_wnd, "Right Legs Wounds": legsw.sec_wnd},
    "Arms": {"Left Arms Wounds": armsw.sec_wnd, "Right Arms Wounds": armsw.sec_wnd},
    "Misc": {},
    "Main Misc": {}

    }




hlt_nest["Legs"]["Right Legs"] = hlt_nest["Legs"]["Left Legs"]
hlt_nest["Arms"]["Right Arms"] = hlt_nest["Arms"]["Left Arms"]

if race == 'L':

    hlt_nest["Misc"]["Front Left Shovel"] = min_hlt
    wounds["Misc"]["Front Left Shovel Wounds"] = miscw.sec_wnd

    hlt_nest["Misc"]["Front Right Shovel"] = min_hlt
    wounds["Misc"]["Front Right Shovel Wounds"] = miscw.sec_wnd

    hlt_nest["Arms"]["Lower Left Arm"] = my_hlt.con_roll() + min_hlt
    lowarmsw = wound_maker(hlt_nest["Arms"]["Lower Left Arm"])
    wounds["Arms"]["Lower Left Arm Wounds"] = lowarmsw.sec_wnd

    hlt_nest["Arms"]["Lower Right Arm"] = hlt_nest["Arms"]["Lower Left Arm"]
    wounds["Arms"]["Lower Right Arm Wounds"] = lowarmsw.sec_wnd

    hlt_nest["Legs"]["Back Left Leg"] = my_hlt.con_roll() + min_hlt
    backlegsw = wound_maker(hlt_nest["Legs"]["Back Left Leg"])
    wounds["Legs"]["Back Left Leg Wounds"] = backlegsw.sec_wnd

    hlt_nest["Legs"]["Back Right Leg"] = hlt_nest["Legs"]["Back Left Leg"]
    wounds["Legs"]["Back Right Leg Wounds"] = backlegsw.sec_wnd

    hlt_nest["Misc"]["Back Right Shovel"] = min_hlt
    wounds["Misc"]["Back Right Shovel Wounds"] = miscw.sec_wnd

    hlt_nest["Misc"]["Bach Left Shovel"] = min_hlt
    wounds["Misc"]["Back Left Shovel Wounds"] = miscw.sec_wnd

    hlt_nest.pop("Main Misc")
    wounds.pop("Main Misc")

elif race == 'I':

    hlt_nest["Main Misc"]["Tail"] = my_hlt.con_roll() + min_hlt
    mnmiscw = wound_maker(hlt_nest["Main Misc"]["Tail"])
    wounds["Main Misc"]["Tail Wounds"] = mnmiscw.sec_wnd

    hlt_nest.pop("Misc")
    wounds.pop("Misc")
    hlt_nest.pop("Legs")

elif race == 'B':

    hlt_nest["Main Misc"]["Left Wing"] = my_hlt.con_roll() + min_hlt
    mnmiscw = wound_maker(hlt_nest["Main Misc"]["Left Wing"])
    wounds["Main Misc"]["Left Wing Wounds"] = mnmiscw.sec_wnd

    hlt_nest["Main Misc"]["Right Wing"] = hlt_nest["Main Misc"]["Left Wing"]
    wounds["Main Misc"]["Right Wing Wounds"] = mnmiscw.sec_wnd

    hlt_nest.pop("Misc")
    wounds.pop("Misc")

elif race == 'C':

    hlt_nest["Misc"]["Left Tail"] = min_hlt
    wounds["Misc"]["Left Tail Wounds"] = miscw.sec_wnd

    hlt_nest["Misc"]["Right Tail"] = min_hlt
    wounds["Misc"]["Right Tail Wounds"] = miscw.sec_wnd

    hlt_nest["Misc"]["Head Finger 1"] = min_hlt
    wounds["Misc"]["Head Finger 1 Wounds"] = miscw.sec_wnd

    hlt_nest["Misc"]["Head Finger 2"] = min_hlt
    wounds["Misc"]["Head Finger 2 Wounds"] = miscw.sec_wnd

    hlt_nest["Misc"]["Head Finger 3"] = min_hlt
    wounds["Misc"]["Head Finger 3 Wounds"] = miscw.sec_wnd

    hlt_nest["Misc"]["Head Finger 4"] = min_hlt
    wounds["Misc"]["Head Finger 4 Wounds"] = miscw.sec_wnd

    hlt_nest["Misc"]["Head Finger 5"] = min_hlt
    wounds["Misc"]["Head Finger 5 Wounds"] = miscw.sec_wnd

    hlt_nest["Misc"]["Head Finger 6"] = min_hlt
    wounds["Misc"]["Head Finger 6 Wounds"] = miscw.sec_wnd

    hlt_nest["Misc"]["Left Forearm"] = min_hlt
    wounds["Misc"]["Left Forearm Wounds"] = miscw.sec_wnd

    hlt_nest["Misc"]["Right Forearm"] = min_hlt
    wounds["Misc"]["Right Forearm Wounds"] = miscw.sec_wnd

    hlt_nest["Misc"]["Left Shin"] = min_hlt
    wounds["Misc"]["Left Shin Wounds"] = miscw.sec_wnd

    hlt_nest["Misc"]["Right Shin"] = min_hlt
    wounds["Misc"]["Right Shin Wounds"] = miscw.sec_wnd

    hlt_nest.pop("Main Misc")
    wounds.pop("Main Misc")

else:

    print("broken")




print(modis)

print("Height: ", hgt)
print("Weight: ", wgt)

tile = dex_temp2.tiles
print("Tiles: ", tile)

init = attr["strg"] + attr["dex"] + attr["wis"]
iq = attr["wis"] + attr["intl"]

ment_hlt = attr["con"] + attr["wis"] + attr["intl"]

print("IQ: ", iq)
print("Initiative", init)
print(sz_class)
print(min_dmg)
print(melee_dmg)
print(ment_hlt)

dec2 = input("m/y: ")

for x,y in hlt_nest.items():
  print(x,y,"\n")

for x,y in wounds.items():
  print(x,y,"\n")


print("Curses: \n")

curses = {

    "1. Lisp -": "-2 Battle Cry",
    "2. Near Sighted -": "-2 to Ranged Attacks",
    "3. Unaware -": "-2 to noticing Ambushes/Surprise attacks",
    "4. Asthma -": "Can only move 1/2 Tiles",
    "5. Not Ready -": "-15 Init",
    "6. Limp -": "-1 Tile",
    "7. Deaf -": "Can't use hearing organs",
    "8. Weak Immunity -": "-4 to rolling out of Toxic Status Effect",
    "9. Scar Tissue -": "Choose a spot to have weakend skin. Attacks there cause auto wounds",
    "10. Gullible -": "-3 on Barter rolls and +2 to traders using it against you",
    "11. Arachnophobia -": "Scared when seeing a Spider, Panic when engaged in combat",
    "12. Aviophobia -": "Fear when more than 15 feet off the ground",
    "13. Megalophobia -": "Anything 2 Size Classes bigger causes Panic",
    "14. Nanophobia -": "Anything 2 Size Classes smaller causes Panic",
    "15. Agateophobia -": "When Crazed, you go insane instead",
    "16. Bibliophobia -": "Can't read Books or Scrolls",
    "17. Catapedaphobia -": "Refuse to Jump",
    "18. Claustrophobia -": "Small Spaces and Burrowed cause Panic",
    "19. Epistemophobia -": "Can't gain Knowledge outside of Player Creation",
    "20. Ticklish -": "-4 Diff when being Tickled",
    "20. High Pitched -": "-3 to Intimidate",
    "21. Achilles Heel -": "Choose a spot to be a 1 hit kill",
    "22. Soft Head -": "Headshots do +2 Dmg",
    "23. Cowardly -": "Intimidation causes Panic",
    "24. Pea Brain -": "-2 Int",
    "25. Mentally....Impaired -": "-20 IQ",
    "26. Ugly -": "-2 Cha",
    "27. Unfortified -": "Nat Armor is 1/2",
    "28. Unbalanced -": "Player is easily knocked over",
    "29. Butter Fingers -": "Failed Attack rolls mean you drop your weapon",
    "30. Toothpick -": "-1 Wound Slot and ???",
    "31. Weaker -": "-10 Health for selected Body Parts or Limb groups",
    "32. Limitations -": "Creature can only have 3 Gifts",
    "33. Anxiety Disorder -": "+5 to all Mental Damages",
    "34. PTSD -": "Random flashbacks and Hallucinations(DM liesure)(Having 1/2 Mental Health for more than 4 rounds))",
    "35. Psychotic -": "Always in a Hallucination(Happens after 4 failed attempts to lower overflown Mental Health limit)",
    "36. Narcissistic -": "Can't have Friends",
    "37. Paranoia -": "Always Alert, but can only have Associates(+2 to Diff for enemy Ambushes/Surprise Attacks)",
    "38. Schizoid -": "Can't have any form of Friendship"

    }

for x,y in curses.items():
  print(x,y,"\n")

my_curses = {



    }

curse_dec = input("Pick your CURSE: ")

gift_dec = input("Would you like a gift?: ")


gifts = {

    "1. Strong Immunity -": "Can roll on the same turn of being poisoned to negate it",
    "2. Thick Skin -": "Immune to Flesh Wounds",
    "3. Deep Voice -": "+2 to Intimidate",
    "4. Alert -": "+2 to noticing Ambush/Surprise attack(Can dodge the attack)",
    "5. Unafraid -": "Being Intimidated gives a bonus",
    "6. Thick Skull -": "Headshots do -2 Dmg",
    "7. Savant -": "20 IQ",
    "8. Ferocity -": "Ignore Negative aliments for 3 Rounds",
    "9. Fast Hands -": "Don't roll to Reload",
    "10. Genius -": "+2 Int",
    "11. Roid Rage -": "Ignore Size Class Diff for a short bit",
    "12. Hyperthymesia -": "+2 Max Knowledge(Can go past the usually Max)",
    "13. Techie -": "+2 Hacking/Piloting/Enginnering",
    "14. Good Looks -": "+2",
    "15. Runner -": "+1 Tiles",
    "16. Thickset -": "Only 12 causes a Wound",
    "17. Iron Ant -": "Use Melee Dmg of 1 Size Class higher",
    "18. Titanium Ant -": "Use Melee Dmg of 2 Size Class higher",
    "19. The Mountain -": "+4 Diff to people trying to Knockdown/Back",
    "20. Light Footed -": "-1 Diff while Moving Silently",
    "20. Infectious Laugh -": "+3 to Wound Die Rolls in Conversation",
    "21. Fortified  -": "Nat Armor + 1/2",
    "22. Dexterous -": "Good at Sleight of hand/Lock picking",
    "23. Iron Grip -": "Can't drop weapon from Failed rolls and add +4 Diff to Disarm Attacks",
    "24. Eagle Eye -": "+2 to Ranged Attacks",
    "25. Spartans Arms -": "1 Additinal Wound slot for arms",
    "26. Hollowed Out -": "A gift for Demi Gods. Needs Impale in order to work and is only obtainable from getting 25 Str. This fills a limb up with all Open Wounds and does Crit dmg. The Diff is x2 to perform however and can only be used every 5 turns.",
    "27. Aim for the Eyes -": "Reduces Diff of Eye attacks to 6",
    "28. Mental Fortress -": "-10 from Mental Damages",
    "29. Fear Not -": "Phobias can be rolled for reduction",
    "30. Functional Insanity -": "Going insane or worse doesn't take the player out of the world. Just gives random quarks to them.",
    "31. Got Nerve?  -": "At 1/2 Mental Health the negative effects on attributes instead boost the creature. After 10 more points of mental damage, this effect doesn't apply.",
    "32. No Regrets -": " PTSD can't happen",

    }

if gift_dec == "yes" or gift_dec == "y":

    for x,y in gifts.items():
        print(x,y,"\n")

gift_pick = input("Pick your GIFT: ")
