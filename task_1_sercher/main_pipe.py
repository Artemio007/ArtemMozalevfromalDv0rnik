import multiprocessing
import os.path
import time

path_ = "file_home/fileWOW_.txt"


def find_file(path: str, conn):
    print(f"proc id {os.getpid()} get started")
    if os.path.exists(path):
        file = open(path, "r")
        if "Wow!" in file.read():
            file.close()
            print("file closed")
            conn.send(True)
            conn.close()
        else:
            print("line not found. im gonna sleep 5 sec.")
            file.close()
            time.sleep(5)
            find_file(path, conn)
    elif not os.path.exists(path):
        print("file not exist, im gonna sleep 5 sec.")
        time.sleep(5)
        find_file(path, conn)


def remove_file(path, conn):
    print(f"proc id {os.getpid()} wait find_file")
    conn.recv()
    print(f"now i will delete file: \n{path}")
    os.remove(path)


if __name__ == "__main__":
    parent, child = multiprocessing.Pipe()
    process_0 = multiprocessing.Process(target=find_file, args=(path_, child,), name="finder")
    process_1 = multiprocessing.Process(target=remove_file, args=(path_, parent,), name="remover")
    process_1.start()
    process_0.start()