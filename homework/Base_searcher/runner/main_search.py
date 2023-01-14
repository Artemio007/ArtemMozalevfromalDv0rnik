from Base_searcher.Interface.interface_base import Interface


def main_search():
    search = Interface("Artem")
    print(search.take_salary())

    add = Interface({"Sasha": "C"})  # add dict("name":"A or B,C,D"
    print(add.add_in_base())


if __name__ == "__main__":
    main_search()


