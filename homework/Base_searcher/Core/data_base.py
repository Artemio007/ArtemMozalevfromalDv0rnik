import json


class Core:
    def __init__(self, name=None):
        self.__name = name
        self.__job_base = {
            "A": 5000,
            "B": 4000,
            "C": 3000,
            "D": 20
        }

    def base_reader(self):
        with open('Basejson/name-category.json', 'r') as file:
            names = json.load(file)
            for n in names:
                if n == self.__name:
                    return f"{n} have {self.__job_base.get(names.get(n))}$ salary"

    def base_writer(self, add_employee):
        add = {}
        with open("Basejson/name-category.json", "r") as file:
            file1 = json.load(file)
            add.update(file1)
            add.update(add_employee)

        with open("Basejson/name-category.json", "w") as file:
            json.dump(add, file, indent=1)
        return f"element {add_employee} was added"


