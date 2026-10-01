import ftpla

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