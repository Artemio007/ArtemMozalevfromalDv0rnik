import csv


def dict_reader():
    with open("datacsv/task_2.csv", "r") as file:
        quoting = csv.QUOTE_MINIMAL
        reader = csv.DictReader(file, fieldnames=["QuotaAmount", "StartDate", "OwnerName", "Username"], quoting=quoting)
        for i in reader:
            print(i)

dict_reader()