
class EvenRange:
    def __init__(self, first: int, last: int):
        self.first = first
        self.last = last
        self.iter_counter = self.first

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter_counter > self.last:
            print("Out of numbers!")
            raise StopIteration

        elif self.iter_counter % 2 == 0:
            print(self.iter_counter)
        self.iter_counter += 1


e = EvenRange(1, 12)
for i in e:
    i
