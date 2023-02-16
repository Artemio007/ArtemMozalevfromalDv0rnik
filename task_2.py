import threading
import time

mark = True


def slp():
    global mark
    try:
        if mark:
            what = input("what to remind you? \n")
            when = int(input("after how much time(sec) \n"))
            mark = False
            w2.start()
            time.sleep(when)
            print(f"{when} seconds have passed, I remind you: {what}")
    except Exception as other:
        print(other)


def w_slp():
    global mark
    if not mark:
        while w1.is_alive():
            what = input("Enter the one word: \n")
            print("wait...")
            print(what[::-1])


w1 = threading.Thread(target=slp)
w2 = threading.Thread(target=w_slp)
w1.start()

try:
    w1.join()
    w2.join()
except RuntimeError as err:
    print(err)
except KeyboardInterrupt as err_:
    print(err_)

print("THE END")
