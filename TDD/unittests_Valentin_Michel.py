#### CLASS ####

class Character:
	def __init__(self,name,level,health):
		self.name = name
		self.level = level
		self.__health = health+0.2*(level-1)*health

	def description(self):
		print("Hi, my name is ", self.name, ", I'm level", self.level, "and I have ", self.__health, "hp")

	def recieveDamage(self,damage):
		self.__health = self.__health - damage

	def isDead(self):
		return self.__health <= 0

	def getHealth(self):
		return self.__health

	def setHealth(self,health):
		self.__health = health

class Warrior(Character):
	def __init__(self,name,level,health,sword,baseHeal):
		Character.__init__(self,name,level,health*1.2)
		self.sword = sword+sword*0.6*(level-1)
		self.baseHeal = baseHeal
		self.heal= baseHeal*level

	def strike(self,cible):
		cible.recieveDamage(self.sword)

	def eat(self):
		self.setHealth(self.getHelath() + self.heal)

class Mage(Character):
	def __init__(self,name,level,health,power,manaRegen):
		Character.__init__(self,name,level,health)
		self.__mana = 100
		self.manaRegen = manaRegen
		self.power = power
		self.fireballCost = 10
		self.manaMax = 100

	def fireball(self,cible):
		if self.__mana < self.fireballCost:
			return "Insufficient mana"
		self.__mana = self.__mana - self.fireballCost
		cible.recieveDamage(0.7*self.power)

	def meditation(self):
		if self.__mana + self.manaRegen <= 100:
			self.__mana = self.__mana + self.manaRegen
		else:
			self.__mana = 100

	def getMana(self):
		return self.__mana

	def setMana(self,mana):
		self.__mana = self.__mana + mana

	def getManaRegen(self):
		return self.manaRegen

	def setManaRegen(self,manaRegen):
		self.manaRegen = manaRegen

#### TEST ####

import unittest

''' In this file I test the Mage classes '''

# Test of recieveDamage(self,damage)

class Test(unittest.TestCase):

	# attribute
	alice = Warrior("Alice",2,100,10,5)
	bob = Mage("Bob",1,100,30,6)
	values_receuveDamage = (10,20,50,100)
	values_isDead = ((100,False),(1,False),(0,True),(-1,True))
	values_meditation = ((100,10,100),(100,0,100),(80,30,100))
	# methode
	def test_receiveDamage(self):
		for value in self.values_receuveDamage:
			initialLife = self.bob.getHealth()
			self.bob.recieveDamage(value)
			finalLife = self.bob.getHealth()
			result = initialLife-finalLife
			self.assertEqual(value, result)

	def test_isDead(self):
		for value in self.values_isDead:
			self.bob.setHealth(value[0])
			self.assertIs(self.bob.isDead(),value[1])

	def test_meditation(self):
		for value in self.values_meditation:
			self.bob.setMana(value[0])
			self.bob.setManaRegen(value[1])
			self.bob.meditation()
			self.assertEqual(self.bob.getMana(),value[2])

if __name__ == '__main__':
	unittest.main()
