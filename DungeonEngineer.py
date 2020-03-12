#!python3.4


import sys
import random

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMainWindow, QApplication
from UI_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        self.btn_Random_Loot.clicked.connect(self.btn_Random_Loot_clicked)
        self.btn_Common.clicked.connect(self.btn_Common_clicked)
        self.btn_Uncommon.clicked.connect(self.btn_Uncommon_clicked)
        self.btn_Rare.clicked.connect(self.btn_Rare_clicked)
        self.btn_Very_Rare.clicked.connect(self.btn_Very_Rare_clicked)
        self.btn_Legendary.clicked.connect(self.btn_Legendary_clicked)
        self.btn_Gold.clicked.connect(self.btn_Gold_clicked)
        self.btn_Potion.clicked.connect(self.btn_Potion_clicked)
        self.btn_Armor.clicked.connect(self.btn_Armor_clicked)
        self.btn_Weapon.clicked.connect(self.btn_Weapon_clicked)
        self.btn_Treasure.clicked.connect(self.btn_Treasure_clicked)
        self.btn_Scroll.clicked.connect(self.btn_Scroll_clicked)
        self.btn_Lingering_Injuries.clicked.connect(self.btn_Lingering_Injuries_clicked)
        self.btn_Madness.clicked.connect(self.btn_Madness_clicked)
        self.btn_Wild_Magic.clicked.connect(self.btn_Wild_Magic_clicked)
        self.btn_Weather.clicked.connect(self.btn_Weather_clicked)
        self.btn_Traps.clicked.connect(self.btn_Traps_clicked)
        self.btn_Tricks.clicked.connect(self.btn_Tricks_clicked)
        self.btn_Lair_Effects.clicked.connect(self.btn_Lair_Effects_clicked)
        self.btn_Monster.clicked.connect(self.btn_Monster_clicked)
        self.btn_Random_Encounter.clicked.connect(self.btn_Random_Encounter_clicked)
        self.btn_Random_Names.clicked.connect(self.btn_Random_Names_clicked)
        self.btn_Drow_Name.clicked.connect(self.btn_Drow_Name_clicked)
        self.btn_Item_Origin.clicked.connect(self.btn_Item_Origin_clicked)
        self.btn_Enchantment.clicked.connect(self.btn_Enchantment_clicked)
        self.btn_NPC_Generator.clicked.connect(self.btn_NPC_Generator_clicked)
        self.btn_Quest_Generator.clicked.connect(self.btn_Quest_Generator_clicked)
        self.btn_Plot_Hook.clicked.connect(self.btn_Plot_Hook_clicked)
        self.btn_Tavern_Generator.clicked.connect(self.btn_Tavern_Generator_clicked)
        self.btn_Downtime.clicked.connect(self.btn_Downtime_clicked)
        self.btn_Puzzle.clicked.connect(self.btn_Puzzle_clicked)
        self.btn_Riddle.clicked.connect(self.btn_Riddle_clicked)

        self.potion_loot = []
        self.uncommon_loot = []
        self.rare_loot = []
        self.very_rare_loot = []
        self.legendary_loot = []
        self.spell_loot = []
        self.name_list = []
        self.common_loot = []
        self.enchantments = []
        self.weapons = []
        self.armors = []
        self.drow_table1 = []
        self.drow_table2 = []
        self.drow_table3 = []
        self.drow_table4 = []
        self.wild_magic = []
        self.traps = []

        with open('Dungeon Engineer Database/Armors.txt') as armor_file:
            for line in armor_file:
                self.armors.append(line)
        with open('Dungeon Engineer Database/Weapons.txt') as weapons_file:
            for line in weapons_file:
                self.weapons.append(line)
        with open('Dungeon Engineer Database/Common.txt') as common_file:
            for line in common_file:
                line = line.split(':')
                self.common_loot.append(line)
        with open('Dungeon Engineer Database/Uncommon.txt') as uncommon_file:
            for line in uncommon_file:
                line = line.split(':')
                self.uncommon_loot.append(line)
        with open('Dungeon Engineer Database/Rare.txt') as rare_file:
            for line in rare_file:
                line = line.split(':')
                self.rare_loot.append(line)
        with open('Dungeon Engineer Database/Very Rare.txt') as very_rare_file:
            for line in very_rare_file:
                line = line.split(':')
                self.very_rare_loot.append(line)
        with open('Dungeon Engineer Database/Legendary.txt') as legendary_file:
            for line in legendary_file:
                line = line.split(':')
                self.legendary_loot.append(line)
        with open('Dungeon Engineer Database/Spells.txt') as spells_file:
            for line in spells_file:
                line = line.split(':')
                self.spell_loot.append(line)
        with open('Dungeon Engineer Database/Potions.txt') as potions_file:
            for line in potions_file:
                line = line.split(':')
                self.potion_loot.append(line)
        with open('Dungeon Engineer Database/Names.txt') as names_file:
            for line in names_file:
                line = line.split(':')
                self.name_list.append(line)
        with open('Dungeon Engineer Database/Enchantments.txt') as enchantment_file:
            for line in enchantment_file:
                line = line.split(':')
                self.enchantments.append(line)
        with open('Dungeon Engineer Database/Drow Table1.txt') as f:
            for line in f:
                line = line.split(':')
                self.drow_table1.append(line)
        with open('Dungeon Engineer Database/Drow Table2.txt') as f:
            for line in f:
                line = line.split(':')
                self.drow_table2.append(line)
        with open('Dungeon Engineer Database/Drow Table3.txt') as f:
            for line in f:
                line = line.split(':')
                self.drow_table3.append(line)
        with open('Dungeon Engineer Database/Drow Table4.txt') as f:
            for line in f:
                line = line.split(':')
                self.drow_table4.append(line)
        with open('Dungeon Engineer Database/Wild Magic.txt') as f:
            for line in f:
                self.wild_magic.append(line)
        with open('Dungeon Engineer Database/Traps.txt') as f:
            for line in f:
                line = line.split(':')
                self.traps.append(line)

        common_length = "\tCommon loot loaded: " + str(len(self.common_loot)) + "\n"
        uncommon_length = "\tUncommon loot loaded: " + str(len(self.uncommon_loot)) + "\n"
        rare_length = "\tRare loot loaded: " + str(len(self.rare_loot)) + "\n"
        very_rare_length = "\tVery Rare loot loaded: " + str(len(self.very_rare_loot)) + "\n"
        legendary_length = "\tLegendary loot loaded: " + str(len(self.legendary_loot)) + "\n"
        spell_length = "\tSpells loaded: " + str(len(self.spell_loot)) + "\n"
        name_length = "\tNames loaded: " + str(len(self.name_list)) + "\n"
        potion_length = "\tPotions loaded: " + str(len(self.potion_loot)) + "\n"
        enchantments_length = "\tEnchantments loaded: " + str(len(self.enchantments)) + "\n"

        self.textEdit.append('Dungeon Engineer Toolkit v1.2\n\n')
        self.textEdit.append('Customizable loot tables:\n')
        self.textEdit.append(common_length)
        self.textEdit.append(uncommon_length)
        self.textEdit.append(rare_length)
        self.textEdit.append(very_rare_length)
        self.textEdit.append(legendary_length)
        self.textEdit.append(spell_length)
        self.textEdit.append(name_length)
        self.textEdit.append(potion_length)
        self.textEdit.append(enchantments_length)

    def roll(self, sides):
        return random.randint(1, sides)

    def spacer(self):
        self.textEdit.append(50 * '~')

    def btn_Random_Loot_clicked(self):
        difficulty = str(self.comboBox_Difficulty.currentText())
        level = self.spinBox_Level.value()
        self.spacer()
        num = self.roll(100)

        common = 0
        uncommon = 0
        rare = 0
        very_rare = 0
        legendary = 0

        #Find number of items to be generated
        if difficulty == 'Easy':
            if num <= 50:
                self.textEdit.append('\nLooks like the good items were already nicked\n\n')
            elif num <= 70:
                common += 1
            elif num <= 90:
                common += self.roll(2)
            elif num <= 96:
                common += self.roll(2)
                uncommon += 1
            elif num <= 99:
                common += 2
                uncommon += self.roll(2)
            elif num == 100:
                common += 2
                uncommon += 2
                rare += 1
        elif difficulty == 'Average':
            if num <= 25:
                self.textEdit.append('\nLooks like the good items were already nicked\n')
            elif num <= 50:
                common += 1
            elif num <= 70:
                common += self.roll(2)
            elif num <= 90:
                common += self.roll(2)
                uncommon += 1
            elif num <= 96:
                common += 2
                uncommon += self.roll(2)
                rare += 1
            elif num <= 100:
                common += 2
                uncommon += 2
                rare += self.roll(2)
                very_rare += 1
        elif difficulty == 'Difficult':
            if num <= 25:
                common += 1
            elif num <= 50:
                common += self.roll(2)
            elif num <= 70:
                common += self.roll(2)
                uncommon += 1
            elif num <= 90:
                common += 2
                uncommon += self.roll(2)
                rare += 1
            elif num <= 97:
                common += 2
                uncommon += 2
                rare += self.roll(2)
                very_rare += 1
            elif num <= 100:
                common += 2
                uncommon += 2
                rare += self.roll(2)
                very_rare += 1
                legendary += 1

        # Display loot
        self.btn_Gold_clicked()
        for x in range(self.roll(6)):
            self.btn_Common_clicked()
        if common >= 1:
            for x in range(common):
                item_type = self.roll(2)
                if item_type == 1:
                    armor = random.choice(self.weapons)
                    enchant = random.choice(self.enchantments)
                    item = armor + 'Enchant: ' + enchant[0] + '\nDescription: ' + enchant[1] + '\n'
                elif item_type == 2:
                    weapon = random.choice(self.weapons)
                    enchant = random.choice(self.enchantments)
                    item = weapon + 'Enchant: ' + enchant[0] + '\nDescription: ' + enchant[1] + '\n'
                self.textEdit.append(item)
        if uncommon >= 1:
            for x in range(uncommon):
                self.btn_Uncommon_clicked()
        if rare >= 1:
            for x in range(rare):
                self.btn_Rare_clicked()
        if very_rare >= 1:
            self.btn_Very_Rare_clicked()
        if legendary >= 1:
            self.btn_Legendary_clicked()
        self.spacer()

    def btn_Common_clicked(self):
        common_item = random.choice(self.common_loot)
        text = 'Common item: ' + common_item[0] + '\nValue: ' + common_item[1]\
               + '\tWeight: ' + common_item[2] + '\nDescription: ' + common_item[3]
        self.textEdit.append(text)

    def btn_Uncommon_clicked(self):
        uncommon_item = random.choice(self.uncommon_loot)
        text = 'Uncommon item: ' + uncommon_item[0] + '\nDescription: ' + uncommon_item[1]
        self.textEdit.append(text)

    def btn_Rare_clicked(self):
        rare_item = random.choice(self.rare_loot)
        text = 'Rare item: ' + rare_item[0] + '\nDescription: ' + rare_item[1]
        self.textEdit.append(text)

    def btn_Very_Rare_clicked(self):
        very_rare_item = random.choice(self.very_rare_loot)
        text = 'Very Rare item: ' + very_rare_item[0] + '\nDescription: ' + very_rare_item[1]
        self.textEdit.append(text)

    def btn_Legendary_clicked(self):
        legendary_item = random.choice(self.legendary_loot)
        text = 'Legendary item: ' + legendary_item[0] + '\nDescription: ' + legendary_item[1]
        self.textEdit.append(text)

    def btn_Potion_clicked(self):
        potion_item = random.choice(self.potion_loot)
        text = potion_item[0] + '\nDescription: ' + potion_item[1]
        self.textEdit.append(text)

    def btn_Weapon_clicked(self):
        weapon = random.choice(self.weapons)
        text = weapon
        self.textEdit.append(text)

    def btn_Armor_clicked(self):
        armor = random.choice(self.armors)
        text = armor
        self.textEdit.append(text)

    def btn_Gold_clicked(self):
        def challenge0_4():
            num = self.roll(100)
            copper = 0
            silver = 0
            electrum = 0
            gold = 0
            platinum = 0
            if num <= 30:
                copper = str(self.roll(30)) + ' copper pieces'
            elif num <= 60:
                silver = str(self.roll(24)) + ' silver pieces'
            elif num <= 70:
                electrum = str(self.roll(18)) + ' electrum pieces'
            elif num <= 95:
                gold = str(self.roll(18)) + ' gold pieces'
            else:
                platinum = str(self.roll(6)) + ' platinum pieces'
            coins = ''
            if copper != 0:
                coins += copper + '\n'
            if silver != 0:
                coins += silver + '\n'
            if electrum != 0:
                coins += electrum + '\n'
            if gold != 0:
                coins += gold + '\n'
            if platinum != 0:
                coins += platinum + '\n'
            return coins

        def challenge5_10():
            num = self.roll(100)
            copper = 0
            silver = 0
            electrum = 0
            gold = 0
            platinum = 0
            if num <= 30:
                copper = str(self.roll(4800)) + ' copper pieces'
                electrum = str(self.roll(60)) + ' electrum pieces'
            elif num <= 60:
                silver = str(self.roll(360)) + ' silver pieces'
                gold = str(self.roll(120)) + ' gold pieces'
            elif num <= 70:
                electrum = str(self.roll(180)) + ' electrum pieces'
                gold = str(self.roll(120)) + ' gold pieces'
            elif num <= 95:
                gold = str(self.roll(240)) + ' gold pieces'
            else:
                gold = str(self.roll(120)) + ' gold pieces'
                platinum = str(self.roll(18)) + ' platinum pieces'
            coins = ''
            if copper != 0:
                coins += copper + '\n'
            if silver != 0:
                coins += silver + '\n'
            if electrum != 0:
                coins += electrum + '\n'
            if gold != 0:
                coins += gold + '\n'
            if platinum != 0:
                coins += platinum + '\n'
            return coins

        def challenge11_16():
            num = self.roll(100)
            silver = 0
            electrum = 0
            gold = 0
            platinum = 0
            if num <= 20:
                silver = str(self.roll(2400)) + ' silver pieces'
                gold = str(self.roll(600)) + ' gold pieces'
            elif num <= 35:
                electrum = str(self.roll(600)) + ' electrum pieces'
                gold = str(self.roll(600)) + ' gold pieces'
            elif num <= 75:
                gold = str(self.roll(1200)) + ' gold pieces'
                platinum = str(self.roll(60)) + ' platinum pieces'
            else:
                gold = str(self.roll(1200)) + ' gold pieces'
                platinum = str(self.roll(120)) + ' platinum pieces'
            coins = ''

            if silver != 0:
                coins += silver + '\n'
            if electrum != 0:
                coins += electrum + '\n'
            if gold != 0:
                coins += gold + '\n'
            if platinum != 0:
                coins += platinum + '\n'
            return coins

        def challenge17():
            num = self.roll(100)
            electrum = 0
            gold = 0
            platinum = 0
            if num <= 15:
                electrum = str(self.roll(12000)) + ' electrum pieces'
                gold = str(self.roll(4800)) + ' gold pieces'
            elif num <= 55:
                gold = str(self.roll(6000)) + ' gold pieces'
                platinum = str(self.roll(600)) + ' platinum pieces'
            else:
                gold = str(self.roll(6000)) + ' gold pieces'
                platinum = str(self.roll(1200)) + ' platinum pieces'
            coins = ''

            if electrum != 0:
                coins += electrum + '\n'
            if gold != 0:
                coins += gold + '\n'
            if platinum != 0:
                coins += platinum + '\n'
            return coins

        difficulty = str(self.comboBox_Difficulty.currentText())
        level = self.spinBox_Level.value()

        if level <= 4:
            self.textEdit.append(challenge0_4())
        elif level <= 10:
            self.textEdit.append(challenge5_10())
        elif level <= 16:
            self.textEdit.append(challenge11_16())
        else:
            self.textEdit.append(challenge17())

    def btn_Treasure_clicked(self):
        gemstone10 = [
            'azurite',
            'banded agate',
            'blue quartz',
            'eye agate',
            'hematite',
            'lapis lazuli',
            'malachite',
            'moss agate',
            'obsidian',
            'rhodochrosite',
            'tiger eye',
            'turquoise'
        ]
        gemstone50 = [
            'bloodstone',
            'carnelian',
            'chalcedony',
            'chrysoprase',
            'citrine',
            'jasper',
            'moonstone',
            'onyx',
            'quartz',
            'sardonyx',
            'star rose',
            'zircon'
        ]
        gemstone100 = [
            'amber',
            'amethyst',
            'chrysoberyl',
            'coral',
            'garnet',
            'jade',
            'jet',
            'pearl',
            'spinel',
            'tourmaline'
        ]
        gemstone500 = [
            'alexandrite',
            'aquamarine',
            'black pearl',
            'blue spinel',
            'peridot',
            'topaz'
        ]
        gemstone1000 = [
            'black opal',
            'blue sapphire',
            'emerald',
            'fire opal',
            'opal',
            'star ruby',
            'star sapphire',
            'yellow sapphire'
        ]
        gemstone5000 = [
            'black sapphire',
            'diamond',
            'jacinth',
            'ruby'
        ]
        art25 = [
            'silver ewer',
            'carved bone statuette',
            'small gold bracelet',
            'cloth-of-gold vestments',
            'black velvet mask stitched with silver thread',
            'copper chalice with silver filigree',
            'pair of engraved bone dice',
            'small mirror set in a painted wooden frame',
            'embroidered silk handkerchief',
            'gold locket with a painted portrait inside'
        ]
        art250 = [
            'gold ring set with bloodstones',
            'carved ivory statuette',
            'large gold bracelet',
            'silver necklace with a gemstone pendant',
            'bronze crown',
            'silk robe with gold embroidery',
            'large well-made tapestry',
            'brass mug with jade inlay',
            'box of turquoise animal figurines',
            'gold bird cage with electrum filigree'
        ]
        art750 = [
            'silver chalice set with moonstones',
            'silver-plated steel longsword with jet set in hilt',
            'carved harp of exotic wood with ivory inlay and zircon gems',
            'small gold idol',
            'gold dragon comb set with red garnets as eyes',
            'bottle stopper cork embossed with gold leaf and set with amethysts',
            'ceremonial electrum dagger with a black pearl in the pommel',
            'silver and gold brooch',
            'obsidian statuette with gold fittings and inlay',
            'painted gold war mask'
        ]
        art2500 = [
            'fine gold chain set with a fire opal',
            'old masterpiece painting',
            'embroidered silk and velvet mantle set with numerous moonstones',
            'platinum bracelet set with a sapphire',
            'embroidered glove set with jewel chips',
            'jeweled anklet',
            'gold music box',
            'gold circlet set with four aquamarines',
            'eye patch with a mock eye set in blue sapphire and moonstone',
            'a necklace string of small pink pearls'
        ]
        art7500 = [
            'jeweled gold crown',
            'jeweled platinum ring',
            'small gold statuette set with rubies',
            'gold cup set with emeralds',
            'gold jewelry box with platinum filigree',
            'painted gold child\'s sarcophagus',
            'jade game board with solid gold playing pieces',
            'bejeweled ivory drinking horn with gold filigree'
        ]

        def magic1():
            number = self.roll(100)

            if number <= 50:
                self.textEdit.append('Potion of healing' + '\n')
            elif number <= 70:
                self.btn_Potion_clicked()
            elif number <= 90:
                self.btn_Scroll_clicked()
            elif number <= 98:
                self.textEdit.append('Potion of greater healing' + '\n')
            elif number <= 99:
                self.textEdit.append('Bag of holding' + '\n')
            elif number <= 100:
                self.textEdit.append('Driftglobe' + '\n')

        def magic2():
            number = self.roll(100)

            if number <= 15:
                self.textEdit.append('Potion of greater healing' + '\n')
            elif number <= 30:
                self.btn_Potion_clicked()
            elif number <= 40:
                self.textEdit.append('+1 ammunition' + '\n')
            elif number <= 60:
                self.btn_Scroll_clicked()
            elif number <= 70:
                self.btn_Common_clicked()
            elif number <= 80:
                self.btn_Uncommon_clicked()
            elif number <= 90:
                self.btn_Rare_clicked()
            elif number <= 100:
                self.btn_Very_Rare_clicked()

        def magic3():
            number = self.roll(100)

            if number <= 15:
                self.textEdit.append('Potion of superior healing' + '\n')
            elif number <= 30:
                self.textEdit.append('+2 ammunition' + '\n')
            elif number <= 50:
                self.btn_Potion_clicked()
            elif number <= 60:
                self.btn_Scroll_clicked()
            elif number <= 70:
                self.btn_Uncommon_clicked()
            elif number <= 80:
                self.btn_Rare_clicked()
            elif number <= 90:
                self.btn_Very_Rare_clicked()
            elif number <= 100:
                self.btn_Legendary_clicked()

        def magic4():
            number = self.roll(100)

            if number <= 20:
                self.textEdit.append('Potion of supreme healing' + '\n')
            elif number <= 40:
                self.btn_Potion_clicked()
            elif number <= 60:
                self.btn_Scroll_clicked()
            elif number <= 70:
                self.textEdit.append('+3 ammunition' + '\n')
            elif number <= 80:
                self.btn_Very_Rare_clicked()
            elif number <= 90:
                self.textEdit.append('Bag of devouring' + '\n')
            elif number <= 92:
                self.textEdit.append('Portable hole' + '\n')
            elif number <= 100:
                self.btn_Legendary_clicked()

        def magic5():
            number = self.roll(100)

            if number <= 30:
                self.btn_Scroll_clicked()
            elif number <= 40:
                self.btn_Potion_clicked()
            elif number <= 50:
                self.btn_Rare_clicked()
            elif number <= 65:
                self.btn_Very_Rare_clicked()
            elif number <= 80:
                self.textEdit.append('Arrow of slaying' + '\n')
            elif number <= 85:
                self.textEdit.append('Sovereign glue' + '\n')
            elif number <= 90:
                self.textEdit.append('Bag of holding' + '\n')
            elif number <= 95:
                self.textEdit.append('Bag of devouring' + '\n')
            elif number <= 100:
                self.textEdit.append('Portable hole' + '\n')

        def magic6():
            number = self.roll(100)

            if number <= 15:
                self.textEdit.append('+1 ' + self.btn_Weapon_clicked())
            elif number <= 30:
                self.textEdit.append('+2 ' + self.btn_Armor_clicked())
            elif number <= 40:
                self.btn_Uncommon_clicked()
            elif number <= 50:
                self.btn_Rare_clicked()
            elif number <= 65:
                self.textEdit.append('Adamantine ' + self.btn_Armor_clicked())
            elif number <= 85:
                self.btn_Very_Rare_clicked()
            elif number <= 100:
                self.btn_Legendary_clicked()

        def challenge4():
            number = self.roll(100)

            copper = str(self.roll(3600)) + ' copper pieces'
            silver = str(self.roll(1800)) + ' silver pieces'
            gold = str(self.roll(120)) + ' gold pieces'
            self.textEdit.append(copper + ' ' + silver + ' ' + gold + '\n')

            if number <= 16:
                for items in range(self.roll(11)):
                    self.textEdit.append(random.choice(gemstone10) + '\n')
                for item in range(self.roll(7)):
                    magic1()
            elif number <= 26:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art25) + '\n')
                for item in range(self.roll(7)):
                    magic1()
            elif number <= 36:
                for item in range(self.roll(11)):
                    self.textEdit.append(random.choice(gemstone50) + '\n')
                for item in range(self.roll(7)):
                    magic1()
            elif number <= 44:
                for item in range(self.roll(11)):
                    self.textEdit.append(random.choice(gemstone10) + '\n')
                for item in range(self.roll(7)):
                    magic1()
            elif number <= 52:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art25) + '\n')
                for item in range(self.roll(7)):
                    magic1()
            elif number <= 60:
                for item in range(self.roll(11)):
                    self.textEdit.append(random.choice(gemstone50) + '\n')
                for item in range(self.roll(7)):
                    magic2()
            elif number <= 65:
                for item in range(self.roll(11)):
                    self.textEdit.append(random.choice(gemstone10) + '\n')
                for item in range(self.roll(7)):
                    magic2()
            elif number <= 70:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art25) + '\n')
                for item in range(self.roll(7)):
                    magic3()
            elif number <= 75:
                for item in range(self.roll(11)):
                    self.textEdit.append(random.choice(gemstone50) + '\n')
                for item in range(self.roll(7)):
                    magic3()
            elif number <= 78:
                for item in range(self.roll(11)):
                    self.textEdit.append(random.choice(gemstone10) + '\n')
                for item in range(self.roll(7)):
                    magic4()
            elif number <= 80:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art25) + '\n')
                for item in range(self.roll(7)):
                    magic4()
            elif number <= 85:
                for item in range(self.roll(11)):
                    self.textEdit.append(random.choice(gemstone50) + '\n')
                for item in range(self.roll(7)):
                    magic4()
            elif number <= 92:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art25) + '\n')
                for item in range(self.roll(7)):
                    magic5()
            elif number <= 97:
                for item in range(self.roll(11)):
                    self.textEdit.append(random.choice(gemstone50) + '\n')
                for item in range(self.roll(7)):
                    magic5()
            elif number <= 99:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art25) + '\n')
                for item in range(self.roll(7)):
                    magic5()
            elif number <= 100:
                for item in range(self.roll(11)):
                    self.textEdit.append(random.choice(gemstone50) + '\n')
                for item in range(self.roll(7)):
                    magic6()

        def challenge10():
            number = self.roll(100)
            copper = str(self.roll(1200)) + ' copper pieces'
            silver = str(self.roll(12000)) + ' silver pieces'
            gold = str(self.roll(3600)) + ' gold pieces'
            platinum = str(self.roll(180)) + ' platinum pieces'
            self.textEdit.append(copper + ' ' + silver + ' ' + gold + ' ' + platinum + '\n')

            if number <= 10:
                for items in range(self.roll(7)):
                    self.textEdit.append(random.choice(art25) + '\n')
                for item in range(self.roll(7)):
                    magic1()
            elif number <= 16:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone50) + '\n')
                for item in range(self.roll(7)):
                    magic1()
            elif number <= 22:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone100) + '\n')
                for item in range(self.roll(7)):
                    magic1()
            elif number <= 28:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art250) + '\n')
                for item in range(self.roll(7)):
                    magic1()
            elif number <= 32:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art25) + '\n')
                for item in range(self.roll(7)):
                    magic1()
            elif number <= 36:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone50) + '\n')
                for item in range(self.roll(7)):
                    magic2()
            elif number <= 40:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone100) + '\n')
                for item in range(self.roll(7)):
                    magic2()
            elif number <= 44:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art250) + '\n')
                for item in range(self.roll(7)):
                    magic2()
            elif number <= 49:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art25) + '\n')
                for item in range(self.roll(7)):
                    magic2()
            elif number <= 54:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone50) + '\n')
                for item in range(self.roll(7)):
                    magic2()
            elif number <= 59:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone100) + '\n')
                for item in range(self.roll(7)):
                    magic2()
            elif number <= 63:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art250) + '\n')
                for item in range(self.roll(7)):
                    magic2()
            elif number <= 66:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art25) + '\n')
                for item in range(self.roll(7)):
                    magic3()
            elif number <= 69:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone50) + '\n')
                for item in range(self.roll(7)):
                    magic3()
            elif number <= 72:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone100) + '\n')
                for item in range(self.roll(7)):
                    magic3()
            elif number <= 74:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art250) + '\n')
                for item in range(self.roll(7)):
                    magic3()
            elif number <= 76:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art25) + '\n')
                for item in range(self.roll(7)):
                    magic3()
            elif number <= 78:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone50) + '\n')
                for item in range(self.roll(7)):
                    magic3()
            elif number <= 79:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone100) + '\n')
                for item in range(self.roll(7)):
                    magic4()
            elif number <= 80:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art250) + '\n')
                for item in range(self.roll(7)):
                    magic4()
            elif number <= 84:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art25) + '\n')
                for item in range(self.roll(7)):
                    magic4()
            elif number <= 88:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone50) + '\n')
                for item in range(self.roll(7)):
                    magic4()
            elif number <= 91:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone100) + '\n')
                for item in range(self.roll(7)):
                    magic4()
            elif number <= 94:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art250) + '\n')
                for item in range(self.roll(7)):
                    magic4()
            elif number <= 96:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone100) + '\n')
                for item in range(self.roll(7)):
                    magic4()
            elif number <= 98:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art250) + '\n')
                for item in range(self.roll(7)):
                    magic4()
            elif number <= 99:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone100) + '\n')
                for item in range(self.roll(7)):
                    magic4()
            elif number <= 100:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art250) + '\n')
                for item in range(self.roll(7)):
                    magic4()

        def challenge16():
            number = self.roll(100)

            gold = str(self.roll(24000)) + ' gold pieces'
            platinum = str(self.roll(3000)) + ' platinum pieces'
            self.textEdit.append(gold + ' ' + platinum + '\n')

            if number <= 6:
                for items in range(self.roll(7)):
                    self.textEdit.append(random.choice(art250) + '\n')
                for item in range(self.roll(7)):
                    magic2()
            elif number <= 9:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art750) + '\n')
                for item in range(self.roll(7)):
                    magic2()
            elif number <= 12:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone500) + '\n')
                for item in range(self.roll(7)):
                    magic2()
            elif number <= 15:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone1000) + '\n')
                for item in range(self.roll(7)):
                    magic2()
            elif number <= 19:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art250) + '\n')
                for item in range(self.roll(7)):
                    magic2()
            elif number <= 23:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art750) + '\n')
                for item in range(self.roll(7)):
                    magic2()
            elif number <= 26:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone500) + '\n')
                for item in range(self.roll(7)):
                    magic2()
            elif number <= 29:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone1000) + '\n')
                for item in range(self.roll(7)):
                    magic2()
            elif number <= 35:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art250) + '\n')
                for item in range(self.roll(7)):
                    magic3()
            elif number <= 40:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art750) + '\n')
                for item in range(self.roll(7)):
                    magic3()
            elif number <= 45:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone500) + '\n')
                for item in range(self.roll(7)):
                    magic3()
            elif number <= 50:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone1000) + '\n')
                for item in range(self.roll(7)):
                    magic3()
            elif number <= 54:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art250) + '\n')
                for item in range(self.roll(7)):
                    magic3()
            elif number <= 58:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art750) + '\n')
                for item in range(self.roll(7)):
                    magic3()
            elif number <= 62:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone500) + '\n')
                for item in range(self.roll(7)):
                    magic3()
            elif number <= 66:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone1000) + '\n')
                for item in range(self.roll(7)):
                    magic3()
            elif number <= 68:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art250) + '\n')
                for item in range(self.roll(7)):
                    magic4()
            elif number <= 70:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art750) + '\n')
                for item in range(self.roll(7)):
                    magic4()
            elif number <= 72:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone500) + '\n')
                for item in range(self.roll(7)):
                    magic4()
            elif number <= 74:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone1000) + '\n')
                for item in range(self.roll(7)):
                    magic4()
            elif number <= 76:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art250) + '\n')
                for item in range(self.roll(7)):
                    magic4()
            elif number <= 78:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art750) + '\n')
                for item in range(self.roll(7)):
                    magic4()
            elif number <= 80:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone500) + '\n')
                for item in range(self.roll(7)):
                    magic4()
            elif number <= 82:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone1000) + '\n')
                for item in range(self.roll(7)):
                    magic5()
            elif number <= 85:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art250) + '\n')
                for item in range(self.roll(7)):
                    magic5()
            elif number <= 88:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art750) + '\n')
                for item in range(self.roll(7)):
                    magic5()
            elif number <= 90:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone500) + '\n')
                for item in range(self.roll(7)):
                    magic5()
            elif number <= 92:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone1000) + '\n')
                for item in range(self.roll(7)):
                    magic5()
            elif number <= 94:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art250) + '\n')
                for item in range(self.roll(7)):
                    magic6()
            elif number <= 96:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(art750) + '\n')
                for item in range(self.roll(7)):
                    magic6()
            elif number <= 98:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone500) + '\n')
                for item in range(self.roll(7)):
                    magic6()
            elif number <= 100:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone1000) + '\n')
                for item in range(self.roll(7)):
                    magic6()

        def challenge17():
            number = self.roll(100)
            gold = str(self.roll(72000)) + ' gold pieces'
            platinum = str(self.roll(48000)) + ' platinum pieces'
            self.textEdit.append(gold + ' ' + platinum + '\n')

            if number <= 5:
                for items in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone1000) + '\n')
                for item in range(self.roll(7)):
                    magic3()
            elif number <= 8:
                for item in range(self.roll(9)):
                    self.textEdit.append(random.choice(art2500) + '\n')
                for item in range(self.roll(7)):
                    magic3()
            elif number <= 11:
                for item in range(self.roll(3)):
                    self.textEdit.append(random.choice(art7500) + '\n')
                for item in range(self.roll(7)):
                    magic3()
            elif number <= 14:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(gemstone5000) + '\n')
                for item in range(self.roll(7)):
                    magic3()
            elif number <= 22:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone1000) + '\n')
                for item in range(self.roll(7)):
                    magic4()
            elif number <= 30:
                for item in range(self.roll(9)):
                    self.textEdit.append(random.choice(art2500) + '\n')
                for item in range(self.roll(7)):
                    magic4()
            elif number <= 38:
                for item in range(self.roll(3)):
                    self.textEdit.append(random.choice(art7500) + '\n')
                for item in range(self.roll(7)):
                    magic4()
            elif number <= 46:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(gemstone5000) + '\n')
                for item in range(self.roll(7)):
                    magic4()
            elif number <= 52:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone1000) + '\n')
                for item in range(self.roll(7)):
                    magic4()
            elif number <= 58:
                for item in range(self.roll(9)):
                    self.textEdit.append(random.choice(art2500) + '\n')
                for item in range(self.roll(7)):
                    magic4()
            elif number <= 63:
                for item in range(self.roll(3)):
                    self.textEdit.append(random.choice(art7500) + '\n')
                for item in range(self.roll(7)):
                    magic4()
            elif number <= 68:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(gemstone5000) + '\n')
                for item in range(self.roll(7)):
                    magic4()
            elif number <= 69:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone1000) + '\n')
                for item in range(self.roll(7)):
                    magic5()
            elif number <= 70:
                for item in range(self.roll(9)):
                    self.textEdit.append(random.choice(art2500) + '\n')
                for item in range(self.roll(7)):
                    magic5()
            elif number <= 71:
                for item in range(self.roll(3)):
                    self.textEdit.append(random.choice(art7500) + '\n')
                for item in range(self.roll(7)):
                    magic5()
            elif number <= 72:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(gemstone5000) + '\n')
                for item in range(self.roll(7)):
                    magic5()
            elif number <= 74:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone1000) + '\n')
                for item in range(self.roll(7)):
                    magic5()
            elif number <= 76:
                for item in range(self.roll(9)):
                    self.textEdit.append(random.choice(art2500) + '\n')
                for item in range(self.roll(7)):
                    magic5()
            elif number <= 78:
                for item in range(self.roll(3)):
                    self.textEdit.append(random.choice(art7500) + '\n')
                for item in range(self.roll(7)):
                    magic6()
            elif number <= 80:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(gemstone5000) + '\n')
                for item in range(self.roll(7)):
                    magic6()
            elif number <= 85:
                for item in range(self.roll(17)):
                    self.textEdit.append(random.choice(gemstone1000) + '\n')
                for item in range(self.roll(7)):
                    magic6()
            elif number <= 90:
                for item in range(self.roll(9)):
                    self.textEdit.append(random.choice(art2500) + '\n')
                for item in range(self.roll(7)):
                    magic6()
            elif number <= 95:
                for item in range(self.roll(3)):
                    self.textEdit.append(random.choice(art7500) + '\n')
                for item in range(self.roll(7)):
                    magic6()
            elif number <= 100:
                for item in range(self.roll(7)):
                    self.textEdit.append(random.choice(gemstone5000) + '\n')
                for item in range(self.roll(7)):
                    magic6()

        level = self.spinBox_Level.value()
        self.spacer()
        self.textEdit.append('Treasure: \n')
        if level <= 4:
            self.textEdit.append(challenge4())
        elif level <= 10:
            self.textEdit.append(challenge10())
        elif level <= 16:
            self.textEdit.append(challenge16())
        else:
            self.textEdit.append(challenge17())
        self.spacer()

    def btn_Scroll_clicked(self):
        self.textEdit.append('Scroll: ' + random.choice(self.spell_loot)[0])

    def btn_Lingering_Injuries_clicked(self):
        injury = self.roll(20)

        if injury == 1:
            self.textEdit.append('Lose an Eye: You have disadvantage on Wisdom (Perception) checks '
                                 'that rely on sight and on ranged attack rolls. Magic such as '
                                 'the regenerate spell can restore the lost eye. If you have no '
                                 'eyes left after sustaining this injury, you are blinded.\n')
        elif injury == 2:
            self.textEdit.append('Lose an Arm or a Hand: You can no longer hold anything with two '
                                 'hands, and you can hold only a single object at a time. Magic '
                                 'such as the regenerate spell can restore the lost appendage.\n')
        elif injury == 3:
            self.textEdit.append('Lose a Foot or Leg: Your speed on foot is halved, and you must '
                                 'use a cane or crutch to move unless you have a peg leg or other '
                                 'prosthesis. You fall prone after using the Dash action. You have '
                                 'disadvantage on Dexterity checks made to balance. Magic such as the'
                                 ' regenerate spell can restore the lost appendage.\n')
        elif injury == 4:
            self.textEdit.append('Limp: Your speed on foot is reduced by 5 feet. You must make a DC 10 '
                                 'Dexterity saving throw after using the Dash action. If you fail the save, '
                                 'you fall prone. Magical healing removes the limp.\n')
        elif injury <= 7:
            self.textEdit.append('Internal Injury: Whenever you attempt an action in combat, you must'
                                 ' make a DC 15 Constitution saving throw. On a failed save, you '
                                 'lose your action and can not use reactions until the start of your '
                                 'next turn. The injury heals if you receive magical healing or if you '
                                 'spend ten days doing nothing but resting.\n')
        elif injury <= 10:
            self.textEdit.append('Broken Ribs: Whenever you attempt an action in combat, you must'
                                 ' make a DC 10 Constitution saving throw. On a failed save, you '
                                 'lose your action and can not use reactions until the start of your '
                                 'next turn. The injury heals if you receive magical healing or if you '
                                 'spend ten days doing nothing but resting.\n')
        elif injury <= 13:
            self.textEdit.append('Horrible Scar: You are disfigured to the extent that the wound can'
                                 ' not be easily concealed. You have disadvantage on Charisma (Persuasion)'
                                 ' checks and advantage on Charisma (Intimidation) checks. Magical healing '
                                 'of 6th level or higher, such as heal and regenerate, removes the scar.\n')
        elif injury <= 16:
            self.textEdit.append('Festering Wound: Your hit point maximum is reduced by 1 every 24 hours '
                                 'the wound persists. If your hit point maximum drops to 0, you die. The wound '
                                 'heals if you receive magical healing. Alternatively, someone can tend to the '
                                 'wound and make a DC 15 Wisdom (Medicine) check once every 24 hours. After ten '
                                 'successes, the wound heals.\n')
        elif injury <= 20:
            self.textEdit.append('Minor Scar: The scar does not have any adverse effect. Magical '
                                 'healing of 6th level or higher, such as heal and regenerate, removes the scar.\n')

    def btn_Madness_clicked(self):
        madness = str(self.comboBox_Madness.currentText())
        number = self.roll(100)
        madtime = self.roll(10)
        if madness == 'Short-term':
            self.textEdit.append('Short-term Madness(' + str(madtime) + ' mins): ')
            if number <= 20:
                self.textEdit.append('The character retreats into his or her mind and becomes paralyzed. '
                                     'The effect ends if the character takes any damage.')
            elif number <= 30:
                self.textEdit.append('The character becomes incapacitated and spends the duration screaming'
                                     ', laughing, or weeping.')
            elif number <= 40:
                self.textEdit.append('The character becomes frightened and must use his or her action'
                                     ' and movement each round to flee from the source of the fear.')
            elif number <= 50:
                self.textEdit.append('The character begins babbling and is incapable of normal speech'
                                     ' or spellcasting.')
            elif number <= 60:
                self.textEdit.append('The character must use his or her action each round to attack the'
                                     ' nearest creature.')
            elif number <= 70:
                self.textEdit.append('The character experiences vivid hallucinations and '
                                     'has disadvantage on ability checks')
            elif number <= 75:
                self.textEdit.append('The character does whatever anyone tells him or her to do that is'
                                     ' not obviously self-destructive.')
            elif number <= 80:
                self.textEdit.append('The character experiences an overpowering urge to eat something strange'
                                     ' such as dirt, slime, or offal.')
            elif number <= 90:
                self.textEdit.append('The character is stunned.')
            elif number <= 100:
                self.textEdit.append('The character falls unconscious.')
            self.textEdit.append('\n')
        elif madness == 'Long-term':
            madtime = self.roll(10) * 10
            self.textEdit.append('Long-term Madness(' + str(madtime) + ' hours): ')
            if number <= 10:
                self.textEdit.append('The character feels compelled to repeat a specific'
                                     ' action over and over, such as washing hands, touching things,'
                                     ' praying, or counting coins.')
            elif number <= 20:
                self.textEdit.append('The character experiences vivid hallucinations and'
                                     'has disadvantage on ability checks.')
            elif number <= 30:
                self.textEdit.append('The character suffers extreme paranoia. The character'
                                     ' has disadvantage on Wisdom and Charisma checks.')
            elif number <= 40:
                self.textEdit.append('The character regards something (usually the source of madness)'
                                     ' with intense revulsion, as if affected by the antipathy effect'
                                     'of the antipathy/sympathy spell.')
            elif number <= 45:
                self.textEdit.append('The character experiences a powerful delusion. Choose a potion. The'
                                     ' character imagines that he or she is under its effects.')
            elif number <= 55:
                self.textEdit.append('The character becomes attached to a "lucky charm", such'
                                     ' as a person or an object, and has '
                                     'disadvantage on attack rolls, ability checks, and saving'
                                     ' throws while more than 30 feet from it.')
            elif number <= 65:
                self.textEdit.append('The character is blinded(25%) or deafened(75%).')
            elif number <= 75:
                self.textEdit.append('The character experiences uncontrollable tremors or tics, '
                                     'which impose disadvantage on attack rolls, ability checks, '
                                     'and saving throws that involve Strength or Dexterity.')
            elif number <= 85:
                self.textEdit.append('The character suffers from partial amnesia. The character knows '
                                     'who he or she is and retains racial traits and class features, but '
                                     'does not recognize other people or remember anything that happened '
                                     'before the madness took effect.')
            elif number <= 90:
                self.textEdit.append('Whenever the character takes damage, he or she must succeed on a DC 15 '
                                     'Wisdom saving throw or be affected as though he or she failed a saving '
                                     'throw against the confusion spell. The confusion effect lats for 1 minute.')
            elif number <= 95:
                self.textEdit.append('The character loses the ability to speak.')
            elif number <= 100:
                self.textEdit.append('The character falls unconscious. No amount of jostling or damage can '
                                     'wake the character.')
            self.textEdit.append('\n')
        elif madness == 'Indefinite':
            self.textEdit.append('Indefinite madness(lasts until cured): ')
            if number <= 15:
                self.textEdit.append('Being drunk keeps me sane.')
            elif number <= 25:
                self.textEdit.append('I keep whatever I find.')
            elif number <= 30:
                self.textEdit.append('I try to become more like someone else I know, adopting his'
                                     ' or her style of dress, mannerisms, and name.')
            elif number <= 35:
                self.textEdit.append('I must bend the truth, exaggerate, or outright lie to be '
                                     'interesting to other people.')
            elif number <= 45:
                self.textEdit.append('Achieving my goal is the only thing of interest to me, '
                                     'and I will ignore everything else to pursue it.')
            elif number <= 50:
                self.textEdit.append('I find it hard to care about anything that goes on around me.')
            elif number <= 55:
                self.textEdit.append('I do not like the way people judge me all the time.')
            elif number <= 70:
                self.textEdit.append('I am the smartest, wisest, strongest, fastest, and most '
                                     'beautiful person I know.')
            elif number <= 80:
                self.textEdit.append('I am convinced that powerful enemies are hunting me, and their '
                                     'agents are everywhere I go. I am sure they are watching me all the time.')
            elif number <= 85:
                self.textEdit.append('There is only one person I can trust. And only I can see this special friend.')
            elif number <= 95:
                self.textEdit.append('I can not take anything seriously. The more serious the situation, the funnier '
                                     'I find it.')
            elif number <= 100:
                self.textEdit.append('I have discovered that I really like killing people.')
            self.textEdit.append('\n')

    def btn_Wild_Magic_clicked(self):
        self.textEdit.append('Wild Magic: ' + random.choice(self.wild_magic) + '\n')

    def btn_Weather_clicked(self):
        temperature = self.roll(20)
        wind = self.roll(20)
        precipitation = self.roll(20)
        self.spacer()
        self.textEdit.append('\n')
        self.textEdit.append('Temperature: ')
        tempchange = str(self.roll(4) * 10)
        if temperature <= 14:
            self.textEdit.append('Normal for the season')
        elif temperature <= 17:
            self.textEdit.append(tempchange + ' degrees colder than normal')
        elif temperature <= 20:
            self.textEdit.append(tempchange + ' degrees hotter than normal')

        self.textEdit.append('Wind: ')
        if wind <= 12:
            self.textEdit.append('No wind')
        elif wind <= 17:
            self.textEdit.append('Light wind')
        elif wind <= 20:
            self.textEdit.append('Strong wind')

        self.textEdit.append('Precipitation: ')
        if precipitation <= 12:
            self.textEdit.append('No precipitation')
        elif precipitation <= 17:
            self.textEdit.append('Light rain or light snowfall')
        elif precipitation <= 20:
            self.textEdit.append('Heavy rain or heavy snowfall')
        self.textEdit.append('\n')
        self.spacer()

    def btn_Traps_clicked(self):
        level = self.spinBox_Level.value()
        difficulty = str(self.comboBox_Difficulty.currentText())

        def damage_roll(dice):
            damage = 0
            for x in range(dice):
                damage += self.roll(10)
            return damage

        if level <= 4:
            if difficulty == 'Easy':
                damage = damage_roll(1)
            elif difficulty == 'Average':
                damage = damage_roll(2)
            elif difficulty == 'Difficult':
                damage = damage_roll(4)
        elif level <= 10:
            if difficulty == 'Easy':
                damage = damage_roll(2)
            elif difficulty == 'Average':
                damage = damage_roll(4)
            elif difficulty == 'Difficult':
                damage = damage_roll(10)
        elif level <= 16:
            if difficulty == 'Easy':
                damage = damage_roll(4)
            elif difficulty == 'Average':
                damage = damage_roll(10)
            elif difficulty == 'Difficult':
                damage = damage_roll(18)
        elif level <= 20:
            if difficulty == 'Easy':
                damage = damage_roll(10)
            elif difficulty == 'Average':
                damage = damage_roll(18)
            elif difficulty == 'Difficult':
                damage = damage_roll(24)

        if difficulty == 'Easy':
            save = 'Save: 10-11'
            atk_bonus = 'Attack bonus: +3 to +5'
        elif difficulty == 'Average':
            save = 'Save: 12-15'
            atk_bonus = 'Attack bonus: +6 to +8'
        elif difficulty == 'Difficult':
            save = 'Save: 16-20'
            atk_bonus = 'Attack bonus: +9 to +12'

        trap = random.choice(self.traps)

        self.textEdit.append('Trap: ' + trap[0] +
                             '\nDescription: ' + trap[1] +
                             '\nDamage: ' + str(damage) +
                             '\n' + save +
                             '\n' + atk_bonus + '\n')

    def btn_Tricks_clicked(self):
        self.textEdit.append('Tricks is still a work in progress\n')

    def btn_Lair_Effects_clicked(self):
        self.textEdit.append('Lair Effects is still a work in progress\n')

    def btn_Monster_clicked(self):
        self.textEdit.append('Monster is still a work in progress\n')

    def btn_Random_Encounter_clicked(self):
        self.textEdit.append('Random Encounter is still a work in progress\n')

    def btn_Random_Names_clicked(self):
        names = ''
        self.spacer()
        for name in range(9):
            name = random.choice(self.name_list)[0]
            names += 'Name: ' + name + '\n'
        self.textEdit.append(names)
        self.spacer()

    def btn_Drow_Name_clicked(self):
        decision1 = self.roll(5)
        gender = self.roll(2)
        if decision1 == 1:
            #roll once on table1 and once on table2
            name1 = random.choice(self.drow_table1)
            name2 = random.choice(self.drow_table2)
            if gender == 1:
                name = "Name: " + name1[0] + name2[0] + '\n'
            else:
                name = "Name: " + name1[1] + name2[1] + '\n'
            name_meaning = "Name meaning: " + name1[2] + ' ' + name2[2]

            house1 = random.choice(self.drow_table3)
            house2 = random.choice(self.drow_table4)
            house = "House: " + house1[0] + house2[0] + '\n'
            house_meaning = "House meaning: " + house1[1] + ' ' + house2[1] + '\n'

        if decision1 == 2:
            #roll once on table1 and twice on table2
            name1 = random.choice(self.drow_table1)
            name2 = random.choice(self.drow_table2)
            name3 = random.choice(self.drow_table2)
            if gender == 1:
                name = "Name: " + name1[0] + name2[0] + name3[0] + '\n'
            else:
                name = "Name: " + name1[1] + name2[1] + name3[1] + '\n'
            name_meaning = "Name meaning: " + name1[2] + ' ' + name2[2] + ' ' + name3[2]

            house1 = random.choice(self.drow_table3)
            house2 = random.choice(self.drow_table4)
            house = "House: " + house1[0] + house2[0] + '\n'
            house_meaning = "House meaning: " + house1[1] + ' ' + house2[1] + '\n'

        if decision1 == 3:
            #roll once on table1 and once on table2 add an apostrophe then roll again on table2
            name1 = random.choice(self.drow_table1)
            name2 = random.choice(self.drow_table2)
            name3 = random.choice(self.drow_table2)
            if gender == 1:
                name = "Name: " + name1[0] + name2[0] + '\'' + name3[0] + '\n'
            else:
                name = "Name: " + name1[1] + name2[1] + '\'' + name3[1] + '\n'
            name_meaning = "Name meaning: " + name1[2] + ' ' + name2[2] + ' ' + name3[2]

            house1 = random.choice(self.drow_table3)
            house2 = random.choice(self.drow_table4)
            house = "House: " + house1[0] + house2[0] + '\n'
            house_meaning = "House meaning: " + house1[1] + ' ' + house2[1] + '\n'

        if decision1 == 4:
            #roll once on table1 and once on table2 for first name then again for second name
            name1 = random.choice(self.drow_table1)
            name2 = random.choice(self.drow_table2)
            name3 = random.choice(self.drow_table2)
            if gender == 1:
                name = "Name: " + name1[0] + name2[0] + ' ' + name3[0] + '\n'
            else:
                name = "Name: " + name1[1] + name2[1] + ' ' + name3[1] + '\n'
            name_meaning = "Name meaning: " + name1[2] + ' ' + name2[2] + ' ' + name3[2]

            house1 = random.choice(self.drow_table3)
            house2 = random.choice(self.drow_table4)
            house = "House: " + house1[0] + house2[0] + '\n'
            house_meaning = "House meaning: " + house1[1] + ' ' + house2[1] + '\n'

        if decision1 == 5:
            #roll once on table2 add an apostrophe then roll once on table1 and once on table2
            name1 = random.choice(self.drow_table1)
            name2 = random.choice(self.drow_table2)
            name3 = random.choice(self.drow_table2)
            if gender == 1:
                name = "Name: " + name2[0] + '\'' + name1[0] + name2[0] + '\n'
            else:
                name = "Name: " + name2[1] + '\'' + name1[1] + name2[1] + '\n'
            name_meaning = "Name meaning: " + name1[2] + ' ' + name2[2] + ' ' + name3[2]

            house1 = random.choice(self.drow_table3)
            house2 = random.choice(self.drow_table4)
            house = "House: " + house1[0] + house2[0] + '\n'
            house_meaning = "House meaning: " + house1[1] + ' ' + house2[1] + '\n'

        self.textEdit.append(name)
        self.textEdit.append(house)
        self.textEdit.append(name_meaning)
        self.textEdit.append(house_meaning)

    def btn_Item_Origin_clicked(self):
        num = self.roll(20)
        origin = ''
        if num == 1:
            origin = "Abyssmal: made from demon materials with runes, owner suffers nightmares " \
                     "but forgets upon awakening"
        elif num <= 4:
            origin = "Ancient Human: Old item from human ancestry that is tied to a person or place"
        elif num == 5:
            origin = "Celestial: light, 1/2 weight, feathered wings, suns, or other good " \
                     "symbols, evil creatures are put off by its presence"
        elif num == 6:
            origin = "Draconic: made by dragons, grows warm when within 100 feet of a dragon"
        elif num == 7:
            origin = "Drow: pitch black, 1/2 weight, might break if exposed to sun for extended time"
        elif num <= 10:
            origin = "Dwarven: Durable, very hard to break"
        elif num == 11:
            origin = "Elemental(air): light, 1/2 weight, but tough as normal, fabrics are whispy"
        elif num == 12:
            origin = "Elemental(earth): made of stone, weighs normal, cloth and leather are studded with polished rock"
        elif num == 13:
            origin = "Elemental(fire): warm to touch, sigils of flames and efreets"
        elif num == 14:
            origin = "Elemental(water): fish scales replace leather or cloth, seashells " \
                     "replace metal portions, hard as any metal"
        elif num <= 17:
            origin = "Elven: 1/2 weight, flexible"
        elif num == 18:
            origin = "Fiendish: black iron with runes that are warm to the touch, good " \
                     "creatures are put off by its presence"
        elif num == 19:
            origin = "Giant: oversized but still usable without penalty"
        elif num == 20:
            origin = "Gnome: item appears unremarkable and worn but is perfectly fine"
        self.textEdit.append(origin + '\n')

    def btn_Enchantment_clicked(self):
        enchant = random.choice(self.enchantments)
        self.textEdit.append('Enchant: ' + enchant[0] + '\nDescription: ' + enchant[1])

    def btn_NPC_Generator_clicked(self):
        self.textEdit.append('NPC Generator is still a work in progress\n')

    def btn_Quest_Generator_clicked(self):
        self.textEdit.append('Quest Generator is still a work in progress\n')

    def btn_Plot_Hook_clicked(self):
        self.textEdit.append('Plot Hook is still a work in progress\n')

    def btn_Tavern_Generator_clicked(self):
        self.textEdit.append('Tavern Generator is still a work in progress\n')

    def btn_Downtime_clicked(self):
        self.textEdit.append('Downtime is still a work in progress\n')

    def btn_Riddle_clicked(self):
        self.textEdit.append('Riddle is still a work in progress\n')

    def btn_Puzzle_clicked(self):
        self.textEdit.append('Puzzle is still a work in progress\n')

if __name__ == '__main__':

    app = QApplication(sys.argv)

    form = MainWindow()
    form.show()

    sys.exit(app.exec_())