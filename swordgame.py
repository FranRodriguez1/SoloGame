import random

MAX_HERO_HEALTH = 40


# 1) Functions
# Function to display character health, armour, and weapon values
def show_character_stats(character):
    for key in character:
        if character[key] != 0 and key != 'name':
            print(key+':', character[key])
    print('')

# Function to choose a valid weapon for attack
def choose_valid_weapon():
    weapon = ''
    weapons_available = list_of_available_weapons(hero)

    while weapon not in weapons_available:
        weapon = input('Choose a weapon to attack: ')
        if weapon not in weapons_available:
            print('You cannot attack with that.')
    return weapon

# Function to randomize attack power within a range
def randomize_attack_power(weapon_strength):
    attack = random.randint(weapon_strength - 5, weapon_strength + 5)
    return attack

# Function to randomize attack power within a smaller range for precise weapons
def randomize_precise_attack(weapon_strength):
    attack = random.randint(weapon_strength - 2, weapon_strength + 2)
    return attack

# Function to get a list of available weapons for a character
def list_of_available_weapons(character):
    weapons_available = list(character.keys())[3:]
    return weapons_available

# Function to perform an attack on the enemy
def perform_attack(enemy):
    weapon_chosen = choose_valid_weapon()

    if weapon_chosen == 'bow':
        attack_power = randomize_precise_attack(hero[weapon_chosen])
    else:
        attack_power = randomize_attack_power(hero[weapon_chosen]) - enemy['armour']
        if attack_power < 0:
            attack_power = 0

    enemy['health'] -= attack_power
    if enemy['health'] < 0:
        enemy['health'] = 0

    print('You have dealt', attack_power, 'damage to', enemy['name'])
    print(enemy['name'], 'has', enemy['health'], 'health remaining')

# Function to recieve an attack from the enemy
def recieve_attack(enemy):
    weapons_available = list_of_available_weapons(enemy)
    weapon_chosen = random.choice(weapons_available)

    if weapon_chosen == 'bow':
        attack_power = randomize_precise_attack(enemy[weapon_chosen])
    else:
        attack_power = randomize_attack_power(enemy[weapon_chosen]) - hero['armour']
        if attack_power < 0:
            attack_power = 0

    hero['health'] -= attack_power
    if hero['health'] < 0:
        hero['health'] = 0

    print(enemy['name'], 'has dealt', attack_power, 'damage with his', weapon_chosen)
    print('You have', hero['health'], 'health remaining')

# Function to simulate a fight between the hero and an enemy
def fight(enemy):
    while enemy['health'] > 0 and hero['health'] > 0:
        perform_attack(enemy)
        print('')

        if enemy['health'] > 0:
            recieve_attack(enemy)
            print('')
        else:
            hero['health'] = MAX_HERO_HEALTH
            print('Congratulations! You have defeated', enemy['name']+'.')

    if hero['health'] == 0:
        print('You have been defeated. Better luck next time.')
        quit()

# Function to offer an option to display updated character values
def offer_gear_display():
    show_gear = input('Would you like to view your updated gear? (yes/no):')
    if show_gear == 'yes':
        show_character_stats(hero)
        
        
# 2) Characters
# Define the attributes for different characters in the game
hero = { 'name': 'Hero', 'health': 40,  'armour': 0, 'sword': 15}

goblin = { 'name': 'the goblin', 'health': 30,  'armour': 0, 'dagger': 10}

guard = { 'name': 'the guard', 'health': 35,  'armour': 5, 'spear': 15, 'dagger':10}

mercenary = {'name': 'the mercenary', 'health': 45,  'armour': 3, 'axe': 17, 'bow':12}


# 3) Adventure:
# Display the initial gear for the hero
print('Welcome traveler!\nBefore you embark on your adventure, \
here is your starting gear:')
show_character_stats(hero)

# Encounter with the goblin
print('Oh no! A greedy goblin has challenged you to a fight.')
show_character_stats(goblin)
fight(goblin)

# Inform the player about healing and acquiring a bow
print('After every fight, you will be healed to maximum health.\n\
You have earned a bow.\nThe bow deals less damage than the sword, but its \
damage is more consistent and can pierce through armour.\n')
hero['bow'] = 12

# Offer an option to display updated gear/stats
offer_gear_display()

# Encounter with the guard and update hero's gear
print('\nAn armoured guard is threatening to arrest you!')
show_character_stats(guard)
fight(guard)
print("You have stolen the guard's armour")
hero['armour'] = guard['armour']

# Offer an option to display updated gear/stats
offer_gear_display()

# Final encounter with the mercenary
print('Before you can return home safely, you must defeat the powerful \
mercenary who has been tasked with your capture.')
show_character_stats(mercenary)
fight(mercenary)

# End of the game 
print('Thank you for playing the game.')
