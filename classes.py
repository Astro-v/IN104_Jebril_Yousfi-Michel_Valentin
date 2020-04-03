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

alice.description()
bob.description()
print("The fight start : Alice first")

turn = 0
while not alice.isDead() and not bob.isDead():
	turn += 1
	print("\n\n Turn number :", turn)
	alice.strike(bob)
	if bob.getMana()>= bob.fireballCost:
		bob.fireball(alice)
	else:
		bob.meditation()
	alice.description()
	bob.description()
