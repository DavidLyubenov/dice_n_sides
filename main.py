import sys
import os
import random
from datetime import time


# screen_width = 100
#
# character_name = 'name'
# character_role = 'role'
# character_weapon = 'weapon'
# character_hp = 1
# character_dmg = 1
# character_mana = 1
# character_resistance = 1
# character_attack_speed = 1.0
# character_luck = 1
# character_status_effects = []
#
#
# # PLAYER SETUP #
# class Player:
#     def __init__(self, name, role, weapon, hp, dmg, mana, resistance, attack_speed, luck, status_effects):
#         self.name = character_name
#         self.role = character_role
#         self.weapon = character_weapon
#         self.hp = character_hp
#         self.dmg = character_dmg
#         self.mana = character_mana
#         self.resistance = character_resistance
#         self.attack_speed = character_attack_speed
#         self.luck = character_luck
#         self.status_effects = character_status_effects
#
#
# myPlayer = Player()
#
#
# # TITLE SCREEN #
# def title_screen_selections():
#     option = input("> ")
#     while option.lower() not in ('plau', 'load game', 'quit'):
#         print('Please enter a valid command.')
#         option = input('> ')
#     #    if option.lower() == "play":
#     #       start_game() #placeholder until written
#     #   elif option.lower() == "load game":
#     #       load_game() #placeholder until written
#     if option.lower() == "quit":
#         sys.exit()
#     elif option.lower() == 'play':
#         pass
#
#
# def title_screen():
#     os.system('cls')
#     print()
#     print()
#     print()
#     print()
#     print()
#     print()
#     print()
#     title_screen_selections()


# def other_menu():
#    print()
#    print()
#    print()
#    print()
#    print()
#    print()
#    print()
#    title_screen_selections()

def clear_console():
    import os
    clear = lambda: os.system('cls')
    clear()


# MAIN MENU
def main_menu():
    os.system('cls')
    print()
    print(f'####################################')
    print(f'######## BOTTOM TEXT HERE ##########')
    print(f'####################################')
    print(f'###### PICK UP TO TWO ANSWERS ######')
    print(f'####################################')
    print(f'####### > > > P L A Y < < <  #######')
    print(f'####################################')
    print(f'###########    O R    ##############')
    print(f'####################################')
    print(f'######## QUIT LIKE A BITCH #########')
    print(f'####################################')
    print(f'########## TOP TEXT HERE ###########')
    print(f'####################################')
    print(f'####################################')

    option = input(f'MAKE THE RIGHT DECISION... OR ELSE!! ')

    if option.lower() in ('quit', '2', 'q', 'exit', 'quit like a bitch'):
        sys.exit(0)
    else:
        os.system('cls')


# You DIED function xd
def you_died():
    print('> > > --- YOU DIED --- < < <')
    print('> > > __like a bitch__ < < <')
    main_menu()


# Dice rolling function
def roll_six():
    basic_roll = random.randint(1, 6)
    print('##########################')
    print(f'You rolled a {basic_roll}')
    print('##########################')


def roll_twenty():
    extended_roll = random.randint(1, 20)
    print('#############################')
    print(f'You rolled a {extended_roll}')
    print('#############################')


main_menu()


print(f'> You wake up in a place, you\'ve never seen before')
print(f'> A strange man approaches you.')

name = input("- Hello, traveler, what is your name? ")
# name = name.capitalize()
clear_console()
print(f'- Oh, so you are the one everyone is talking about, huh?')
print(f'- May I ask you something? Some say you are a mage, other a warrior and third even say you are an archer...')
print(f'- So you are a?')
role_selection = ['warrior', "mage", "archer"]
print(f'Choose a role : {role_selection}')
role = input("I aaam... ")

# character_role = role
weapon = ''
hp = 0
dmg = 0
mana = 0
resistance = 0
attack_speed = 0

# Setting up the stats boy
if role.lower() == "mage":
    weapon = 'staff'
    hp = 8
    dmg = 2.4
    mana = 4
    resistance = 0
    attack_speed = 1
elif role.lower() == "warrior":
    weapon = 'sword'
    p = 12
    dmg = 1.3
    mana = 2
    resistance = 2
    attack_speed = 1
elif role.lower() == "archer":
    weapon = 'bow'
    hp = 10
    dmg = 3
    mana = 2
    resistance = 1
    attack_speed = 3
else:
    while role not in ('mage', 'archer', 'warrior'):
        print(f'What did you say?')
        role = input()
        if role.lower() == "mage":
            weapon = 'staff'
            hp = 8
            dmg = 2.4
            mana = 4
            resistance = 0
            attack_speed = 1
            break
        elif role.lower() == "warrior":
            weapon = 'sword'
            p = 12
            dmg = 1.3
            mana = 2
            resistance = 2
            attack_speed = 1
            break
        elif role.lower() == "archer":
            weapon = 'bow'
            hp = 10
            dmg = 3
            mana = 2
            resistance = 1
            attack_speed = 3
            break


