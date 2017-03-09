class Map(object):
	def __init__(self):
		self.scenes = {
			"example": locations[0],
			"hallway": locations[1],
			"entryway": locations[2]
		}

	def get_scene(self, scene):
		return self.scenes[scene]


class Item(object):
	def __init__(self, name, description):
		self.name = name
		self.description = description

	def get_name(self):
		return self.name

	def get_description(self):
		return self.description


class Location(object):
	def __init__(self, compass, items, description):
		self.compass = compass
		self.items = items
		self.description = description

	def get_type(self):
		return "base"

	def get_compass(self):
		#never eat soggy weetbix
		return self.compass

	def get_items(self):
		return self.items

	def take_item(self, item):
		if item in self.items:
			self.items.remove(item)
			return item
		else:
			print("no item there")
			return None

	def add_item(self, item):
		self.items.append(item)
		return item;

	def get_description(self):
		return self.description

	def get_description_and_items(self):
		return f"{self.get_description()}\nIt contains {self.get_item_names()}"

	def get_item_names(self):
		if self.items:
			output = ""
			for i, item in enumerate(self.items):
				output += item.get_name()
				if i != len(self.items) - 1: output += ", "
				else: output += "."
			return output
		else:
			return "nothing."

	def get_item_names_and_descs(self):
		output = ""
		if self.items:
			for i, item in enumerate(self.items):
				output += f"{item.get_name()} ({item.get_description()})"
				if i != len(self.items) - 1: output += ", "
				else: output += "."
			return output
		else:
			return "nothing"


class LockedLocation(Location):
		def __init__(self, compass, items, description, key, is_unlocked, unlocked_compass, unlocked_description):
			self.key = key
			self.is_unlocked = is_unlocked
			self.unlocked_compass = unlocked_compass
			self.unlocked_description = unlocked_description
			super(LockedLocation, self).__init__(compass, items, description)

		def get_type(self):
			return "locked"

		def get_description(self):
			if self.is_unlocked:
				return self.unlocked_description
			else:
				return self.description

		def get_compass(self):
			if self.is_unlocked:
				return self.unlocked_compass
			else:
				return self.compass

		def get_unlocked_status(self):
			return self.is_unlocked

		def get_key(self):
			return self.key

		def unlock(self, key):
			if key.get_name() == self.key.get_name():
				self.is_unlocked = True
				return True
			else:
				return False

example_item = Item("Example Item", "perfectly bland")
key = Item("Key", "Looks pretty insecure")
locations = [Location(["hallway", None, None, None], [example_item, example_item, example_item], "perfectly blank room.\nNothing leads here."),
			Location([None, None, "example", "entryway"], [key], "hallway.\nThere is quite a nice lamp on a wooden dresser."),
			LockedLocation([None, "hallway", None, None], [], "room with a locked door to the north.", key, False,
							["example", "hallway", None, None], "room with an open door to the north")
			]

if __name__ == "__main__":
	print(locations[2].get_description())
	print(locations[2].get_compass())
	print(locations[2].get_items())
	locations[2].unlock(key)
	print(locations[2].get_compass())
	print(locations[2].get_description())


