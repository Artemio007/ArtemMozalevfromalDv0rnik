import multiprocessing
import os.path
import time

path_ = "file_home/fileWOW.txt"


def find_file(path: str, event_):
    print(f"proc id {os.getpid()} get started")
    try:
        if os.path.exists(path):
            file = open(path, "r")
            if "Wow!" in file.read():
                file.close()
                print("file closed")
                event_.set()
            else:
                print("line not found. im gonna sleep 5 sec.")
                file.close()
                time.sleep(5)
                find_file(path, event_)
        elif not os.path.exists(path):
            print("file not exist, im gonna sleep 5 sec.")
            time.sleep(5)
            find_file(path, event_)
    except Exception as err:
        print(err)
        time.sleep(10)
        find_file(path, event_)


def remove_file(path, event_):

    print(f"proc id {os.getpid()} wait find_file")
    event_.wait()
    print(f"now i will delete file: \n{path}")
    os.remove(path)


if __name__ == "__main__":
    event = multiprocessing.Event()
    process_0 = multiprocessing.Process(target=find_file, args=(path_, event,), name="finder")
    process_1 = multiprocessing.Process(target=remove_file, args=(path_, event,), name="remover")
    process_1.start()
    process_0.start()