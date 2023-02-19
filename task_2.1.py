import threading
from threading import Thread
import time

work = True
cond = threading.Condition()


def slp():
    global work
    if work:
        try:
            what = input("what to remind you?")
            when = int(input("after how much time(sec)"))
            work = False
            with cond:
                w_slp()
                cond.wait(when)
                print(f"{when} seconds have passed, I remind you: {what}")
        except Exception as err:
            print(err)


def w_slp():
    if not work:
        what = input("Enter the one word: ")
        print("wait...")
        time.sleep(1)
        print(what[::-1])
        cond.notify()


worker_1 = Thread(target=w_slp)
worker_1.start()
slp()

print("work stoped")
work = False