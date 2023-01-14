from Base_searcher.Core.data_base import Core


class Interface:
    def __init__(self, name=None):
        self.name = name

    def take_salary(self):
        return Core(self.name).base_reader()

    def add_in_base(self):
        return Core().base_writer(self.name)


