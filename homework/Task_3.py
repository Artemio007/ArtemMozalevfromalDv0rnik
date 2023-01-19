
def bzz(num):
    try:
        bar(num)
    except ZeroDivisionError as err_0:
        print(err_0)
    finally:
        print("bzz turned on the bar ")


def bar(num):
    try:
        foo(num)
    except ZeroDivisionError as err_0:
        print(err_0)
    except IndexError as err_i:
        print(err_i)
    finally:
        print("bar turned on the foo")


def foo(num):
    my_list = [1, 2, 3]
    div = 5 / num
    index = my_list[num]
    print(div, num, index)


def main(number):
    print("main working...")
    try:
        bzz(number)
    except IndexError as err_i1:
        print(err_i1)
    except TypeError as err_t:
        print(err_t)


if __name__ == '__main__':
    main("xdg")