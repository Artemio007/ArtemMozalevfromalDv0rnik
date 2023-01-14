import functools


@functools.total_ordering
class Number(int):

    def __eq__(self, num: int):
        return int(self) == int(num)

    def __lt__(self, num):
        return int(self) < int(num)


a = Number(5)
b = Number(6)
c = Number(7)
print(b > a > c)
print(b < a)
print(b == a)
print(b >= a)
print(b <= a)
print(b != a)



