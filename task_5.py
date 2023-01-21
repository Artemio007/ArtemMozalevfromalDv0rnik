from time import sleep


def fib_gener():
    first = second = 1
    while True:
        first, second = second, first + second
        yield second


generator = fib_gener()
print(generator)
print(next(generator))
print(next(generator))

for i in generator:
    print(i)
    sleep(1)



