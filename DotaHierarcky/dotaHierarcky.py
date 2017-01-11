class BasicCreature:

    def __init__(self, moveSpeed, clan, hp):
        self.moveSpeed = moveSpeed
        self.clan = clan
        self.hp = hp

        self.representMyself = None

    def move(self):
        print()
        return 'I am running now. My speed is: {}'.format(self.moveSpeed)
    
    def represent(self):
        print()
        self.representMyself = self.aboutMe()
        return self.representMyself

class AggressiveCreature(BasicCreature):

    def __init__(self, moveSpeed, clan, hp, attack):
        super().__init__(moveSpeed, clan, hp)

        self.attack = attack

    def fight(self):
        print()
        return 'I am fighting now. My attack equal to {attack}'.format(attack = self.attack)

class PeacefulCreature(BasicCreature):
    
    def __init__(self, moveSpeed, clan, hp):
        super().__init__(moveSpeed, clan, hp)

class Hero(AggressiveCreature):

    def __init__(self, moveSpeed, clan, hp, attack, strength, agility, intelligence, name):
        super().__init__(moveSpeed, clan, hp, attack)

        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.name = name
    
    def fight(self):
        fightCreature = super().fight()
        return '{0} and my attack speed is {1}% '.format(fightCreature, self.agility)

    def aboutMe(self):
        return 'Hello my name is {0:*^9} I have a lots of health points - {5:*^8}. I am fighting for {1:*^10} clan.\nLook at my attributes:\nstrenght - {2:*^4}\nagility - {3:*^4}\nintelligence - {4:*^4}'.format(self.name, self.clan, self.strength, self.agility, self.intelligence, self.hp)

class Crip(AggressiveCreature):
    
    def __init__(self, moveSpeed, clan, hp, attack):
        super().__init__(moveSpeed, clan, hp, attack)
    
    def fight(self):
        return super().fight()
    
    def aboutMe(self):
        return 'Hello I am just a stupid crip.\nI am very slow...my move speed is {0}, I have little health points {1} and attack {2}.\nNevertheless, I will fight for {3} clan!'.format(self.moveSpeed, self.hp, self.attack, self.clan)

class Courier(PeacefulCreature):
    def __init__(self, moveSpeed, clan, hp):
        super().__init__(moveSpeed, clan, hp)

    def upFlyingCourier(self):
        print()
        print('Thank you my friend!!I can fly now and I became faster!!')
        self.moveSpeed += 100
        return 'Moove speed upgraded: + {} ms'.format(self.moveSpeed)
    
    def aboutMe(self):
        return 'I am courier of {0} with {2} health points. I move with speed - {1}'.format(self.clan, self.moveSpeed, self.hp)

# Creating object of class Hero and calling its methods:

obj_Hero = Hero(300, 'Sentinel', 500, 45, 18, 20, 15, 'Slark') # Creating instance of class 'Hero'

print(obj_Hero.represent()) # Calling method 'represent' from super class 'BasicCreature'. Also method represent used methon aboutMe from class 'Hero'.

print(obj_Hero.move()) # Calling method 'move' from super class 'BasicCreature'.

print(obj_Hero.fight()) # Calling method 'fight' from class 'Hero'. This method 'fight' from 'Hero' used method with the same name 'fight' from super class 'AggressiveCreature'. So that we have Polymorphism.

# Similarly we will create object of 'Crip' class and call it's methods:

obj_Crip = Crip(200, 'Scourge', 400, 25)

print(obj_Crip.represent())

print(obj_Crip.move())

print(obj_Crip.fight())

# Creating object of class Courier and calling its methods:

obj_Courier = Courier(250, 'Sentinel', 100)

print(obj_Courier.represent())

print(obj_Courier.move())

print(obj_Courier.upFlyingCourier()) # Unlike Hero's and Crip's objects Courier's instance have method 'upFlyingCourier' which increase move speed of certain object.

print(obj_Courier.moveSpeed) # Check whether move speed incresed or not after applying 'upFlyingCourier method.