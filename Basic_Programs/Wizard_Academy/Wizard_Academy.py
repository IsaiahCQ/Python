class Wizard:
   def __init__(self, name):
      self.name = name
      self.health = 100
      self.mana = 100
      self.spells = {}

   def learnSpell(self, spellName, spellPower):
      self.spells[spellName] = spellPower

   def castSpell(self, spell, target):
      if self.mana > 0:
          self.mana -= self.spells[spell]
          target.health -= self.spells[spell]

   def heal(self):
       if self.mana >= 0:
          self.mana -= 10
          self.health += 10

   def rechargeMana(self):
          self.mana += 10

spellLibrary = [
    {"fireblast": 5},
    {"iceblast": 7},
    {"electroshock": 10},
    {"lightningbolt": 15},
    {"dragon's breath": 17},
    {"blizzard": 20},
    {"glacier": 25},
    {"thunderstorm": 27},
    {"hellfire": 30}
]


while True:
    print("Hi, would you like to try my wizard academy simulation?")
    print("Type yes if you wish to try it and type no if you don't.")
    academychoice = input()
    if academychoice == "yes":
        print("What do you want to name your wizard?")
        goodWizard  = Wizard(input())
        print("Your wizard is now named " + goodWizard.name + ".")

        while True:
            print("Would you like to learn a spell " + goodWizard.name  + "?")
            learnaspell = input()

            if learnaspell == "yes":
                print(goodWizard.name + ", here's a list of the spells you can learn:")
                for spell in spellLibrary:
                    print(spell)
                print("What spell do you wish to learn?")
                spell = input()

                if spell  == "fireblast":
                    goodWizard.spells["fireblast"] = 5
                    print(goodWizard.name + " learned fireblast.")

                elif spell  == "iceblast":
                    goodWizard.spells["iceblast"] = 7
                    print(goodWizard.name + " learned iceblast.")

                elif spell  == 'electroshock':
                    goodWizard.spells['electroshock'] = 10
                    print(goodWizard.name + " learned electroshock.")

                elif spell  == "lightningbolt":
                    goodWizard.spells["lightningbolt"] = 15
                    print(goodWizard.name + " learned lightningbolt.")

                elif spell  == "dragon's breath":
                    goodWizard.spells["dragon's breath"] = 17
                    print(goodWizard.name + " learned dragon's breath.")

                elif spell  == "blizzard":
                    goodWizard.spells["blizzard"] = 20
                    print(goodWizard.name + " learned blizzard.")

                elif spell  == "glacier":
                    goodWizard.spells["glacier"] = 25
                    print(goodWizard.name + " learned glacier.")

                elif spell  == "thunderstorm":
                    goodWizard.spells["thunderstorm"] = 27
                    print(goodWizard.name + " learned thunderstorm.")

                elif spell  == "hellfire":
                    goodWizard.spells["hellfire"] = 30
                    print(goodWizard.name + " hellfire.")

            else:
                break

        print("Would you like to see the list of spells you know?")
        seelistchoice = input()

        if seelistchoice == "yes":
            print(goodWizard.name + " knows the following spells: " + str (goodWizard.spells))
            break

        else:
            break

badWizard = Wizard("Gargamel")
print(badWizard.name + " is trying to kidnap smurfs, you need to stop him.")
print(goodWizard.name + ", you need to lower " + badWizard.name + "'s health to zero to win.")
print("Type a to attack (and then select a spell), h to heal, and r to recharge your mana.")

