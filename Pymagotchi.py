import time
#Pymagotchi is an electronic pet
#Choose your pet (cat, dog, rabbit or parrot)
#name it then play with it or feed it!

# Function to set up your electronic pet
def setup_pet():
	"""Prompts the user for pet type and name. 
	Returns and instance of Pet"""
	choice = raw_input("Choose a pet cat/dog/rabbit/parrot (type c/d/r/p): ")
	if choice not in ["c", "d", "r", "p"]:
		print "unknown command"
	else:
		name = raw_input("Choose a name: ")
		if choice == "c":
			pet = Cat(name, 3) 
		elif choice == "d":
			pet = Dog(name, 3)
		elif choice == "r":
			pet = Rabbit(name, 3)
		elif choice == "p":
			pet = Parrot(name, 3)
		else:
			print "unkown command"
		print "meet %s, your new %s!" %(name, pet.__class__.__name__)
		return pet

# Function to interact with your electronic pet
def pymagotchi(pet):
	"""Prompts the user to interact with its electronic pet."""
	print "To play with %s type 'play', to feed %s type 'eat', to hear your parrot sing type 'sing', to exit the game type 'exit': " \
			%(pet.name, pet.name)
	elec_pet = True
	while elec_pet:
		action = raw_input(" ")
		if action == "play":
			pet.play(pet.name, pet.hunger_level)
		elif action == "eat":
			pet.eat(pet.name, pet.hunger_level)
		elif action == 'sing':
			if pet.__class__.__name__ == 'Parrot':
				pet.sing(pet.name)
		elif action == "exit":
			elec_pet = False
		else:
			print "unknown command"

# Class Pet definition
class Pet(object):
	#pet has a name and hunger level
	def __init__(self, name, hunger_level):
		self.name = name
		self.hunger_level = hunger_level

	#pet can eat or play
	def eat(self, name, hunger_level):
		if self.hunger_level == 5:
			print "%s refuses to eat" %(self.name)
		else:
			if self.hunger_level < 5:
				self.hunger_level += 1
				print "%s is eating" %(self.name)
		print self.hunger_level
		return self.hunger_level

	def play(self, name, hunger_level):
		if self.hunger_level == 1:
			print "%s is too hungry" %(self.name)
		else:
			print "%s is playing" %(self.name)
			if self.hunger_level > 1:
				self.hunger_level -= 1
		return self.hunger_level

# Dog, Cat, Rabbit and Parrot all inherit from class Pet
# with a few differences. Dog get hungry faster and Parrot
# can sing
class Dog(Pet):
	def __init__(self, name, hunger_level):
		self.name = name
		self.hunger_level = hunger_level

	def play(self, name, hunger_level):
		if self.hunger_level == 1:
			print "%s is too hungry" %(self.name)
		else:
			if self.hunger_level > 2:
				self.hunger_level -= 2
			print "%s is playing" %(self.name)
		return self.hunger_level
	
class Cat(Pet):
	def __init__(self, name, hunger_level):
		self.name = name
		self.hunger_level = hunger_level

class Parrot(Pet):
	def __init__(self, name, hunger_level):
		self.name = name
		self.hunger_level = hunger_level
	def sing(self, name):
		print "%s is singing" %(self.name)

class Rabbit(Pet):
	def __init__(self, name, hunger_level):
		self.name = name
		self.hunger_level = hunger_level

# Set electroni pet, wait and prompt user to interact with its pet
if __name__ == "__main__":
	pet = setup_pet()
	if pet:
		time.sleep(1)
		pymagotchi(pet)

