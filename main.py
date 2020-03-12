#!python3.4
# Program: Dungeon Engineer's Toolkit
# Version: 1.2.2
# Date: 5/7/2015
# Author: Joseph L. Crandal
# Purpose: Assist with the backend of a tabletop rpg game master's work.

import sys, random

from operator import itemgetter
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMainWindow, QApplication
from UI_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)

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
        self.btn_Random_Names.clicked.connect(self.btn_Random_Names_clicked)
        self.btn_Drow_Name.clicked.connect(self.btn_Drow_Name_clicked)
        self.btn_Item_Origin.clicked.connect(self.btn_Item_Origin_clicked)
        self.btn_Enchantment.clicked.connect(self.btn_Enchantment_clicked)
        self.btn_Plot_Hook.clicked.connect(self.btn_Plot_Hook_clicked)
        self.btn_Downtime.clicked.connect(self.btn_Downtime_clicked)
        self.btn_Puzzle.clicked.connect(self.btn_Puzzle_clicked)
        self.btn_Riddle.clicked.connect(self.btn_Riddle_clicked)
        self.btn_Spellbook.clicked.connect(self.btn_Spellbook_clicked)
        self.btn_QuestGen.clicked.connect(self.btn_Quest_Generator_clicked)
        self.btnClear.clicked.connect(self.textClear)

        self.potion_loot = []
        self.uncommon_loot = []
        self.rare_loot = []
        self.very_rare_loot = []
        self.legendary_loot = []
        self.all_spells = []
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
        self.quests = []
        self.puzzle = []
        self.riddle = []
        self.plothook = []
        self.carousing = []

        self.bard_spells = []
        self.bard_0spells = []
        self.bard_1spells = []
        self.bard_2spells = []
        self.bard_3spells = []
        self.bard_4spells = []
        self.bard_5spells = []
        self.bard_6spells = []
        self.bard_7spells = []
        self.bard_8spells = []
        self.bard_9spells = []

        self.cleric_spells = []
        self.cleric_0spells = []
        self.cleric_1spells = []
        self.cleric_2spells = []
        self.cleric_3spells = []
        self.cleric_4spells = []
        self.cleric_5spells = []
        self.cleric_6spells = []
        self.cleric_7spells = []
        self.cleric_8spells = []
        self.cleric_9spells = []

        self.druid_spells = []
        self.druid_0spells = []
        self.druid_1spells = []
        self.druid_2spells = []
        self.druid_3spells = []
        self.druid_4spells = []
        self.druid_5spells = []
        self.druid_6spells = []
        self.druid_7spells = []
        self.druid_8spells = []
        self.druid_9spells = []

        self.paladin_spells = []
        self.paladin_1spells = []
        self.paladin_2spells = []
        self.paladin_3spells = []
        self.paladin_4spells = []
        self.paladin_5spells = []

        self.ranger_spells = []
        self.ranger_1spells = []
        self.ranger_2spells = []
        self.ranger_3spells = []
        self.ranger_4spells = []
        self.ranger_5spells = []

        self.sorcerer_spells = []
        self.sorcerer_0spells = []
        self.sorcerer_1spells = []
        self.sorcerer_2spells = []
        self.sorcerer_3spells = []
        self.sorcerer_4spells = []
        self.sorcerer_5spells = []
        self.sorcerer_6spells = []
        self.sorcerer_7spells = []
        self.sorcerer_8spells = []
        self.sorcerer_9spells = []

        self.warlock_spells = []
        self.warlock_0spells = []
        self.warlock_1spells = []
        self.warlock_2spells = []
        self.warlock_3spells = []
        self.warlock_4spells = []
        self.warlock_5spells = []
        self.warlock_6spells = []
        self.warlock_7spells = []
        self.warlock_8spells = []
        self.warlock_9spells = []

        self.wizard_spells = []
        self.wizard_0spells = []
        self.wizard_1spells = []
        self.wizard_2spells = []
        self.wizard_3spells = []
        self.wizard_4spells = []
        self.wizard_5spells = []
        self.wizard_6spells = []
        self.wizard_7spells = []
        self.wizard_8spells = []
        self.wizard_9spells = []

        with open('Dungeon Engineer Database/Armors.txt') as armor_file:
            for line in armor_file:
                line = line.rstrip('\n')
                self.armors.append(line)
        with open('Dungeon Engineer Database/Weapons.txt') as weapons_file:
            for line in weapons_file:
                line = line.rstrip('\n')
                self.weapons.append(line)
        with open('Dungeon Engineer Database/Common.txt') as common_file:
            for line in common_file:
                line = (line.rstrip('\n')).split(':')
                self.common_loot.append(line)
        with open('Dungeon Engineer Database/Uncommon.txt') as uncommon_file:
            for line in uncommon_file:
                line = (line.rstrip('\n')).split(':')
                self.uncommon_loot.append(line)
        with open('Dungeon Engineer Database/Rare.txt') as rare_file:
            for line in rare_file:
                line = (line.rstrip('\n')).split(':')
                self.rare_loot.append(line)
        with open('Dungeon Engineer Database/Very Rare.txt') as very_rare_file:
            for line in very_rare_file:
                line = (line.rstrip('\n')).split(':')
                self.very_rare_loot.append(line)
        with open('Dungeon Engineer Database/Legendary.txt') as legendary_file:
            for line in legendary_file:
                line = (line.rstrip('\n')).split(':')
                self.legendary_loot.append(line)
        with open('Dungeon Engineer Database/Potions.txt') as potions_file:
            for line in potions_file:
                line = (line.rstrip('\n')).split(':')
                self.potion_loot.append(line)
        with open('Dungeon Engineer Database/Names.txt') as names_file:
            for line in names_file:
                line = (line.rstrip('\n')).split(':')
                self.name_list.append(line)
        with open('Dungeon Engineer Database/Enchantments.txt') as enchantment_file:
            for line in enchantment_file:
                line = (line.rstrip('\n')).split(':')
                self.enchantments.append(line)
        with open('Dungeon Engineer Database/Drow Table1.txt') as f:
            for line in f:
                line = (line.rstrip('\n')).split(':')
                self.drow_table1.append(line)
        with open('Dungeon Engineer Database/Drow Table2.txt') as f:
            for line in f:
                line = (line.rstrip('\n')).split(':')
                self.drow_table2.append(line)
        with open('Dungeon Engineer Database/Drow Table3.txt') as f:
            for line in f:
                line = (line.rstrip('\n')).split(':')
                self.drow_table3.append(line)
        with open('Dungeon Engineer Database/Drow Table4.txt') as f:
            for line in f:
                line = (line.rstrip('\n')).split(':')
                self.drow_table4.append(line)
        with open('Dungeon Engineer Database/Wild Magic.txt') as f:
            for line in f:
                line = line.rstrip('\n')
                self.wild_magic.append(line)
        with open('Dungeon Engineer Database/Traps.txt') as f:
            for line in f:
                line = (line.rstrip('\n')).split(':')
                self.traps.append(line)
        with open('Dungeon Engineer Database/Puzzle.txt') as f:
            for line in f:
                line = line.rstrip('\n')
                self.puzzle.append(line)
        with open('Dungeon Engineer Database/Riddle.txt') as f:
            for line in f:
                line = line.rstrip('\n')
                self.riddle.append(line)
        with open('Dungeon Engineer Database/Plot Hook.txt') as f:
            for line in f:
                line = line.rstrip('\n')
                self.plothook.append(line)
        with open('Dungeon Engineer Database/Quests.txt') as f:
            for line in f:
                line = line.rstrip('\n')
                self.quests.append(line)
        with open('Dungeon Engineer Database/Carousing.txt') as f:
            for line in f:
                line = line.rstrip('\n')
                self.carousing.append(line)
        with open('Dungeon Engineer Database/Spells.txt') as f:
            for line in f:
                line = (line.rstrip('\n')).split(':')
                self.all_spells.append(line)

                if line[2] == 'bard':
                    self.bard_spells.append(line)
                    if line[1] == '0':
                        self.bard_0spells.append(line)
                    elif line[1] == '1':
                        self.bard_1spells.append(line)
                    elif line[1] == '2':
                        self.bard_2spells.append(line)
                    elif line[1] == '3':
                        self.bard_3spells.append(line)
                    elif line[1] == '4':
                        self.bard_4spells.append(line)
                    elif line[1] == '5':
                        self.bard_5spells.append(line)
                    elif line[1] == '6':
                        self.bard_6spells.append(line)
                    elif line[1] == '7':
                        self.bard_7spells.append(line)
                    elif line[1] == '8':
                        self.bard_8spells.append(line)
                    elif line[1] == '9':
                        self.bard_9spells.append(line)

                elif line[2] == 'cleric':
                    self.cleric_spells.append(line)
                    if line[1] == '0':
                        self.cleric_0spells.append(line)
                    elif line[1] == '1':
                        self.cleric_1spells.append(line)
                    elif line[1] == '2':
                        self.cleric_2spells.append(line)
                    elif line[1] == '3':
                        self.cleric_3spells.append(line)
                    elif line[1] == '4':
                        self.cleric_4spells.append(line)
                    elif line[1] == '5':
                        self.cleric_5spells.append(line)
                    elif line[1] == '6':
                        self.cleric_6spells.append(line)
                    elif line[1] == '7':
                        self.cleric_7spells.append(line)
                    elif line[1] == '8':
                        self.cleric_8spells.append(line)
                    elif line[1] == '9':
                        self.cleric_9spells.append(line)

                elif line[2] == 'druid':
                    self.druid_spells.append(line)
                    if line[1] == '0':
                        self.druid_0spells.append(line)
                    elif line[1] == '1':
                        self.druid_1spells.append(line)
                    elif line[1] == '2':
                        self.druid_2spells.append(line)
                    elif line[1] == '3':
                        self.druid_3spells.append(line)
                    elif line[1] == '4':
                        self.druid_4spells.append(line)
                    elif line[1] == '5':
                        self.druid_5spells.append(line)
                    elif line[1] == '6':
                        self.druid_6spells.append(line)
                    elif line[1] == '7':
                        self.druid_7spells.append(line)
                    elif line[1] == '8':
                        self.druid_8spells.append(line)
                    elif line[1] == '9':
                        self.druid_9spells.append(line)

                elif line[2] == 'paladin':
                    self.paladin_spells.append(line)
                    if line[1] == '1':
                        self.paladin_1spells.append(line)
                    elif line[1] == '2':
                        self.paladin_2spells.append(line)
                    elif line[1] == '3':
                        self.paladin_3spells.append(line)
                    elif line[1] == '4':
                        self.paladin_4spells.append(line)
                    elif line[1] == '5':
                        self.paladin_5spells.append(line)

                elif line[2] == 'ranger':
                    self.ranger_spells.append(line)
                    if line[1] == '1':
                        self.ranger_1spells.append(line)
                    elif line[1] == '2':
                        self.ranger_2spells.append(line)
                    elif line[1] == '3':
                        self.ranger_3spells.append(line)
                    elif line[1] == '4':
                        self.ranger_4spells.append(line)
                    elif line[1] == '5':
                        self.ranger_5spells.append(line)

                elif line[2] == 'sorcerer':
                    self.sorcerer_spells.append(line)
                    if line[1] == '0':
                        self.sorcerer_0spells.append(line)
                    elif line[1] == '1':
                        self.sorcerer_1spells.append(line)
                    elif line[1] == '2':
                        self.sorcerer_2spells.append(line)
                    elif line[1] == '3':
                        self.sorcerer_3spells.append(line)
                    elif line[1] == '4':
                        self.sorcerer_4spells.append(line)
                    elif line[1] == '5':
                        self.sorcerer_5spells.append(line)
                    elif line[1] == '6':
                        self.sorcerer_6spells.append(line)
                    elif line[1] == '7':
                        self.sorcerer_7spells.append(line)
                    elif line[1] == '8':
                        self.sorcerer_8spells.append(line)
                    elif line[1] == '9':
                        self.sorcerer_9spells.append(line)

                elif line[2] == 'warlock':
                    self.warlock_spells.append(line)
                    if line[1] == '0':
                        self.warlock_0spells.append(line)
                    elif line[1] == '1':
                        self.warlock_1spells.append(line)
                    elif line[1] == '2':
                        self.warlock_2spells.append(line)
                    elif line[1] == '3':
                        self.warlock_3spells.append(line)
                    elif line[1] == '4':
                        self.warlock_4spells.append(line)
                    elif line[1] == '5':
                        self.warlock_5spells.append(line)
                    elif line[1] == '6':
                        self.warlock_6spells.append(line)
                    elif line[1] == '7':
                        self.warlock_7spells.append(line)
                    elif line[1] == '8':
                        self.warlock_8spells.append(line)
                    elif line[1] == '9':
                        self.warlock_9spells.append(line)

                elif line[2] == 'wizard':
                    self.wizard_spells.append(line)
                    if line[1] == '0':
                        self.wizard_0spells.append(line)
                    elif line[1] == '1':
                        self.wizard_1spells.append(line)
                    elif line[1] == '2':
                        self.wizard_2spells.append(line)
                    elif line[1] == '3':
                        self.wizard_3spells.append(line)
                    elif line[1] == '4':
                        self.wizard_4spells.append(line)
                    elif line[1] == '5':
                        self.wizard_5spells.append(line)
                    elif line[1] == '6':
                        self.wizard_6spells.append(line)
                    elif line[1] == '7':
                        self.wizard_7spells.append(line)
                    elif line[1] == '8':
                        self.wizard_8spells.append(line)
                    elif line[1] == '9':
                        self.wizard_9spells.append(line)

        common_length = "\tCommon loot loaded: " + str(len(self.common_loot)) + "\n"
        uncommon_length = "\tUncommon loot loaded: " + str(len(self.uncommon_loot)) + "\n"
        rare_length = "\tRare loot loaded: " + str(len(self.rare_loot)) + "\n"
        very_rare_length = "\tVery Rare loot loaded: " + str(len(self.very_rare_loot)) + "\n"
        legendary_length = "\tLegendary loot loaded: " + str(len(self.legendary_loot)) + "\n"
        spell_length = "\tSpells loaded: " + str(len(self.all_spells)) + "\n"
        name_length = "\tNames loaded: " + str(len(self.name_list)) + "\n"
        potion_length = "\tPotions loaded: " + str(len(self.potion_loot)) + "\n"
        enchantments_length = "\tEnchantments loaded: " + str(len(self.enchantments)) + "\n"

        self.textEdit.append('Dungeon Engineer Toolkit v1.2.2\n\n')
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

    def sep(self):
        self.textEdit.append(50 * '-')

    def textClear(self):
        self.textEdit.clear()

    def outputFormat(self, text):
        self.spacer()
        self.textEdit.append(text)
        self.spacer()

    def enhancement_bonus(self):
        level = self.spinBox_Level.value()

        bonus_range = 0
        if level <= 5:
            bonus_range = 2
        elif level <= 9:
            bonus_range = 3
        elif level <= 13:
            bonus_range = 4
        elif level <= 17:
            bonus_range = 5
        elif level <= 20:
            bonus_range = 6

        return '+' + str(random.randrange(0, bonus_range)) + ' '

    def btn_Random_Loot_clicked(self):
        difficulty = str(self.comboBox_Difficulty.currentText())
        level = self.spinBox_Level.value()
        num = self.roll(100)

        common = 0
        uncommon = 0
        rare = 0
        very_rare = 0
        legendary = 0

        # Find number of items to be generated
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
        self.textEdit.append('End of loot bag :c')

    def btn_Common_clicked(self):
        common_item = random.choice(self.common_loot)
        text = 'Common item: ' + common_item[0] + '\nValue: ' + common_item[1]\
               + '\tWeight: ' + common_item[2] + '\nDescription: ' + common_item[3]
        self.outputFormat(text)

    def btn_Uncommon_clicked(self):
        uncommon_item = random.choice(self.uncommon_loot)
        text = 'Uncommon item: ' + uncommon_item[0] + '\nDescription: ' + uncommon_item[1]
        self.outputFormat(text)

    def btn_Rare_clicked(self):
        rare_item = random.choice(self.rare_loot)
        text = 'Rare item: ' + rare_item[0] + '\nDescription: ' + rare_item[1]
        self.outputFormat(text)

    def btn_Very_Rare_clicked(self):
        very_rare_item = random.choice(self.very_rare_loot)
        text = 'Very Rare item: ' + very_rare_item[0] + '\nDescription: ' + very_rare_item[1]
        self.outputFormat(text)

    def btn_Legendary_clicked(self):
        legendary_item = random.choice(self.legendary_loot)
        text = 'Legendary item: ' + legendary_item[0] + '\nDescription: ' + legendary_item[1]
        self.outputFormat(text)

    def btn_Potion_clicked(self):
        potion_item = random.choice(self.potion_loot)
        text = potion_item[0] + '\nDescription: ' + potion_item[1]
        self.outputFormat(text)

    def btn_Weapon_clicked(self):
        weapon = random.choice(self.weapons)
        text = self.enhancement_bonus() + weapon
        self.outputFormat(text)

    def btn_Armor_clicked(self):
        armor = random.choice(self.armors)
        text = self.enhancement_bonus() + armor
        self.outputFormat(text)

    def btn_Gold_clicked(self):
        def challenge0_4():
            num = self.roll(100)
            copper = 0
            silver = 0
            electrum = 0
            gold = 0
            platinum = 0
            if num <= 30:
                copper = str(self.roll(40)) + ' copper pieces'
            elif num <= 60:
                silver = str(self.roll(30)) + ' silver pieces'
            elif num <= 70:
                electrum = str(self.roll(20)) + ' electrum pieces'
            elif num <= 95:
                gold = str(self.roll(15)) + ' gold pieces'
            else:
                platinum = str(self.roll(8)) + ' platinum pieces'
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
                copper = str(self.roll(5000)) + ' copper pieces'
                electrum = str(self.roll(50)) + ' electrum pieces'
            elif num <= 60:
                silver = str(self.roll(400)) + ' silver pieces'
                gold = str(self.roll(150)) + ' gold pieces'
            elif num <= 70:
                electrum = str(self.roll(200)) + ' electrum pieces'
                gold = str(self.roll(150)) + ' gold pieces'
            elif num <= 95:
                gold = str(self.roll(300)) + ' gold pieces'
            else:
                gold = str(self.roll(150)) + ' gold pieces'
                platinum = str(self.roll(25)) + ' platinum pieces'
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
                silver = str(self.roll(2500)) + ' silver pieces'
                gold = str(self.roll(700)) + ' gold pieces'
            elif num <= 35:
                electrum = str(self.roll(700)) + ' electrum pieces'
                gold = str(self.roll(700)) + ' gold pieces'
            elif num <= 75:
                gold = str(self.roll(1000)) + ' gold pieces'
                platinum = str(self.roll(50)) + ' platinum pieces'
            else:
                gold = str(self.roll(1000)) + ' gold pieces'
                platinum = str(self.roll(100)) + ' platinum pieces'
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
                electrum = str(self.roll(10000)) + ' electrum pieces'
                gold = str(self.roll(5000)) + ' gold pieces'
            elif num <= 55:
                gold = str(self.roll(7000)) + ' gold pieces'
                platinum = str(self.roll(700)) + ' platinum pieces'
            else:
                gold = str(self.roll(8000)) + ' gold pieces'
                platinum = str(self.roll(1000)) + ' platinum pieces'
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
            self.outputFormat(challenge0_4())
        elif level <= 10:
            self.outputFormat(challenge5_10())
        elif level <= 16:
            self.outputFormat(challenge11_16())
        else:
            self.outputFormat(challenge17())

    def btn_Treasure_clicked(self):
        gemstone10 = [
            'azurite(10 gold)',
            'banded agate(10 gold)',
            'quartz(10 gold)',
            'eye agate(10 gold)',
            'hematite(10 gold)',
            'citrine(10 gold)',
            'malachite(10 gold)',
            'moss agate(10 gold)',
            'jasper(10 gold)',
            'rhodochrosite(10 gold)',
            'tiger eye(10 gold)',
            'turquoise(10 gold)'
        ]
        gemstone50 = [
            'bloodstone(50 gold)',
            'carnelian(50 gold)',
            'chalcedony(50 gold)',
            'chrysoprase(50 gold)',
            'obsidian(50 gold)',
            'pearl(50 gold)',
            'moonstone(50 gold)',
            'onyx(50 gold)',
            'blue quartz(50 gold)',
            'sardonyx(50 gold)',
            'star rose(50 gold)',
            'zircon(50 gold)'
        ]
        gemstone100 = [
            'amber(100 gold)',
            'amethyst(100 gold)',
            'chrysoberyl(100 gold)',
            'coral(100 gold)',
            'garnet(100 gold)',
            'jade(100 gold)',
            'jet(100 gold)',
            'emerald(100 gold)',
            'spinel(100 gold)',
            'tourmaline(100 gold)'
        ]
        gemstone500 = [
            'alexandrite(500 gold)',
            'aquamarine(500 gold)',
            'black pearl(500 gold)',
            'blue spinel(500 gold)',
            'peridot(500 gold)',
            'fire opal(500 gold)'
        ]
        gemstone1000 = [
            'black opal(1000 gold)',
            'blue sapphire(1000 gold)',
            'scarlet emerald(1000 gold)',
            'ruby(1000 gold)',
            'rainbow opal(1000 gold)',
            'star ruby(1000 gold)',
            'star sapphire(1000 gold)',
            'diamond(1000 gold)'
        ]
        gemstone5000 = [
            'blood sapphire(5000 gold)',
            'sun diamond(5000 gold)',
            'jacinth(5000 gold)',
            'tanzanite(5000 gold)'
        ]
        art25 = [
            'silver spoon(25 gold)',
            'carved bone figurine(25 gold)',
            'small gold bracelet(25 gold)',
            'gold laced vestments(25 gold)',
            'ancient stone mask(25 gold)',
            'bronze cup(25 gold)',
            'copper pipe with a silver tip(25 gold)',
            'small 6 by 8 oil painting(25 gold)',
            'velvet hat with plume(25 gold)',
            'gold locket with a saucy portrait inside(25 gold)'
        ]
        art250 = [
            'gold ring set with bloodstones(250 gold)',
            'onyx statuette(250 gold)',
            'large gold bracelet(250 gold)',
            'silver necklace with a jade pendant(250 gold)',
            'bronze crown with tiger eye gemstones(250 gold)',
            'silken lingerie(250 gold)',
            'large tapestry of a historic moment(250 gold)',
            'brass tankard with silver trim(250 gold)',
            'gem encrusted jewelry box(250 gold)',
            'dragon statuette made of obsidian(250 gold)'
        ]
        art750 = [
            'silver platter with amethyst edges(750 gold)',
            'silver-plated steel cutlass with black pearl set in hilt(750 gold)',
            'silver compass with fire opal hands(750 gold)',
            'small gold idol(750 gold)',
            'gold wand with red garnets caps(750 gold)',
            'golden ewer with a peridot rim(750 gold)',
            'ceremonial silver dagger with a bloodstone in the pommel(750 gold)',
            'silver and gold laced large shield(750 gold)',
            'iron staff with a blue spinel end piece(750 gold)',
            'angelic mask made of pearl(750 gold)'
        ]
        art2500 = [
            'golden lute with gemstone tuning pieces(2500 gold)',
            'old masterpiece painting(2500 gold)',
            'embroidered silk cape with platinum clasps(2500 gold)',
            'platinum dagger set with a ruby(2500 gold)',
            'embroidered bow tie(2500 gold)',
            'jeweled platinum ring(2500 gold)',
            'golden idol(2500 gold)',
            'golden holy symbol with gemstones(2500 gold)',
            'old ornate handkerchief(2500 gold)',
            'fire opal stringed necklace(2500 gold)'
        ]
        art7500 = [
            'jeweled gold crown(7500 gold)',
            'jeweled platinum anklet(7500 gold)',
            'golden animal figurine(7500 gold)',
            'gold chalice with emeralds(7500 gold)',
            'gold music box with platinum filigree(7500 gold)',
            'jeweled coffin painted gold(7500 gold)',
            'marble game board with solid sapphire and ruby playing pieces(7500 gold)',
            'jeweled ivory war horn(7500 gold)'
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
                self.textEdit.append('Portable hole' + '\n')

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
        text = 'Scroll: ' + random.choice(self.all_spells)[0]
        self.outputFormat(text)

    def btn_Lingering_Injuries_clicked(self):
        injury = self.roll(20)

        if injury == 1:
            text = ('Lose an Eye: You have disadvantage on Perception checks '
                    'that rely on sight and on ranged attack rolls. Magic such as '
                    'the regenerate spell can restore the lost eye. You are blinded '
                    'if both eyes are lost.\n')
        elif injury == 2:
            text = ('Lose an Arm or a Hand: Roll a 1d2 to decide if you lose'
                    'an arm or hand, 1 and 2 respectively. You can only hold one handed items'
                    ', and you can hold only a single object at a time. Magic '
                    'such as the regenerate spell can restore the lost appendage.\n')
        elif injury == 3:
            text = ('Lose a Foot or Leg: Roll a 1d2 to decide if you lose'
                    'an arm or hand, 1 and 2 respectively. Your speed on foot is halved, and you must '
                    'use some form of support. You fall prone after using the Dash action. You have '
                    'disadvantage on Dexterity checks made to balance. Magic such as the'
                    ' regenerate spell can restore the lost appendage.\n')
        elif injury == 4:
            text = ('Lose an Ear: You have disadvantage on Perception checks that rely'
                    ' on your hearing. Magic such as the regenerate spell can restore the lost'
                    ' ear. You are deafened if you lose both ears.\n')
        elif injury == 5:
            text = ('Lose Your Tongue: You are unable to speak in an intelligible manor and as such '
                    'can not cast any spells that have a verbal requirement. Magic such as the '
                    'regenerate spell can restore your tongue.\n')
        elif injury == 6:
            text = ('Limp: Your speed on foot is reduced by 1d3 times 5 feet. You must make a DC 10 '
                    'Dexterity saving throw after using the Dash action. If you fail the save, '
                    'you fall prone. Magical healing removes the limp.\n')
        elif injury <= 7:
            text = ('Deep Gash: Whenever you attempt an action in combat, you take'
                    ' 1d6 bleeding damage(no damage mitigation). You can not use any'
                    ' reactions until the gash is tended to. A DC 13 Medicine check or'
                    'magical healing cures the deep gash.\n')
        elif injury <= 10:
            text = ('Broken Bone: Whenever you attempt an action in combat, you must'
                    ' make a DC 10 Constitution saving throw. On a failed save, you '
                    'lose your action and can not use reactions until the start of your '
                    'next turn. The injury heals if you receive magical healing or if you '
                    'spend ten days doing nothing but resting.\n')
        elif injury <= 12:
            text = ('Disfiguring Scar: You are disfigured to the extent that the wound can'
                    ' not be easily concealed. You have disadvantage on Charisma (Persuasion)'
                    ' checks and advantage on Charisma (Intimidation) checks. Magical healing '
                    'of 6th level or higher, such as heal and regenerate, removes the scar.\n')
        elif injury <= 14:
            text = ('Infected Wound: Your hit point maximum is reduced by 1d10 every 12 hours '
                    'the wound persists. If your hit point maximum drops to 0, you die. The wound '
                    'heals if you receive magical healing three times. Alternatively, '
                    'someone can tend to the wound and make a DC 15 Medicine check once '
                    'every 24 hours. After ten successes, the wound heals.\n')
        elif injury <= 16:
            text = ('Head Injury: You lose the rest of your turn. On the start '
                    'of your next turn make a DC 10 '
                    'Constitution saving throw. On save, you are fine. On a '
                    'failed save you are dazed until the end of your next turn.\n')
        elif injury <= 18:
            text = ('Nerve Damage: You have disadvantage on Dexterity saving throws and checks. '
                    'You also lose your reaction. This effect ends when you take a short rest.\n')
        elif injury <= 20:
            text = ('Small Scar: The scar does not have any adverse effect. Magical '
                    'healing of 6th level or higher, such as heal and regenerate, removes the scar.\n')
        self.outputFormat(text)

    def btn_Madness_clicked(self):
        madness = str(self.comboBox_Madness.currentText())
        number = self.roll(100)
        madtime = self.roll(10)
        if madness == 'Short-term':
            self.textEdit.append('Short-term Madness(' + str(madtime) + ' mins): ')
            if number <= 20:
                self.textEdit.append('The character zones out and is considered paralyzed until they take damage.')
            elif number <= 30:
                self.textEdit.append('The character becomes incapacitated and spends the duration dancing because'
                                     ' they think if they stop the world will end.')
            elif number <= 40:
                self.textEdit.append('The character believes they are able to cast spells and prefer that '
                                     'over anything else. If they are a caster they think they cannot cast spells.')
            elif number <= 50:
                self.textEdit.append('The character begins babbling and is incapable of normal speech'
                                     ' or spellcasting.')
            elif number <= 60:
                self.textEdit.append('The character must use his or her action each round to attack the'
                                     ' nearest creature.')
            elif number <= 70:
                self.textEdit.append('The character is always hungry and thinks they are going to starve'
                                     ' if they cannot eat every hour.')
            elif number <= 75:
                self.textEdit.append('The character does whatever anyone tells him or her to do that is'
                                     ' not obviously self-destructive.')
            elif number <= 80:
                self.textEdit.append('The character experiences an overpowering urge to be in tight spaces.')
            elif number <= 90:
                self.textEdit.append('The character is dazed.')
            elif number <= 100:
                self.textEdit.append('The character falls unconscious.')
            self.textEdit.append('\n')
        elif madness == 'Long-term':
            madtime = self.roll(10) * 10
            self.textEdit.append('Long-term Madness(' + str(madtime) + ' hours): ')
            if number <= 10:
                self.textEdit.append('The character feels compelled to collect a specific type of item'
                                     ' and becomes violent if anyone talks about it.')
            elif number <= 20:
                self.textEdit.append('The character experiences vivid hallucinations and'
                                     'has nightmares causing them to need 10 hours of sleep.')
            elif number <= 30:
                self.textEdit.append('The character suffers extreme paranoia. The character'
                                     ' has disadvantage on Wisdom and Charisma checks.')
            elif number <= 40:
                self.textEdit.append('The character believes that they are never clean and is always '
                                     'scrubbing away at their skin or trying to find a place to bathe.')
            elif number <= 45:
                self.textEdit.append('The character experiences a powerful delusion. Believing that they are '
                                     'either missing a leg or an arm.')
            elif number <= 55:
                self.textEdit.append('The character becomes attached to whatever caused the madness '
                                     'and whenever they are more than 50 feet apart the character has '
                                     'disadvantage on all checks and saves.')
            elif number <= 65:
                self.textEdit.append('The character is blinded(25%), mute(25%), or deafened(50%).')
            elif number <= 75:
                self.textEdit.append('The character experiences uncontrollable tremors and shaking '
                                     'when in combat. When attacking they must make a DC 14 Constitution '
                                     'saving throw or drop their weapon or held items.')
            elif number <= 85:
                self.textEdit.append('The character suffers from partial amnesia. The character has'
                                     ' all of their memories, except they believe themselves to be of '
                                     'a difference race. They lose their active racial abilities but all '
                                     'passive abilities remain.')
            elif number <= 90:
                self.textEdit.append('The character loses the ability to read.')
            elif number <= 95:
                self.textEdit.append('The character loses the ability to speak.')
            elif number <= 100:
                self.textEdit.append('The character falls unconscious. No amount of jostling or damage can '
                                     'wake the character.')
            self.textEdit.append('\n')
        elif madness == 'Indefinite':
            self.textEdit.append('Indefinite madness(lasts until cured): ')
            if number <= 15:
                self.textEdit.append('The only thing that stops the voices is being drunk.')
            elif number <= 25:
                self.textEdit.append('I take whatever I want.')
            elif number <= 30:
                self.textEdit.append('I hate everyone and everything.')
            elif number <= 35:
                self.textEdit.append('I must always tell the truth, and cannot keep a secret when I need to.')
            elif number <= 45:
                self.textEdit.append('I get what I want with my good looks and suggestive remarks.')
            elif number <= 50:
                self.textEdit.append('I find it hard to focus on anything for more than 30 seconds.')
            elif number <= 55:
                self.textEdit.append('I do not like to wear clothing or armor as it is not natural.')
            elif number <= 70:
                self.textEdit.append('I am the smartest, wisest, strongest, fastest, and most '
                                     'beautiful person I know.')
            elif number <= 80:
                self.textEdit.append('I am convinced that everyone I travel with is trying to kill me.')
            elif number <= 85:
                self.textEdit.append('I can only talk to people of the same gender as myself.')
            elif number <= 95:
                self.textEdit.append('I can find everything dire and serious. Nothing is a joke or funny.')
            elif number <= 100:
                self.textEdit.append('I have discovered that I really hate killing anything.')
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

    def btn_Random_Names_clicked(self):
        names = ''
        self.spacer()
        for name in range(9):
            name = random.choice(self.name_list)[0]
            names += 'Name: ' + name + '\n'
        self.outputFormat(names)

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
            origin = "Unholy: Gives off a dark aura and saps the energy of any that touch it that are good aligned."
        elif num <= 4:
            origin = "Holy: Gives off a divine aura and burns any evil that touches the item."
        elif num == 5:
            origin = "Draconic: Warm and made with the scales or bones of dragons. " \
                     "Burns hotter when within 1 mile of a dragon."
        elif num == 6:
            origin = "Dwarven: Sturdy and unbreakable, just like a dwarf."
        elif num == 7:
            origin = "Elven: Weighs half what it normally would and is very elegant."
        elif num <= 10:
            origin = "Human: Made of common material and is of average make."
        elif num == 11:
            origin = "Gnomish: Doesn't look great but functions just as well as a new one."
        elif num == 12:
            origin = "Halfling: Made a size smaller for those of the shorter variety."
        elif num == 13:
            origin = "Orcish: Vicious and nasty spikes are the focus of the item."
        elif num == 14:
            origin = "Ancient: Very old and has a good chance of breaking."
        elif num <= 17:
            origin = "Noble: Jeweled and laced with silver, gold, or platinum."
        elif num == 18:
            origin = "Outlandish: Made out of bizarre materials and shapes but works."
        elif num == 19:
            origin = "Mythical: The item is tied to some story or prophecy."
        elif num == 20:
            origin = "Arcane: The item has some minor magical property linked to its creation."
        self.outputFormat(origin)

    def btn_Enchantment_clicked(self):
        enchant = random.choice(self.enchantments)
        text = 'Enchant: ' + enchant[0] + '\nDescription: ' + enchant[1]
        self.outputFormat(text)

    def btn_Quest_Generator_clicked(self):
        choice = random.choice(self.quests)
        text = 'Quest: ' + choice
        self.outputFormat(text)

    def btn_Plot_Hook_clicked(self):
        choice = random.choice(self.plothook)
        text = 'Plot Hook: ' + choice
        self.outputFormat(text)

    def btn_Downtime_clicked(self):
        # Generate downtime based on activity
        activity = str(self.comboBox_Downtime.currentText())

        # Activity: Training, Sell Magic Item, Carousing
        if activity == 'Training':
            self.textEdit.append('Training:')
            self.textEdit.append('2-4\t10 days\t20gp')
            self.textEdit.append('5-10\t20 days\t40gp')
            self.textEdit.append('11-16\t30 days\t60gp')
            self.textEdit.append('17-20\t40 days\t80gp')
            return
        elif activity == 'Sell Magic Item':
            self.textEdit.append('Magic Item Price:')
            self.textEdit.append('Common: 100gp Days: 1d4')
            self.textEdit.append('Uncommon: 500gp Days: 1d6')
            self.textEdit.append('Rare: 5000gp Days: 1d8')
            self.textEdit.append('Very Rare: 50,000 Days: 1d10')

            inflation = self.roll(100)
            if inflation <= 20:
                self.textEdit.append('You find a buyer offering a quarter of the base price.')
            elif inflation <= 40:
                self.textEdit.append('You find a buyer offering half of the base price.')
            elif inflation <= 60:
                self.textEdit.append('You find a buyer offering full base price.')
            elif inflation <= 80:
                self.textEdit.append('You find a shady buyer offering one and a half times the base price.')
            return
        elif activity == 'Carousing':
            encounter = random.choice(self.carousing)
            self.textEdit.append('Carousing: ' + encounter)
            return

    def btn_Riddle_clicked(self):
        riddle = random.choice(self.riddle)
        text = 'Riddle: ' + riddle
        self.outputFormat(text)

    def btn_Puzzle_clicked(self):
        puzzle = random.choice(self.puzzle)
        text = 'Puzzle: ' + puzzle
        self.outputFormat(text)

    def btn_Spellbook_clicked(self):
        # Get currently selected class
        caster_class = str(self.comboBox_Spellbook.currentText())
        level = self.spinBox_Level.value()

        spellbook = ''
        spells = []
        cantrip_spells = self.bard_0spells

        if caster_class == 'bard':
            spellbook += 'Bard Spellbook:\n'
            if level == 1:
                possible_spells = [self.bard_1spells]
                cantrips = 2
                spells_known = 4
            elif level == 2:
                possible_spells = [self.bard_1spells]
                cantrips = 2
                spells_known = 5
            elif level == 3:
                possible_spells = [self.bard_1spells]
                cantrips = 2
                spells_known = 6
            elif level == 4:
                possible_spells = [self.bard_1spells, self.bard_2spells]
                cantrips = 3
                spells_known = 7
            elif level == 5:
                possible_spells = [self.bard_1spells, self.bard_2spells, self.bard_3spells]
                cantrips = 3
                spells_known = 8
            elif level == 6:
                possible_spells = [self.bard_1spells, self.bard_2spells, self.bard_3spells]
                cantrips = 3
                spells_known = 9

            elif level == 7:
                possible_spells = [self.bard_1spells, self.bard_2spells, self.bard_3spells, self.bard_4spells]
                cantrips = 3
                spells_known = 10
            elif level == 8:
                possible_spells = [self.bard_1spells, self.bard_2spells, self.bard_3spells, self.bard_4spells]
                cantrips = 3
                spells_known = 11
            elif level == 9:
                possible_spells = [self.bard_1spells, self.bard_2spells, self.bard_3spells, self.bard_4spells,
                                   self.bard_5spells]
                cantrips = 3
                spells_known = 12
            elif level == 10:
                possible_spells = [self.bard_1spells, self.bard_2spells, self.bard_3spells, self.bard_4spells,
                                   self.bard_5spells]
                cantrips = 4
                spells_known = 14
            elif level == 11:
                possible_spells = [self.bard_1spells, self.bard_2spells, self.bard_3spells, self.bard_4spells,
                                   self.bard_5spells, self.bard_6spells]
                cantrips = 4
                spells_known = 15
            elif level == 12:
                possible_spells = [self.bard_1spells, self.bard_2spells, self.bard_3spells, self.bard_4spells,
                                   self.bard_5spells, self.bard_6spells]
                cantrips = 4
                spells_known = 15
            elif level == 13:
                possible_spells = [self.bard_1spells, self.bard_2spells, self.bard_3spells, self.bard_4spells,
                                   self.bard_5spells, self.bard_6spells, self.bard_7spells]
                cantrips = 4
                spells_known = 16
            elif level == 14:
                possible_spells = [self.bard_1spells, self.bard_2spells, self.bard_3spells, self.bard_4spells,
                                   self.bard_5spells, self.bard_6spells, self.bard_7spells]
                cantrips = 4
                spells_known = 18
            elif level == 15:
                possible_spells = [self.bard_1spells, self.bard_2spells, self.bard_3spells, self.bard_4spells,
                                   self.bard_5spells, self.bard_6spells, self.bard_7spells, self.bard_8spells]
                cantrips = 4
                spells_known = 19
            elif level == 16:
                possible_spells = [self.bard_1spells, self.bard_2spells, self.bard_3spells, self.bard_4spells,
                                   self.bard_5spells, self.bard_6spells, self.bard_7spells, self.bard_8spells]
                cantrips = 4
                spells_known = 19
            elif level == 17:
                possible_spells = [self.bard_1spells, self.bard_2spells, self.bard_3spells, self.bard_4spells,
                                   self.bard_5spells, self.bard_6spells, self.bard_7spells, self.bard_8spells,
                                   self.bard_9spells]
                cantrips = 4
                spells_known = 20
            elif level == 18:
                possible_spells = [self.bard_1spells, self.bard_2spells, self.bard_3spells, self.bard_4spells,
                                   self.bard_5spells, self.bard_6spells, self.bard_7spells, self.bard_8spells,
                                   self.bard_9spells]
                cantrips = 4
                spells_known = 22
            elif level == 19:
                possible_spells = [self.bard_1spells, self.bard_2spells, self.bard_3spells, self.bard_4spells,
                                   self.bard_5spells, self.bard_6spells, self.bard_7spells, self.bard_8spells,
                                   self.bard_9spells]
                cantrips = 4
                spells_known = 22
            elif level == 20:
                possible_spells = [self.bard_1spells, self.bard_2spells, self.bard_3spells, self.bard_4spells,
                                   self.bard_5spells, self.bard_6spells, self.bard_7spells, self.bard_8spells,
                                   self.bard_9spells]
                cantrips = 4
                spells_known = 22

        elif caster_class == 'cleric':
            spellbook += 'Cleric Spellbook:\n'
            wis_mod = 0  # TODO change this to a prompt for wisdom modifier
            cantrip_spells = self.cleric_0spells
            if level == 1:
                possible_spells = [self.cleric_1spells]
                cantrips = 3
                spells_known = level + wis_mod
            elif level == 2:
                possible_spells = [self.cleric_1spells]
                cantrips = 3
                spells_known = level + wis_mod
            elif level == 3:
                possible_spells = [self.cleric_1spells, self.cleric_2spells]
                cantrips = 3
                spells_known = level + wis_mod
            elif level == 4:
                possible_spells = [self.cleric_1spells, self.cleric_2spells]
                cantrips = 4
                spells_known = level + wis_mod
            elif level == 5:
                possible_spells = [self.cleric_1spells, self.cleric_2spells, self.cleric_3spells]
                cantrips = 4
                spells_known = level + wis_mod
            elif level == 6:
                possible_spells = [self.cleric_1spells, self.cleric_2spells, self.cleric_3spells]
                cantrips = 4
                spells_known = level + wis_mod
            elif level == 7:
                possible_spells = [self.cleric_1spells, self.cleric_2spells, self.cleric_3spells, self.cleric_4spells]
                cantrips = 4
                spells_known = level + wis_mod
            elif level == 8:
                possible_spells = [self.cleric_1spells, self.cleric_2spells, self.cleric_3spells, self.cleric_4spells]
                cantrips = 4
                spells_known = level + wis_mod
            elif level == 9:
                possible_spells = [self.cleric_1spells, self.cleric_2spells, self.cleric_3spells, self.cleric_4spells,
                                   self.cleric_5spells]
                cantrips = 4
                spells_known = level + wis_mod
            elif level == 10:
                possible_spells = [self.cleric_1spells, self.cleric_2spells, self.cleric_3spells, self.cleric_4spells,
                                   self.cleric_5spells]
                cantrips = 5
                spells_known = level + wis_mod
            elif level == 11:
                possible_spells = [self.cleric_1spells, self.cleric_2spells, self.cleric_3spells, self.cleric_4spells,
                                   self.cleric_5spells, self.cleric_6spells]
                cantrips = 5
                spells_known = level + wis_mod
            elif level == 12:
                possible_spells = [self.cleric_1spells, self.cleric_2spells, self.cleric_3spells, self.cleric_4spells,
                                   self.cleric_5spells, self.cleric_6spells]
                cantrips = 5
                spells_known = level + wis_mod
            elif level == 13:
                possible_spells = [self.cleric_1spells, self.cleric_2spells, self.cleric_3spells, self.cleric_4spells,
                                   self.cleric_5spells, self.cleric_6spells, self.cleric_7spells]
                cantrips = 5
                spells_known = level + wis_mod
            elif level == 14:
                possible_spells = [self.cleric_1spells, self.cleric_2spells, self.cleric_3spells, self.cleric_4spells,
                                   self.cleric_5spells, self.cleric_6spells, self.cleric_7spells]
                cantrips = 5
                spells_known = level + wis_mod
            elif level == 15:
                possible_spells = [self.cleric_1spells, self.cleric_2spells, self.cleric_3spells, self.cleric_4spells,
                                   self.cleric_5spells, self.cleric_6spells, self.cleric_7spells, self.cleric_8spells]
                cantrips = 5
                spells_known = level + wis_mod
            elif level == 16:
                possible_spells = [self.cleric_1spells, self.cleric_2spells, self.cleric_3spells, self.cleric_4spells,
                                   self.cleric_5spells, self.cleric_6spells, self.cleric_7spells, self.cleric_8spells]
                cantrips = 5
                spells_known = level + wis_mod
            elif level == 17:
                possible_spells = [self.cleric_1spells, self.cleric_2spells, self.cleric_3spells, self.cleric_4spells,
                                   self.cleric_5spells, self.cleric_6spells, self.cleric_7spells, self.cleric_8spells,
                                   self.cleric_9spells]
                cantrips = 5
                spells_known = level + wis_mod
            elif level == 18:
                possible_spells = [self.cleric_1spells, self.cleric_2spells, self.cleric_3spells, self.cleric_4spells,
                                   self.cleric_5spells, self.cleric_6spells, self.cleric_7spells, self.cleric_8spells,
                                   self.cleric_9spells]
                cantrips = 5
                spells_known = level + wis_mod
            elif level == 19:
                possible_spells = [self.cleric_1spells, self.cleric_2spells, self.cleric_3spells, self.cleric_4spells,
                                   self.cleric_5spells, self.cleric_6spells, self.cleric_7spells, self.cleric_8spells,
                                   self.cleric_9spells]
                cantrips = 5
                spells_known = level + wis_mod
            elif level == 20:
                possible_spells = [self.cleric_1spells, self.cleric_2spells, self.cleric_3spells, self.cleric_4spells,
                                   self.cleric_5spells, self.cleric_6spells, self.cleric_7spells, self.cleric_8spells,
                                   self.cleric_9spells]
                cantrips = 5
                spells_known = level + wis_mod

        elif caster_class == 'druid':
            spellbook += 'Druid Spellbook:\n'
            wis_mod = 0  # TODO change this to a prompt for wisdom modifier
            cantrip_spells = self.druid_0spells
            if level == 1:
                possible_spells = [self.druid_1spells]
                cantrips = 2
                spells_known = level + wis_mod
            elif level == 2:
                possible_spells = [self.druid_1spells]
                cantrips = 2
                spells_known = level + wis_mod
            elif level == 3:
                possible_spells = [self.druid_1spells, self.druid_2spells]
                cantrips = 2
                spells_known = level + wis_mod
            elif level == 4:
                possible_spells = [self.druid_1spells, self.druid_2spells]
                cantrips = 3
                spells_known = level + wis_mod
            elif level == 5:
                possible_spells = [self.druid_1spells, self.druid_2spells, self.druid_3spells]
                cantrips = 3
                spells_known = level + wis_mod
            elif level == 6:
                possible_spells = [self.druid_1spells, self.druid_2spells, self.druid_3spells]
                cantrips = 3
                spells_known = level + wis_mod
            elif level == 7:
                possible_spells = [self.druid_1spells, self.druid_2spells, self.druid_3spells, self.druid_4spells]
                cantrips = 3
                spells_known = level + wis_mod
            elif level == 8:
                possible_spells = [self.druid_1spells, self.druid_2spells, self.druid_3spells, self.druid_4spells]
                cantrips = 3
                spells_known = level + wis_mod
            elif level == 9:
                possible_spells = [self.druid_1spells, self.druid_2spells, self.druid_3spells, self.druid_4spells,
                                   self.druid_5spells]
                cantrips = 3
                spells_known = level + wis_mod
            elif level == 10:
                possible_spells = [self.druid_1spells, self.druid_2spells, self.druid_3spells, self.druid_4spells,
                                   self.druid_5spells]
                cantrips = 4
                spells_known = level + wis_mod
            elif level == 11:
                possible_spells = [self.druid_1spells, self.druid_2spells, self.druid_3spells, self.druid_4spells,
                                   self.druid_5spells, self.druid_6spells]
                cantrips = 4
                spells_known = level + wis_mod
            elif level == 12:
                possible_spells = [self.druid_1spells, self.druid_2spells, self.druid_3spells, self.druid_4spells,
                                   self.druid_5spells, self.druid_6spells]
                cantrips = 4
                spells_known = level + wis_mod
            elif level == 13:
                possible_spells = [self.druid_1spells, self.druid_2spells, self.druid_3spells, self.druid_4spells,
                                   self.druid_5spells, self.druid_6spells, self.druid_7spells]
                cantrips = 4
                spells_known = level + wis_mod
            elif level == 14:
                possible_spells = [self.druid_1spells, self.druid_2spells, self.druid_3spells, self.druid_4spells,
                                   self.druid_5spells, self.druid_6spells, self.druid_7spells]
                cantrips = 4
                spells_known = level + wis_mod
            elif level == 15:
                possible_spells = [self.druid_1spells, self.druid_2spells, self.druid_3spells, self.druid_4spells,
                                   self.druid_5spells, self.druid_6spells, self.druid_7spells, self.druid_8spells]
                cantrips = 4
                spells_known = level + wis_mod
            elif level == 16:
                possible_spells = [self.druid_1spells, self.druid_2spells, self.druid_3spells, self.druid_4spells,
                                   self.druid_5spells, self.druid_6spells, self.druid_7spells, self.druid_8spells]
                cantrips = 4
                spells_known = level + wis_mod
            elif level == 17:
                possible_spells = [self.druid_1spells, self.druid_2spells, self.druid_3spells, self.druid_4spells,
                                   self.druid_5spells, self.druid_6spells, self.druid_7spells, self.druid_8spells,
                                   self.druid_9spells]
                cantrips = 4
                spells_known = level + wis_mod
            elif level == 18:
                possible_spells = [self.druid_1spells, self.druid_2spells, self.druid_3spells, self.druid_4spells,
                                   self.druid_5spells, self.druid_6spells, self.druid_7spells, self.druid_8spells,
                                   self.druid_9spells]
                cantrips = 4
                spells_known = level + wis_mod
            elif level == 19:
                possible_spells = [self.druid_1spells, self.druid_2spells, self.druid_3spells, self.druid_4spells,
                                   self.druid_5spells, self.druid_6spells, self.druid_7spells, self.druid_8spells,
                                   self.druid_9spells]
                cantrips = 4
                spells_known = level + wis_mod
            elif level == 20:
                possible_spells = [self.druid_1spells, self.druid_2spells, self.druid_3spells, self.druid_4spells,
                                   self.druid_5spells, self.druid_6spells, self.druid_7spells, self.druid_8spells,
                                   self.druid_9spells]
                cantrips = 4
                spells_known = level + wis_mod

        elif caster_class == 'paladin':
            spellbook += 'Paladin Spellbook:\n'
            cantrip_spells = False
            cha_mod = 0  # TODO change this to prompt for charisma modifier
            if level == 1:
                possible_spells = []
                spells_known = 0
            elif level == 2:
                possible_spells = [self.paladin_1spells]
                spells_known = (level // 2) + cha_mod
            elif level == 3:
                possible_spells = [self.paladin_1spells]
                spells_known = (level // 2) + cha_mod
            elif level == 4:
                possible_spells = [self.paladin_1spells]
                spells_known = (level // 2) + cha_mod
            elif level == 5:
                possible_spells = [self.paladin_1spells, self.paladin_2spells]
                spells_known = (level // 2) + cha_mod
            elif level == 6:
                possible_spells = [self.paladin_1spells, self.paladin_2spells]
                spells_known = (level // 2) + cha_mod
            elif level == 7:
                possible_spells = [self.paladin_1spells, self.paladin_2spells]
                spells_known = (level // 2) + cha_mod
            elif level == 8:
                possible_spells = [self.paladin_1spells, self.paladin_2spells]
                spells_known = (level // 2) + cha_mod
            elif level == 9:
                possible_spells = [self.paladin_1spells, self.paladin_2spells, self.paladin_3spells]
                spells_known = (level // 2) + cha_mod
            elif level == 10:
                possible_spells = [self.paladin_1spells, self.paladin_2spells, self.paladin_3spells]
                spells_known = (level // 2) + cha_mod
            elif level == 11:
                possible_spells = [self.paladin_1spells, self.paladin_2spells, self.paladin_3spells]
                spells_known = (level // 2) + cha_mod
            elif level == 12:
                possible_spells = [self.paladin_1spells, self.paladin_2spells, self.paladin_3spells]
                spells_known = (level // 2) + cha_mod
            elif level == 13:
                possible_spells = [self.paladin_1spells, self.paladin_2spells, self.paladin_3spells,
                                   self.paladin_4spells]
                spells_known = (level // 2) + cha_mod
            elif level == 14:
                possible_spells = [self.paladin_1spells, self.paladin_2spells, self.paladin_3spells,
                                   self.paladin_4spells]
                spells_known = (level // 2) + cha_mod
            elif level == 15:
                possible_spells = [self.paladin_1spells, self.paladin_2spells, self.paladin_3spells,
                                   self.paladin_4spells]
                spells_known = (level // 2) + cha_mod
            elif level == 16:
                possible_spells = [self.paladin_1spells, self.paladin_2spells, self.paladin_3spells,
                                   self.paladin_4spells]
                spells_known = (level // 2) + cha_mod
            elif level == 17:
                possible_spells = [self.paladin_1spells, self.paladin_2spells, self.paladin_3spells,
                                   self.paladin_4spells, self.paladin_5spells]
                spells_known = (level // 2) + cha_mod
            elif level == 18:
                possible_spells = [self.paladin_1spells, self.paladin_2spells, self.paladin_3spells,
                                   self.paladin_4spells, self.paladin_5spells]
                spells_known = (level // 2) + cha_mod
            elif level == 19:
                possible_spells = [self.paladin_1spells, self.paladin_2spells, self.paladin_3spells,
                                   self.paladin_4spells, self.paladin_5spells]
                spells_known = (level // 2) + cha_mod
            elif level == 20:
                possible_spells = [self.paladin_1spells, self.paladin_2spells, self.paladin_3spells,
                                   self.paladin_4spells, self.paladin_5spells]
                spells_known = (level // 2) + cha_mod

        elif caster_class == 'ranger':
            spellbook += 'Ranger Spellbook:\n'
            cantrip_spells = False

            if level == 1:
                possible_spells = []
                spells_known = 0
            elif level == 2:
                possible_spells = [self.ranger_1spells]
                spells_known = 2
            elif level == 3:
                possible_spells = [self.ranger_1spells]
                spells_known = 3
            elif level == 4:
                possible_spells = [self.ranger_1spells]
                spells_known = 3
            elif level == 5:
                possible_spells = [self.ranger_1spells, self.ranger_2spells]
                spells_known = 4
            elif level == 6:
                possible_spells = [self.ranger_1spells, self.ranger_2spells]
                spells_known = 4
            elif level == 7:
                possible_spells = [self.ranger_1spells, self.ranger_2spells]
                spells_known = 5
            elif level == 8:
                possible_spells = [self.ranger_1spells, self.ranger_2spells]
                spells_known = 5
            elif level == 9:
                possible_spells = [self.ranger_1spells, self.ranger_2spells, self.ranger_3spells]
                spells_known = 6
            elif level == 10:
                possible_spells = [self.ranger_1spells, self.ranger_2spells, self.ranger_3spells]
                spells_known = 6
            elif level == 11:
                possible_spells = [self.ranger_1spells, self.ranger_2spells, self.ranger_3spells]
                spells_known = 7
            elif level == 12:
                possible_spells = [self.ranger_1spells, self.ranger_2spells, self.ranger_3spells]
                spells_known = 7
            elif level == 13:
                possible_spells = [self.ranger_1spells, self.ranger_2spells, self.ranger_3spells,
                                   self.ranger_4spells]
                spells_known = 8
            elif level == 14:
                possible_spells = [self.ranger_1spells, self.ranger_2spells, self.ranger_3spells,
                                   self.ranger_4spells]
                spells_known = 8
            elif level == 15:
                possible_spells = [self.ranger_1spells, self.ranger_2spells, self.ranger_3spells,
                                   self.ranger_4spells]
                spells_known = 9
            elif level == 16:
                possible_spells = [self.ranger_1spells, self.ranger_2spells, self.ranger_3spells,
                                   self.ranger_4spells]
                spells_known = 9
            elif level == 17:
                possible_spells = [self.ranger_1spells, self.ranger_2spells, self.ranger_3spells,
                                   self.ranger_4spells, self.ranger_5spells]
                spells_known = 10
            elif level == 18:
                possible_spells = [self.ranger_1spells, self.ranger_2spells, self.ranger_3spells,
                                   self.ranger_4spells, self.ranger_5spells]
                spells_known = 10
            elif level == 19:
                possible_spells = [self.ranger_1spells, self.ranger_2spells, self.ranger_3spells,
                                   self.ranger_4spells, self.ranger_5spells]
                spells_known = 11
            elif level == 20:
                possible_spells = [self.ranger_1spells, self.ranger_2spells, self.ranger_3spells,
                                   self.ranger_4spells, self.ranger_5spells]
                spells_known = 11

        elif caster_class == 'sorcerer':
            spellbook += 'Sorcerer Spellbook:\n'
            cantrip_spells = self.sorcerer_0spells
            if level == 1:
                possible_spells = [self.sorcerer_1spells]
                cantrips = 4
                spells_known = 2
            elif level == 2:
                possible_spells = [self.sorcerer_1spells]
                cantrips = 4
                spells_known = 3
            elif level == 3:
                possible_spells = [self.sorcerer_1spells, self.sorcerer_2spells]
                cantrips = 4
                spells_known = 4
            elif level == 4:
                possible_spells = [self.sorcerer_1spells, self.sorcerer_2spells]
                cantrips = 5
                spells_known = 5
            elif level == 5:
                possible_spells = [self.sorcerer_1spells, self.sorcerer_2spells, self.sorcerer_3spells]
                cantrips = 5
                spells_known = 6
            elif level == 6:
                possible_spells = [self.sorcerer_1spells, self.sorcerer_2spells, self.sorcerer_3spells]
                cantrips = 5
                spells_known = 7
            elif level == 7:
                possible_spells = [self.sorcerer_1spells, self.sorcerer_2spells, self.sorcerer_3spells,
                                   self.sorcerer_4spells]
                cantrips = 5
                spells_known = 8
            elif level == 8:
                possible_spells = [self.sorcerer_1spells, self.sorcerer_2spells, self.sorcerer_3spells,
                                   self.sorcerer_4spells]
                cantrips = 5
                spells_known = 9
            elif level == 9:
                possible_spells = [self.sorcerer_1spells, self.sorcerer_2spells, self.sorcerer_3spells,
                                   self.sorcerer_4spells, self.sorcerer_5spells]
                cantrips = 5
                spells_known = 10
            elif level == 10:
                possible_spells = [self.sorcerer_1spells, self.sorcerer_2spells, self.sorcerer_3spells,
                                   self.sorcerer_4spells, self.sorcerer_5spells]
                cantrips = 6
                spells_known = 11
            elif level == 11:
                possible_spells = [self.sorcerer_1spells, self.sorcerer_2spells, self.sorcerer_3spells,
                                   self.sorcerer_4spells, self.sorcerer_5spells, self.sorcerer_6spells]
                cantrips = 6
                spells_known = 12
            elif level == 12:
                possible_spells = [self.sorcerer_1spells, self.sorcerer_2spells, self.sorcerer_3spells,
                                   self.sorcerer_4spells, self.sorcerer_5spells, self.sorcerer_6spells]
                cantrips = 6
                spells_known = 12
            elif level == 13:
                possible_spells = [self.sorcerer_1spells, self.sorcerer_2spells, self.sorcerer_3spells,
                                   self.sorcerer_4spells, self.sorcerer_5spells, self.sorcerer_6spells,
                                   self.sorcerer_7spells]
                cantrips = 6
                spells_known = 13
            elif level == 14:
                possible_spells = [self.sorcerer_1spells, self.sorcerer_2spells, self.sorcerer_3spells,
                                   self.sorcerer_4spells, self.sorcerer_5spells, self.sorcerer_6spells,
                                   self.sorcerer_7spells]
                cantrips = 6
                spells_known = 13
            elif level == 15:
                possible_spells = [self.sorcerer_1spells, self.sorcerer_2spells, self.sorcerer_3spells,
                                   self.sorcerer_4spells, self.sorcerer_5spells, self.sorcerer_6spells,
                                   self.sorcerer_7spells, self.sorcerer_8spells]
                cantrips = 6
                spells_known = 14
            elif level == 16:
                possible_spells = [self.sorcerer_1spells, self.sorcerer_2spells, self.sorcerer_3spells,
                                   self.sorcerer_4spells, self.sorcerer_5spells, self.sorcerer_6spells,
                                   self.sorcerer_7spells, self.sorcerer_8spells]
                cantrips = 6
                spells_known = 14
            elif level == 17:
                possible_spells = [self.sorcerer_1spells, self.sorcerer_2spells, self.sorcerer_3spells,
                                   self.sorcerer_4spells, self.sorcerer_5spells, self.sorcerer_6spells,
                                   self.sorcerer_7spells, self.sorcerer_8spells, self.sorcerer_9spells]
                cantrips = 6
                spells_known = 15
            elif level == 18:
                possible_spells = [self.sorcerer_1spells, self.sorcerer_2spells, self.sorcerer_3spells,
                                   self.sorcerer_4spells, self.sorcerer_5spells, self.sorcerer_6spells,
                                   self.sorcerer_7spells, self.sorcerer_8spells, self.sorcerer_9spells]
                cantrips = 6
                spells_known = 15
            elif level == 19:
                possible_spells = [self.sorcerer_1spells, self.sorcerer_2spells, self.sorcerer_3spells,
                                   self.sorcerer_4spells, self.sorcerer_5spells, self.sorcerer_6spells,
                                   self.sorcerer_7spells, self.sorcerer_8spells, self.sorcerer_9spells]
                cantrips = 6
                spells_known = 15
            elif level == 20:
                possible_spells = [self.sorcerer_1spells, self.sorcerer_2spells, self.sorcerer_3spells,
                                   self.sorcerer_4spells, self.sorcerer_5spells, self.sorcerer_6spells,
                                   self.sorcerer_7spells, self.sorcerer_8spells, self.sorcerer_9spells]
                cantrips = 6
                spells_known = 15

        elif caster_class == 'warlock':
            spellbook += 'Warlock Spellbook:\n'
            cantrip_spells = self.warlock_0spells
            if level == 1:
                possible_spells =  [self.warlock_1spells]
                cantrips = 2
                spells_known = 2
            elif level == 2:
                possible_spells = [self.warlock_1spells]
                cantrips = 2
                spells_known = 3
            elif level == 3:
                possible_spells = [self.warlock_1spells, self.warlock_2spells]
                cantrips = 2
                spells_known = 4
            elif level == 4:
                possible_spells = [self.warlock_1spells, self.warlock_2spells]
                cantrips = 3
                spells_known = 5
            elif level == 5:
                possible_spells = [self.warlock_1spells, self.warlock_2spells, self.warlock_3spells]
                cantrips = 3
                spells_known = 6
            elif level == 6:
                possible_spells = [self.warlock_1spells, self.warlock_2spells, self.warlock_3spells]
                cantrips = 3
                spells_known = 7
            elif level == 7:
                possible_spells = [self.warlock_1spells, self.warlock_2spells, self.warlock_3spells,
                                   self.warlock_4spells]
                cantrips = 3
                spells_known = 8
            elif level == 8:
                possible_spells = [self.warlock_1spells, self.warlock_2spells, self.warlock_3spells,
                                   self.warlock_4spells]
                cantrips = 3
                spells_known = 9
            elif level == 9:
                possible_spells = [self.warlock_1spells, self.warlock_2spells, self.warlock_3spells,
                                   self.warlock_4spells, self.warlock_5spells]
                cantrips = 3
                spells_known = 10
            elif level == 10:
                possible_spells = [self.warlock_1spells, self.warlock_2spells, self.warlock_3spells,
                                   self.warlock_4spells, self.warlock_5spells]
                cantrips = 4
                spells_known = 10
            elif level == 11:
                possible_spells = [self.warlock_1spells, self.warlock_2spells, self.warlock_3spells,
                                   self.warlock_4spells, self.warlock_5spells]
                cantrips = 4
                spells_known = 11
                spells.append(random.choice(self.warlock_6spells))
            elif level == 12:
                possible_spells = [self.warlock_1spells, self.warlock_2spells, self.warlock_3spells,
                                   self.warlock_4spells, self.warlock_5spells]
                cantrips = 4
                spells_known = 11
                spells.append(random.choice(self.warlock_6spells))
            elif level == 13:
                possible_spells = [self.warlock_1spells, self.warlock_2spells, self.warlock_3spells,
                                   self.warlock_4spells, self.warlock_5spells]
                cantrips = 4
                spells_known = 12
                spells.append(random.choice(self.warlock_6spells))
                spells.append(random.choice(self.warlock_7spells))
            elif level == 14:
                possible_spells = [self.warlock_1spells, self.warlock_2spells, self.warlock_3spells,
                                   self.warlock_4spells, self.warlock_5spells]
                cantrips = 4
                spells_known = 12
                spells.append(random.choice(self.warlock_6spells))
                spells.append(random.choice(self.warlock_7spells))
            elif level == 15:
                possible_spells = [self.warlock_1spells, self.warlock_2spells, self.warlock_3spells,
                                   self.warlock_4spells, self.warlock_5spells]
                cantrips = 4
                spells_known = 13
                spells.append(random.choice(self.warlock_6spells))
                spells.append(random.choice(self.warlock_7spells))
                spells.append(random.choice(self.warlock_8spells))
            elif level == 16:
                possible_spells = [self.warlock_1spells, self.warlock_2spells, self.warlock_3spells,
                                   self.warlock_4spells, self.warlock_5spells]
                cantrips = 4
                spells_known = 13
                spells.append(random.choice(self.warlock_6spells))
                spells.append(random.choice(self.warlock_7spells))
                spells.append(random.choice(self.warlock_8spells))
            elif level == 17:
                possible_spells = [self.warlock_1spells, self.warlock_2spells, self.warlock_3spells,
                                   self.warlock_4spells, self.warlock_5spells]
                cantrips = 4
                spells_known = 14
                spells.append(random.choice(self.warlock_6spells))
                spells.append(random.choice(self.warlock_7spells))
                spells.append(random.choice(self.warlock_8spells))
                spells.append(random.choice(self.warlock_9spells))
            elif level == 18:
                possible_spells = [self.warlock_1spells, self.warlock_2spells, self.warlock_3spells,
                                   self.warlock_4spells, self.warlock_5spells]
                cantrips = 4
                spells_known = 14
                spells.append(random.choice(self.warlock_6spells))
                spells.append(random.choice(self.warlock_7spells))
                spells.append(random.choice(self.warlock_8spells))
                spells.append(random.choice(self.warlock_9spells))
            elif level == 19:
                possible_spells = [self.warlock_1spells, self.warlock_2spells, self.warlock_3spells,
                                   self.warlock_4spells, self.warlock_5spells]
                cantrips = 4
                spells_known = 15
                spells.append(random.choice(self.warlock_6spells))
                spells.append(random.choice(self.warlock_7spells))
                spells.append(random.choice(self.warlock_8spells))
                spells.append(random.choice(self.warlock_9spells))
            elif level == 20:
                possible_spells = [self.warlock_1spells, self.warlock_2spells, self.warlock_3spells,
                                   self.warlock_4spells, self.warlock_5spells]
                cantrips = 4
                spells_known = 15
                spells.append(random.choice(self.warlock_6spells))
                spells.append(random.choice(self.warlock_7spells))
                spells.append(random.choice(self.warlock_8spells))
                spells.append(random.choice(self.warlock_9spells))

        elif caster_class == 'wizard':
            spellbook += 'Wizard Spellbook:\n'
            cantrip_spells = self.wizard_0spells
            if level == 1:
                possible_spells = [self.wizard_1spells]
                cantrips = 3
                spells_known = level * 2
            elif level == 2:
                possible_spells = [self.wizard_1spells]
                cantrips = 3
                spells_known = level * 2
            elif level == 3:
                possible_spells = [self.wizard_1spells, self.wizard_2spells]
                cantrips = 3
                spells_known = level * 2
            elif level == 4:
                possible_spells = [self.wizard_1spells, self.wizard_2spells]
                cantrips = 4
                spells_known = level * 2
            elif level == 5:
                possible_spells = [self.wizard_1spells, self.wizard_2spells, self.wizard_3spells]
                cantrips = 4
                spells_known = level * 2
            elif level == 6:
                possible_spells = [self.wizard_1spells, self.wizard_2spells, self.wizard_3spells]
                cantrips = 4
                spells_known = level * 2
            elif level == 7:
                possible_spells = [self.wizard_1spells, self.wizard_2spells, self.wizard_3spells,
                                   self.wizard_4spells]
                cantrips = 4
                spells_known = level * 2
            elif level == 8:
                possible_spells = [self.wizard_1spells, self.wizard_2spells, self.wizard_3spells,
                                   self.wizard_4spells]
                cantrips = 4
                spells_known = level * 2
            elif level == 9:
                possible_spells = [self.wizard_1spells, self.wizard_2spells, self.wizard_3spells,
                                   self.wizard_4spells, self.wizard_5spells]
                cantrips = 4
                spells_known = level * 2
            elif level == 10:
                possible_spells = [self.wizard_1spells, self.wizard_2spells, self.wizard_3spells,
                                   self.wizard_4spells, self.wizard_5spells]
                cantrips = 5
                spells_known = level * 2
            elif level == 11:
                possible_spells = [self.wizard_1spells, self.wizard_2spells, self.wizard_3spells,
                                   self.wizard_4spells, self.wizard_5spells, self.wizard_6spells]
                cantrips = 5
                spells_known = level * 2
            elif level == 12:
                possible_spells = [self.wizard_1spells, self.wizard_2spells, self.wizard_3spells,
                                   self.wizard_4spells, self.wizard_5spells, self.wizard_6spells]
                cantrips = 5
                spells_known = level * 2
            elif level == 13:
                possible_spells = [self.wizard_1spells, self.wizard_2spells, self.wizard_3spells,
                                   self.wizard_4spells, self.wizard_5spells, self.wizard_6spells,
                                   self.wizard_7spells]
                cantrips = 5
                spells_known = level * 2
            elif level == 14:
                possible_spells = [self.wizard_1spells, self.wizard_2spells, self.wizard_3spells,
                                   self.wizard_4spells, self.wizard_5spells, self.wizard_6spells,
                                   self.wizard_7spells]
                cantrips = 5
                spells_known = level * 2
            elif level == 15:
                possible_spells = [self.wizard_1spells, self.wizard_2spells, self.wizard_3spells,
                                   self.wizard_4spells, self.wizard_5spells, self.wizard_6spells,
                                   self.wizard_7spells, self.wizard_8spells]
                cantrips = 5
                spells_known = level * 2
            elif level == 16:
                possible_spells = [self.wizard_1spells, self.wizard_2spells, self.wizard_3spells,
                                   self.wizard_4spells, self.wizard_5spells, self.wizard_6spells,
                                   self.wizard_7spells, self.wizard_8spells]
                cantrips = 5
                spells_known = level * 2
            elif level == 17:
                possible_spells = [self.wizard_1spells, self.wizard_2spells, self.wizard_3spells,
                                   self.wizard_4spells, self.wizard_5spells, self.wizard_6spells,
                                   self.wizard_7spells, self.wizard_8spells, self.wizard_9spells]
                cantrips = 5
                spells_known = level * 2
            elif level == 18:
                possible_spells = [self.wizard_1spells, self.wizard_2spells, self.wizard_3spells,
                                   self.wizard_4spells, self.wizard_5spells, self.wizard_6spells,
                                   self.wizard_7spells, self.wizard_8spells, self.wizard_9spells]
                cantrips = 5
                spells_known = level * 2
            elif level == 19:
                possible_spells = [self.wizard_1spells, self.wizard_2spells, self.wizard_3spells,
                                   self.wizard_4spells, self.wizard_5spells, self.wizard_6spells,
                                   self.wizard_7spells, self.wizard_8spells, self.wizard_9spells]
                cantrips = 5
                spells_known = level * 2
            elif level == 20:
                possible_spells = [self.wizard_1spells, self.wizard_2spells, self.wizard_3spells,
                                   self.wizard_4spells, self.wizard_5spells, self.wizard_6spells,
                                   self.wizard_7spells, self.wizard_8spells, self.wizard_9spells]
                cantrips = 5
                spells_known = level * 2

        if cantrip_spells:
            while cantrips != 0:
                    spell = random.choice(cantrip_spells)
                    if spell not in spells:
                        spells.append(spell)
                        cantrips -= 1

        while spells_known != 0:
            list_choice = random.choice(possible_spells)
            spell = random.choice(list_choice)
            if spell not in spells:
                spells.append(spell)
                spells_known -= 1

        spells = sorted(spells, key=itemgetter(1))
        for spell in spells:
            spellbook += 'Spell level: ' + spell[1] + '\tSpell name: ' + spell[0] + '\n'

        self.outputFormat(spellbook)

if __name__ == '__main__':

    app = QApplication(sys.argv)

    form = MainWindow()
    form.show()

    sys.exit(app.exec_())
