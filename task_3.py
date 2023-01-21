
generator = (i for i in range(int(0x16345785d8a0000)) if i % 2 != 0)
# print(generator)
# print(next(generator))
# print(generator.__next__())
# for i in generator:
#     print(i)


def gener(x):
    i = -1
    while x:
        i += 2
        yield i


s = gener(True)
# print(s)
# print(next(s))
#
# for i in s:
#     print(i)

