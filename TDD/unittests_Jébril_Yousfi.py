#### CLASS ####

class Character:
    def __init__(self,name,level,health):
    	self.name = name
    	self.level = level
    	self.health = health+0.2*(level-1)*health
	
    def description(self):
    	print("Hi, my name is ", self.name, ", I'm level", self.level, "and I have ", self.__health, "hp")
	
    def recieveDamage(self,damage):
    	self.health = self.health - damage
		
    def isDead(self):
    	return self.health <= 0
    
    def getHealth(self):
        return self.health

class Warrior(Character):
    def __init__(self,name,level,health,sword,baseHeal):
    	Character.__init__(self,name,level,health*1.2)
    	self.sword = sword+sword*0.6*(level-1)
    	self.baseHeal = baseHeal
    	self.heal= baseHeal*level

    def strike(self,cible):
    	cible.recieveDamage(self.sword)
		
    def eat(self):
    	self.health = self.health + self.heal
		
class Mage(Character):
    def __init__(self,name,level,health,power,manaRegen):
    	Character.__init__(self,name,level,health)
    	self.__mana = 100
    	self.manaRegen = manaRegen
    	self.power = power
    	self.fireballCost = 10
		
    def fireball(self,cible):
    	if self.__mana < self.fireballCost:
    		return "Insufficient mana"
    	self.__mana = self.__mana - self.fireballCost
    	cible.recieveDamage(0.7*self.power)
		
    def meditation(self):
    	self.__mana = semf.__mana + self.manaRegen
	
    def getMana(self):
    	return self.__mana
		
#### MAIN ####

alice = Warrior("Alice",2,100,10,5)
bob = Mage("Bob",1,100,30,6)


####TEST####

import unittest as un

class TestNum(un.TestCase):
    def testStrike(self):
        hpi = bob.getHealth()
        alice.strike(bob)
        hpf = bob.getHealth()
        self.assertEqual(hpi-hpf,16,"Should be 16")
        
    def testEat(self):
        hpi = alice.getHealth()
        alice.eat()
        hpf = alice.getHealth()
        self.assertEqual(hpf-hpi,10,"Should be 10")
        
    def testRecieveDamage(self):
        hpi = alice.getHealth()
        alice.recieveDamage(15)
        hpf = alice.getHealth()
        self.assertEqual(hpi-hpf,15,"Should be 15")
        
    def testIsDead(self):
        self.assertFalse(alice.isDead(),"Should be False")


if __name__ == '__main__':
    un.main()
