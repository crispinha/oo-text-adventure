import classes, sys


class Player(object):
	def __init__(self, location):
		self.inventory = [classes.example_item]
		self.location = location

	def get_inventory(self):
		return self.inventory

	def get_inventory_names(self):
		output = ""
		for i, item in enumerate(self.inventory):
			output += item.get_name()
			if i != len(self.inventory) - 1: output += ", "
		return output

	def get_inventory_names_and_descs(self):
		output = ""
		for i, item in enumerate(self.inventory):
			output += f"{item.get_name()} ({item.get_description()})"
			if i != len(self.inventory) - 1: output += ", "
		return output

	def stock_inventory(self, item):
		self.inventory.append(item)

	def take_from_inventory(self, item):
		if item in self.inventory:
			self.inventory.remove(item)
		else:
			print("Item not found in inventory, check ur code crispin.")


def move(direction):
	#probably a horrble manglement
	global current_scene
	compass = current_scene.get_compass()
	if direction == "n" or direction == "north":
		if compass[0]:
			current_scene = map.get_scene(compass[0])
			print(f"You are standing in a {current_scene.get_description_and_items()}")
		else:
			print("You can't go there.")
	elif direction == "e" or direction == "east":
		if compass[1]:
			current_scene = map.get_scene(compass[1])
			print(f"You are standing in a {current_scene.get_description_and_items()}")
		else:
			print("You can't go there.")
	elif direction == "s" or direction == "south":
		if compass[2]:
			current_scene = map.get_scene(compass[2])
			print(f"You are standing in a {current_scene.get_description_and_items()}")
		else:
			print("You can't go there.")
	elif direction == "w" or direction == "west":
		if compass[3]:
			current_scene = map.get_scene(compass[3])
			print(f"You are standing in a {current_scene.get_description_and_items()}")
		else:
			print("You can't go there.")
	else:
		print("That's not a direction")

#init stuff
start_scene = "example"
map = classes.Map()
current_scene = map.get_scene(start_scene)

player = Player(start_scene)
print(f"You are standing in a {current_scene.get_description()}")

while True:
	command = input("> ")
	if command == "help":
		print("hey")
	elif command == "look" or command == "l":
		print(f"You are standing in a {current_scene.get_description_and_items()}")
	elif command == "i" or command == "inv" or command == "inventory":
		print(player.get_inventory_names_and_descs())
	elif command == "drop":
		print("What are you dropping?")
	elif command[:5] == "drop ":
		done = 0
		for i in player.get_inventory():
			if i.get_name().lower() == command[5:].lower():
				current_scene.add_item(i)
				print(f"You have dropped your {i.get_name()}.")
				player.take_from_inventory(i)
				done = 1
				break
		if not done: print("You don't have one of those to drop.")
	elif command == "take":
		print("What are you taking?")
	elif command[:5] == "take ":
		done = 0
		for i in current_scene.get_items():
			if i.get_name().lower() == command[5:].lower():
				player.stock_inventory(i)
				print(f"You have taken a {i.get_name()}.")
				current_scene.take_item(i)
				done = 1
				break
		if not done: print("There isn't one of those to take.")
	elif command == "unlock":
		print("Unlock with what?")
	elif command[:7] == "unlock ":
		done = 0
		if current_scene.get_type() == "locked":
			for i in player.get_inventory():
				if i.get_name().lower() == command[7:].lower():
					if i == i:
						if current_scene.unlock(i): print("You unlock the door")
						else: print("Something's wrong.")
						done = 1
					else:
						done = 1
						print("That is not the key.")
					break
			if not done: print("You don't have that.")
		else:
			print("There is nothing to unlock here.")
	elif command == "go" or command == "move":
		print("Where are you going?")
	elif command[:3] == "go " or command[:5] == "move ":
		if command[:3] == "go ": move(command[3:])
		else: move(command[5:])
	elif command == "quit" or command == "exit":
		sys.exit()
	elif command == "unlocked":
		if current_scene.get_type() == "locked":
			print(current_scene.get_unlocked_status())
	else:
		print("invalid command\ntry again, but better")

