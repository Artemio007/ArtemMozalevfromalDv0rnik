from time import sleep
from art import tprint


def geo(first, second):
    return round((first * second) ** 0.5, 3)


try:
    print(geo(float(input()), float(input())))

except Exception as ex:
    print(ex)


try:
    lambda_ = lambda x, y: (x * y) ** 0.5
    print(lambda_("gffh", "fgfdg"))

except TypeError as err:
    print(err)

except Exception as err_:
    print(err_)

finally:
    print("...Pending")
    sleep(5)
    tprint("The end")
