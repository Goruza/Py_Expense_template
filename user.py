from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    },
]


def chose_user(*args):
    with open("users.csv", mode="r") as file:
        reader = csv.reader(file)
        users = []
        for row in reader:
            users.append(row[0])
    return users


def add_user(*args):
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    toSave = [infos["name"]]
    with open("users.csv", mode="a", newline="")as file:
        writer = csv.writer(file)
        writer.writerow(toSave)
    print("A new user has been created !")
    return True