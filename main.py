class DataBase:
    def __init__(self, items):
        self.items = items

    def write_data(self, element):
        self.items.append(element)


class Data:
    def __init__(self, country, name, age, gender, height, weight):
        self.country = country
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

