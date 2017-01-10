import random
warriors = ['Wizard', 'Berserk', 'Assassin']

def enemyHero(listWarriors):
    '''
    This function randomly select enemy from warriors list
    '''
    firstWarriors = 0
    amountEnemy = len(listWarriors)
    enemyIndex = random.randrange(firstWarriors, amountEnemy)
    enemy = listWarriors[enemyIndex]
    return enemy


def myHero(listWarriors):
    '''
    This function give the ability for player to select hero
    '''
    amountEnemy = len(listWarriors)
    print('{:*^60}'.format('Heroes'))
    for i in range(amountEnemy):
        print('{0:^18}'.format(listWarriors[i]), end = '')
    print('')
    print('{:*^60}'.format(''))
    print('')
    while True:
        hero = input('Choose your hero by typing his name: ')
        if hero in listWarriors:
            return hero
        else:
            print()
            print('You can write only one of the heroes names above. Let\'s try again!!')
            print()

def advert(hero, enemy):
    '''
    This function announce names of your hero and your enemy
    '''
    print('')
    print('{:!^60}'.format('Advert'))
    print('')
    hero_and_enemy = ' VS '.join([hero, enemy])
    print('{:^60}'.format(hero_and_enemy))
    print()

def winner(hero, enemy):
    '''
    This function define who is the winner
    '''
    hero_enemy = [hero, enemy]

    if 'Wizard' in hero_enemy and 'Berserk' in hero_enemy:
        return 'Wizard'
    elif 'Wizard' in hero_enemy and 'Assassin' in hero_enemy:
        return 'Assassin'
    elif 'Assassin' in hero_enemy and 'Berserk' in hero_enemy:
        return 'Berserk'
    else:
        return 'equal'

def battleResult(hero, enemy, winner):
    '''
    This function announce whether you win or lose
    '''
    print('{:+^60}'.format(''))
    print()
    if winner == hero:
        print('{:^60}'.format('You WIN'))
    elif winner == enemy:
        print('{:^60}'.format('You LOSE'))
    elif winner == 'equal':
        print('{:^60}'.format('Equal strength!!!'))
    print()
    print('{:+^60}'.format(''))




enemyHero = enemyHero(warriors)
myHero = myHero(warriors)

advert(myHero, enemyHero)

winner = winner(myHero,enemyHero)

battleResult(myHero, enemyHero, winner)
