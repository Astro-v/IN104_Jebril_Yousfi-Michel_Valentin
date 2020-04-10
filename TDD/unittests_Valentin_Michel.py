import unittest

''' In this file I test the Mage classes '''

# Test of recieveDamage(self,damage)

class Test(unittest.TestCase):
    
    # attribute
    alice = Warrior("Alice",2,100,10,5)
    bob = Mage("Bob",1,100,30,6)
    values_receuveDamage = (10,20,50,100)
    values_isDead = ((100,False),(1,False),(0,True),(-1,True))
    
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
            
    def test_isDead(self):
        for value in self.values_isDead:
            self.bob.setHealth(value[0])
            self.assertIs(self.bob.isDead(),value[1])

if __name__ == '__main__':
    unittest.main()
