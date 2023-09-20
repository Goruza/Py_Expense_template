from PyInquirer import prompt
from user import chose_user
import csv


possible_usernames = chose_user()
possible_users = [
    {
    'name': user,
    'value': user,
    'checked': True,
    }
    for user in possible_usernames
]
expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": chose_user()
    },
    {
        "type":"checkbox",
        "name":"involved_users",
        "message":"New Expense - Involved Users",
        "choices": possible_users,
    },
]


def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    toSave = [infos["amount"], infos["label"], infos["spender"], infos["involved_users"]]
    with open("expense_report.csv", mode="a", newline="")as file:
        writer = csv.writer(file)
        writer.writerow(toSave)
    print("A new expense has been created !")
    return True