while badWizard.health >= 0:
    if goodWizard.mana >= 0:
        print(goodWizard.name + ", do you want to attack(a), heal(h), or recharge(r) your mana?")
        battlechoice = input()

        if battlechoice == "a":
            print("Select a spell:" + str (goodWizard.spells))
            spelltouse = input()

            if spelltouse == "fireblast":
                goodWizard.castSpell("fireblast", badWizard)
                print(goodWizard.name + " used fireblast against " + badWizard.name + ".")
                print(goodWizard.name + " now has " + str (goodWizard.mana) + " mana, and "
                            + badWizard.name + " has " + str (badWizard.health) + " health.")
                if badWizard.health <= 0:
                    print("Congratulations " + goodWizard.name + ", you defeated " + badWizard.name + "!")
                    break

            elif spelltouse == "iceblast":
                goodWizard.castSpell("iceblast", badWizard)
                print(goodWizard.name + " used iceblast against " + badWizard.name + ".")
                print(goodWizard.name + " now has " + str (goodWizard.mana) + " mana, and "
                                      + badWizard.name + " has " + str (badWizard.health) + " health.")
                if badWizard.health <= 0:
                   print("Congratulations " + goodWizard.name + ", you defeated " + badWizard.name + "!")
                   break

            elif spelltouse == "electroshock":
                goodWizard.castSpell("electroshock", badWizard)
                print(goodWizard.name + " used electroschock against " + badWizard.name + ".")
                print(goodWizard.name + " now has " + str (goodWizard.mana) + " mana, and "
                            + badWizard.name + " has " + str (badWizard.health) + " health.")
                if badWizard.health <= 0:
                   print("Congratulations " + goodWizard.name + ", you defeated " + badWizard.name + "!")
                   break

            elif spelltouse == "lightningbolt":
                goodWizard.castSpell("lightningbolt", badWizard)
                print(goodWizard.name + " used lightningbolt against " + badWizard.name + ".")
                print(goodWizard.name + " now has " + str (goodWizard.mana) + " mana, and "
                            + badWizard.name + " has " + str (badWizard.health) + " health.")
                if badWizard.health <= 0:
                   print("Congratulations " + goodWizard.name + ", you defeated " + badWizard.name + "!")
                   break

            elif spelltouse == "dragon's breath":
                goodWizard.castSpell("dragon's breath", badWizard)
                print(goodWizard.name + " used dragon's breath against " + badWizard.name + ".")
                print(goodWizard.name + " now has " + str (goodWizard.mana) + " mana, and "
                            + badWizard.name + " has " + str (badWizard.health) + " health.")
                if badWizard.health <= 0:
                   print("Congratulations " + goodWizard.name + ", you defeated " + badWizard.name + "!")
                   break

            elif spelltouse == "blizzard":
                goodWizard.castSpell("blizzard", badWizard)
                print(goodWizard.name + " used blizzard against " + badWizard.name + ".")
                print(goodWizard.name + " now has " + str (goodWizard.mana) + " mana, and "
                            + badWizard.name + " has " + str (badWizard.health) + " health.")
                if badWizard.health <= 0:
                   print("Congratulations " + goodWizard.name + ", you defeated " + badWizard.name + "!")
                   break

            elif spelltouse == "glacier":
                goodWizard.castSpell("glacier", badWizard)
                print(goodWizard.name + " used glacier against " + badWizard.name + ".")
                print(goodWizard.name + " now has " + str (goodWizard.mana) + " mana, and "
                            + badWizard.name + " has " + str (badWizard.health) + " health.")
                if badWizard.health <= 0:
                   print("Congratulations " + goodWizard.name + ", you defeated " + badWizard.name + "!")
                   break

            elif spelltouse == "thunderstorm":
                goodWizard.castSpell("thunderstorm", badWizard)
                print(goodWizard.name + " used thunderstorm against " + badWizard.name + ".")
                print(goodWizard.name + " now has " + str (goodWizard.mana) + " mana, and "
                            + badWizard.name + " has " + str (badWizard.health) + " health.")
                if badWizard.health <= 0:
                   print("Congratulations " + goodWizard.name + ", you defeated " + badWizard.name + "!")
                   break

            elif spelltouse == "hellfire":
                goodWizard.castSpell("hellfire", badWizard)
                print(goodWizard.name + " used hellfire against " + badWizard.name + ".")
                print(goodWizard.name + " now has " + str (goodWizard.mana) + " mana, and "
                            + badWizard.name + " has " + str (badWizard.health) + " health.")
                if badWizard.health <= 0:
                   print("Congratulations " + goodWizard.name + ", you defeated " + badWizard.name + "!")
                   break



        elif battlechoice == "h":
            goodWizard.heal()
            print(goodWizard.name + " gained ten health-points, and now has " + str (goodWizard.health) + " health.")

        elif battlechoice == "r":
            goodWizard.rechargeMana()
            print(goodWizard.name + " gained ten mana-points, and now has " + str (goodWizard.mana) + " mana.")

    else:
        print(goodWizard.name + " doesn't have enough mana to perform a action this round")
        goodWizard.rechargeMana()
        print(goodWizard.name + " gained ten mana-points, and now has " + str (goodWizard.mana) + " mana.")

