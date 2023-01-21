
def show_letters(some_str: str):
    st = ""
    for i in some_str:
        if i.isalpha():
            st += i
            yield i
    print(st)


a = show_letters("dfg.dfgm.gfh''''h h g")
# print(next(a))
# print(next(a))
# print(next(a))
# for i in a:
#     print(i)

generator = (print(i) for i in input("введи набор символов: ") if i.isalpha())
# print(generator)
# next(generator)
