import csv


class DialectClass(csv.Dialect):
    quoting = csv.QUOTE_MINIMAL
    delimiter = "]"
    lineterminator = "\n"
    quotechar = "*"
    escapechar="-"
    doublequote="//"
    skipinitialspace=True


csv.register_dialect("mydialect", dialect=DialectClass)

path = "datacsv/task_2.csv"
path_2 = "datacsv/task_2_new_writer.csv"


def sniffer(path_):
    with open(path_, "r") as file:
        context = file.read()
        dialect = csv.Sniffer().sniff(context)
        print(f"delimiter: {dialect.delimiter},qutechar: {dialect.quotechar},quoting: {dialect.quoting},"
              f"lineterminator: {dialect.lineterminator}, "
              f"escapechar: {dialect.escapechar}, skipinitialspace: {dialect.skipinitialspace}, doublequote: {dialect.doublequote}")


def new():
    with open("datacsv/task_2.csv", "r") as file:
        reader_ = csv.reader(file)
        for i in reader_:
            print(*i)


def reader_writer():
    with open("datacsv/task_2_new_writer.csv", "w") as file:
        writer_d = csv.writer(file, dialect=DialectClass)
        writer_d.writerow(["150000", "2016-01-01", "Chris Riley", "trailhead9.ub20k5i9t8ou@example.com"])
        writer_d.writerow(["150000", "2016-01-01", "Chris Riley", "trailhead9.ub20k5i9t8ou@example.com"])
        writer_d.writerow(["150000", "2016-01-01", "Chris Riley", "trailhead9.ub20k5i9t8ou@example.com"])
        writer_d.writerow(["150000", "2016-01-01", "Chris Riley", "trailhead9.ub20k5i9t8ou@example.com"])


def dict_writer():
    with open("datacsv/task_2_new_writer.csv", "w") as file:
        quoting = csv.QUOTE_MINIMAL
        writer = csv.DictWriter(file,
                                fieldnames=["name", "email"],
                                # quoting=quoting,
                                # lineterminator="\n"
                                dialect=DialectClass

                                )
        writer.writeheader()
        writer.writerow({"name": "Chris Riley", "email": "trailhead9.ub20k5i9t8ou@example.com"})
        writer.writerow({"name": "Harold Campbell", "email": "trailhead14.jibpbwvuy67t@example.com"})
        writer.writerow({"name": "Jessica Nichols", "email": "trailhead19.d1fxj2goytkp@example.com"})
        writer.writerow({"name": "Catherine Brown", "email": "trailhead16.kojyepokybge@example.com"})
        writer.writerow({"name": "Kelly Frazier", "email": "trailhead7.zdcsy4ax10mr@example.com"})
        writer.writerow({"name": "Dennis Howard", "email": "trailhead4.wfokpckfroxp@example.com"})


def dict_reader(path_):
    with open(path_, "r") as file:
        quoting = csv.QUOTE_MINIMAL
        reader = csv.DictReader(file, fieldnames=["QuotaAmount", "StartDate", "OwnerName", "Username"], quoting=quoting)
        for i in reader:
            print(i)


dict_writer()
sniffer(path_2)