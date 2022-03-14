class DataBase:
    def __init__(self, items):
        self.items = items

    def write_data(self, element):
        self.items.append(element)

    def read_data(self, criteria):
        for item in self.items:
            if item.name == criteria:
                return item


class Data:
    def __init__(self, country=None, name=None, age=None, gender=None, height=None, weight=None):
        self.country = country
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

        self.dict_items = {
            'country': self.country,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'height': self.height,
            'weight': self.weight
        }


data = Data('Russia', 'Abakar', 28, 'male', 172, 70)
data2 = Data('Russia', 'Ivan', 21, 'male', 172, 70)
data3 = Data('Russia', 'Igor', 35, 'male', 172, 70)

data_base = DataBase(items=[])
data_base.write_data(data)
data_base.write_data(data2)
data_base.write_data(data3)

print(data.country, data.name)
print(data_base)
print(data_base.read_data('Igor').age)
print(data_base.read_data('Ivan').age)
print(data_base.read_data('Abakar').age)

