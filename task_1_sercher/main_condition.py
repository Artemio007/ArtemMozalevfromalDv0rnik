import multiprocessing
import os.path
import time

path_ = "file_home/WOW.txt"


def find_file(path: str, con_):
    print(f"proc id {os.getpid()} get started")
    try:
        if os.path.exists(path):
            file = open(path, "r")
            if "Wow!" in file.read():
                file.close()
                print("file closed")
                with con_:
                    con_.notify()
            else:
                print("line not found. im gonna sleep 5 sec.")
                file.close()
                time.sleep(5)
                find_file(path, con_)
        elif not os.path.exists(path):
            print("file not exist, im gonna sleep 5 sec.")
            time.sleep(5)
            find_file(path, con_)
    except Exception as err:
        print(err)
        time.sleep(10)
        find_file(path, con_)


def remove_file(path, con_):

    print(f"proc id {os.getpid()} wait find_file")
    with con_:
        con_.wait()
    print(f"now i will delete file: \n{path}")
    os.remove(path)


if __name__ == "__main__":
    con = multiprocessing.Condition()
    process_0 = multiprocessing.Process(target=find_file, args=(path_, con,), name="finder")
    process_1 = multiprocessing.Process(target=remove_file, args=(path_, con,), name="remover")
    process_1.start()
    process_0.start()