class Plant:
    @staticmethod
    def is_a_year_old(age):
        return (age > 365)

    @classmethod
    def anonymous(cls):
        return cls("Anonimo", 0, 0)

    class Statistics:
        GROW_COUNT = 0
        SHOW_COUNT = 0
        AGE_COUNT = 0

        @classmethod
        def show(cls, plant):
            print(f"[statics for {plant.name}]")
            msg1 = f"Stats: {cls.GROW_COUNT} grow, "
            msg2 = f"{cls.AGE_COUNT} age, "
            msg3 = f"{cls.SHOW_COUNT} show"
            print(msg1 + msg2 + msg3)

    def __init__(self, name, height, age):
        self.name = name
        self._height = round(height, 1)
        self._age = age
        self.life_time = 0

    def show(self):
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")
        self.Statistics.SHOW_COUNT += 1

    def grow(self):
        self._height += 0.8
        self._height = round(self._height, 1)
        self.Statistics.GROW_COUNT += 1

    def age_increment(self):
        self._age += 1

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
            self._height = new_height
            print(f"Height updated: {new_height}")
            return
        print("Error, height can't be negative\nHeight update rejected")

    def set_age(self, new_age: int):
        if (new_age > 0):
            self._age = new_age
            print(f"Age updated: {new_age}")
            return
        print("Error, age can't be negative\nAge update rejected")

    def get_height(self):
        return self._height

    def get_age(self):
        self.Statistics.AGE_COUNT += 1
        return self._age


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
        h = s.get_height()
        d = s.t_diam
        n = s.name
        msg = f"Tree {n} now produces a shade of {h}cm long and {d}cm wide"
        print(msg)

    class Statistic(Plant.Statistics):
        SHADE_COUNT = 0

        def show(cls, self):
            super().show(self)
            print(f"{cls.SHADE_COUNT} shade")


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
    plant.Statistics.show(plant)


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_a_year_old(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_a_year_old(400)}\n")
    print("=== Flower")
    rose = Flower(name="Rose", age=34, height=30, color="yellow")
    rose.show()
    rose.Statistics.show(rose)
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("\n\n")
    print("=== Tree")
    tree = Tree(name="Dak", age=33, height=3424, t_diameter=3, )
    tree.show()
    tree.Statistics.show(tree)
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    tree.Statistics.show(tree)
    print("\n\n")
    print("=== Seed")
    seed = Seed(name="Sunflower", age=45, height=80, color="yellow")
    seed.show()
    print("[make sunflower grow, age and bloom]")
    seed.grow()
    seed.get_age()
    seed.bloom()
    seed.Statistics.show(seed)
    print("\n\n=== Anonymous")
    anonymous = Plant.anonymous()
    anonymous.show()
    anonymous.Statistics.show(anonymous)
