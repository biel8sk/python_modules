class Plant:
	@staticmethod
	def is_a_year_old(age):
		return (age > 365)
	@classmethod
	def anonymous(cls):
		return cls("Anonimo", 0, 0)
	def __init__(self, name, height, age):
		self.name = name
		self.__height = round(height, 1)
		self.__age = age
		self.life_time = 0
		
	def show(self):
		print(f"{self.name}: {self.__height:.1f}cm, {self.__age} days old")
	def grow(self):
		self.__height += 0.8
		self.__height = round(self.__height, 1)
	def age_increment(self):
		self.__age += 1
	def	pass_day(self):
		self.grow()
		self.age_increment()
		self.life_time += 1
		print(f"=== Day: {self.life_time} ===")
	def growth_day(self, days: int):
		self.growth = round(days * 0.8, 1)
		print(f"Growth this week: {self.growth}cm")
	def set_height(self, new_height: int):
		if (new_height > 0):
			self.__height = new_height
			print(f"Height updated: {new_height}")
			return
		print("Error, height can't be negative\nHeight update rejected")
	def set_age(self, new_age: int):
		if (new_age > 0):
			self.__age = new_age
			print(f"Age updated: {new_age}")
			return
		print("Error, age can't be negative\nAge update rejected")
	def get_height(self):
		return self.__height
	def get_age(self):
		return self.__age

class Flower(Plant):
	def __init__(self, color, age, height, name):
		super().__init__(age=age, height=height, name=name)
		self.color = color
		self.count_bloom = 0
	def bloom(self):
		self.count_bloom += 1
		print(f"{self.name} is blooming beautifully!")
	def show(self):
		super().show()
		print(f"Color: {self.color}")
		print(f"{self.name} has not bloomet yet")

class Tree(Plant):
	def __init__(self, trunk_diameter, age, height, name):
		super().__init__(age=age, height=height, name=name)
		self.trunk_diameter = trunk_diameter
	def produce_shade(self):
		print(f"Tree {self.name} now produces a shade of {self.get_height()}cm long and {self.trunk_diameter}cm wide")

class Vegetable(Plant):
	def __init__(self, harvest_season, age, height, name, nutritional_value):
		super().__init__(age=age, height=height, name=name)
		self.harvest_season = harvest_season
		self.nutritional_value = nutritional_value
	def pass_day(self):
		super().pass_day()
		self.nutritional_value += 1
	def show(self):
		super().show()
		print(f"Harvest season: {self.harvest_season}")
		print(f"Nutrition value: {self.nutritional_value}")

class Seed(Flower):
	def __init__(self, color, age, height, name):
		self.count_bloom = 0

if __name__ == "__main__":
	print("=== Garden Plan Types ===")
	print("=== Flower")
	rose = Flower(name="Rose", age=34, height=30, color="yellow")
	rose.show()
	print("[asking the rose to bloom]")
	rose.show()
	print(rose.__height)
	rose.bloom()
	rose.show()
	print("\n\n")
	print("=== Tree")
	tree = Tree(name="Dak", age=33, height=3424, trunk_diameter=3, )
	tree.show()
	print("[asking the oak to produce shade]")
	tree.show()
	tree.produce_shade()
	print("\n\n")
	print("=== Vegetable")
	veg = Vegetable(name="Tomato", age=2, height=1,harvest_season="April", nutritional_value=0)
	veg.show()
	print("[make tomato grow and age for 20 days]")
	for i in range(20):
		veg.pass_day()
	veg.show()
