import json

name_job = {
    "John": "Engineer",
    "Oliver": "Teacher",
    "Jack": "Sportsman",
    "Harry": "Doctor",
    "Jacob": "Actor",
    "Charley": "Cosmonaut",
    "Thomas": "Fireman",
    "George": "Veterinarian",
    "Oscar": "Pilot"
}

name_1 = {
    "John": "1",
    "Oliver": "2",
    "Jack": "3",
    "Harry": "4",
    "Jacob": "5",
    "Charley": "6",
    "Thomas": "7",
    "George": "8",
    "Oscar": "9"
}


def dump1(x: dict) -> json:
    with open(r"jsonfile\task_1.json", "w") as file_1:
        print("dump_1 is ready")
        json.dump(x, file_1)


def dump_2(y: dict) -> json:
    print("dump_2 is ready")
    with open(r"jsonfile\task_2.json", "a") as file_2:
        json.dump(y, file_2)


dump1(name_job)
dump_2(name_1)