clear_console()
# ACT 1 STARTS:
print(f'- OH REALLY DUDE???? SWEET')
print(f'- My father was {role} as well and I always wanted to be like him :3')
print(f'- Would you like to come to my place and chill for a bit')
print(f'- We could feast together, I\'m sure you have a shit ton of stories to tell the world!')
print(f'- So, what do you say?')

answer = input('### Yes or No? ###')

if answer.lower() == "yes" or answer.lower() == 'y':
    mana += 1
    print(f'Oh... Let/s go then...')
    print('*The stranger heads to the nearby woods, which is strange,')
    print('but you decided to follow him, so it/s your problem now...')
    print("You are already walking through the woods and you start hearing strange noises...")
    # grrrr grrrr goblin noices
    print('You ask him if he knows the source of these noises')
    print('the stranger laughs...')
    print('- Oh I forgot to introduce myself, how rude of me... sorry...')
    print(f'My name is Mikkel. I\'m a self-learning newbie {role}')
    print(f'but I\'m sure I will never become as famous as you are...')
    ask_first = input("You can ask him: Why? / Or say: Understandable / Or: Don\'t ask anything ")
    if ask_first.lower() in ("why", "why?", "y", "y?", '1'):
        print(f'Well, uh, as i said... everyone in my village have heard about you and what you\'ve done')
    elif ask_first.lower == 'understandable' or ask_first.lower() == '2':
        print(f'your respond creates an awkward silence that may not be disrupted for a long time')
    elif ask_first.lower() == "dont ask anything" or ask_first.lower() == '3':
        print(f'*feels like the noises are starting to get closer and closer*')

action = 0

while True:
    if answer.lower() in ("no", "n"):
        print(f'> The stranger takes your answer as an insult.')
        print(f'> He grabs his dagger and points it at you...')
        print(f'######## What do you do? ###########')
        print('#####################################')
        print(f'# 1. Search yourself for a weapon. #')
        print('#####################################')
        print(f'## 2. Try talking him out of it. ###')
        print('#####################################')
        print(f'########## 3. Run away. ############')
        print('#####################################')
        print(f'######### 4. Laugh at him. #########')
        print('#####################################')
        print(f'########### 5. No action ###########')
        action = int(input())
        if action == 1:
            print(f'> You start going through your pockets but they are empty...')
            print('> The stranger charges at you...')
            print('> Maybe you should\'ve chosen a different action...')
            print(f'> I am almost sure you are just going to die here...')
            print('> Kind of sad, ain\'t it?')
            print('> His knife is 6.66 centimeters away and you will be stabbed any moment now...')
            print('> But suddenly something strange happens... As the dagger touches you')
            # shield sounds
            print('> something like a magical shield spawns around you')
            print('> and the dagger with the stranger\'s hand go inside you')
            print(f'> Not in the sexual way of course, even though it would be way easier to explain')
            print(f'> The stranger backs up... His weapon and half of his hand are missing')
            # screaming sounds
            print(f'> Screaming for help he runs away in fear')
            break
        elif action == 2:
            print('> You say:')
            print('- Lets stop before someone gets hurt.')
            print(f"-Pff, - the stranger continues - And what you can do to stop me, {name.capitalize()}?!")
            print('......')
            print(f'- That\'s what I thought, {name.capitalize()}. Now what?')
            break
            ###########################
            ###########################
            ###########################
        elif action == 3:
            print('> You head to the nearby woods')
            print('> As going deeper and deeper through the woods, you start hearing weird noises')
            print('> It seems like you lost the stranger though...')
            break
        elif action == 4:
            print('> Your laugh is followed by silence')
            print('> You say to him to run away before you take off your sword and cut off his head')
            print('> The stranger changed the way he was looking at you.')
            print(f'- You dont have the balls, {name.capitalize()}.. Come at me bro')
            print(f'> As soon as you grabbed the {weapon} from your backpack,')
            print('> he ran away in fear...')
            print(f'> > > ...like a bitch... < < <')
            break
        elif action == 5:
            print(f'> The man starts screaming: "CHAAARGE", as he runs closer and closer to you')
            print(f'> He stabs you with his dagger.... multiple times...')
            print('> maybe he is Varg from another dimension')
            you_died()
        else:
            print('### Please select a valid action: ###')
            print('#####################################')
            print(f'# 1. Search yourself for a weapon. #')
            print('#####################################')
            print(f'## 2. Try talking him out of it. ###')
            print('#####################################')
            print(f'########## 3. Run away. ############')
            print('#####################################')
            print(f'######### 4. Laugh at him. #########')
            print('#####################################')
            print(f'########### 5. No action ###########')
            action = input()
