class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.__height = round(height, 1)
		self.__age = age
		self.life_time = 0
	def show(self):
		print(f"{self.name}: {self.__height:.1f}cm, {self.__age} days old")
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

if __name__ == "__main__":
	print("=== Plant Factory Output ===")
	rose = Plant("Rose", 34, 30)
	print("Plant created: ", end="")
	rose.show()
	print("\n\n")
	rose.set_age(25)
	rose.set_height(30)
	print("\n\n")
	rose.set_age(-2)
	rose.set_height(-1)
	print("\n\n")
	print("Current state: ", end="")
	rose.show()