class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = round(height, 1)
		self.age = age
		self.life_time = 0
	def show(self):
		print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")
	def grow(self):
		self.height += 0.8
		self.height = round(self.height, 1)
	def age_increment(self):
		self.age += 1
	def	pass_day(self):
		self.grow()
		self.age_increment()
		self.life_time += 1
		print(f"=== Day: {self.life_time} ===")
	def growth_day(self, days: int):
		growth = round(days * 0.8, 1)
		print(f"Growth this week: {growth}cm") 

if __name__ == "__main__":
	print("=== Plant Factory Output ===")
	rose = Plant("Rose", 25, 30)
	print("Created: ", end="")
	rose.show()
	oak = Plant("Oak", 200, 365)
	print("Created: ", end="")
	oak.show()
	cactus = Plant("Cactus", 5, 90)
	print("Created: ", end="")
	cactus.show()
	sun = Plant("Sun", 43, 90234)
	print("Created: ", end="")
	sun.show()
	fern = Plant("Fern", 3.432, 3)
	print("Created: ", end="")
	fern.show()
