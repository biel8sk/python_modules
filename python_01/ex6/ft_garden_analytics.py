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
        self.show_c = 0
        self.grow_c = 0
        self.age_c = 0
        self.life_time = 0

    def statics(s):
        print(f"[statics for {s.name}]")
        print(f"Stats: {s.grow_c} grow, {s.life_time} age, {s.show_c} show")

    def show(self):
        print(f"{self.name}: {self.__height:.1f}cm, {self.__age} days old")
        self.show_c += 1

    def grow(self):
        self.__height += 0.8
        self.__height = round(self.__height, 1)
        self.grow_c += 1

    def age_increment(self):
        self.__age += 1

    def pass_day(self):
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
        self.age_c += 1
        return self.__age


class Flower(Plant):
    def __init__(self, color, age, height, name):
        super().__init__(age=age, height=height, name=name)
        self.color = color
        self.bloom_count = 0

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")
        self.bloom_count += 1

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if (self.bloom_count < 1):
            print(f"{self.name} has not bloomet yet")


class Tree(Plant):
    def __init__(self, t_diameter, age, height, name):
        super().__init__(age=age, height=height, name=name)
        self.t_diam = t_diameter
        self.shades_count = 0

    def produce_shade(s):
        s.shades_count += 1
        print(f'''Tree {s.name} now produces a shade of {s.get_height()}
        cm long and {s.t_diam}cm wide''')

    def statics(self):
        super().statics()
        print(f"{self.shades_count} shade")


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
        super().__init__(age=age, height=height, name=name, color=color)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        self.seeds += 42

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")


def print_statics(plant: Plant):
    plant.statics()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_a_year_old(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_a_year_old(400)}\n")
    print("=== Flower")
    rose = Flower(name="Rose", age=34, height=30, color="yellow")
    rose.show()
    rose.statics()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("\n\n")
    print("=== Tree")
    tree = Tree(name="Dak", age=33, height=3424, t_diameter=3, )
    tree.show()
    tree.statics()
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    tree.statics()
    print("\n\n")
    print("=== Seed")
    seed = Seed(name="Sunflower", age=45, height=80, color="yellow")
    seed.show()
    print("[make sunflower grow, age and bloom]")
    seed.grow()
    seed.get_age()
    seed.bloom()
    seed.statics()
    print("\n\n=== Anonymous")
    anonymous = Plant.anonymous()
    anonymous.show()
    anonymous.statics()
