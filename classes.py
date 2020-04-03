class Character:
	def __init__(self,name):
		self.name = name
		self.level = 1
		self.__health = 100
		
	def description(self):
		print("Hi, my name is ", self.name, ", I'm level", self.level, "and i have ", self.__health, "hp")
		
	def recieveDamage(self,damage):
		self.__health = self.__health - damage

class Warrior(Character):
	def __init__(self,name,sword,baseHeal):
		Character.init(self,name)
		self.sword = sword
		self.baseHeal = baseHeal
		self.heal= baseHeal*level

	def strike(self,cible):
		cible.recieveDamage(sword)
		
	def eat(self):
		self.health = self.health + self.heal
		
class Mage(Characters):
	def __init__(self,name,manaRegen,power):
		Character.init(self,name)
		self.mana = 100
		self.manaRegen = manaRegen
		self.power = power
		self.fireballCost = 10
		
	def fireball(self,cible):
		if self.mana < fireballCost:
			return "Insufficient mana"
		self.mana = self.mana - self.fireballCost
		cible.health = cible.health - 0.7*self.power
		
	def meditation(self):
		self.mana = semf.mana + self.manaRegen
		
		
		
		
		
