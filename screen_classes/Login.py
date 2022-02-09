from employee_classes.Head import *
import Database
from constants import *


def check_login_details(username, password):
    if username == "" or password == "":
        return EMPTY_FIELDS_ERROR

    if len(username) != 10:
        return WRONG_USERNAME_OR_PASSWORD_ERROR
    employee = Database.get_employee_by_employees_id(username[:4])
    if employee is None:
        return WRONG_USERNAME_OR_PASSWORD_ERROR ;
    if employee[4] != username[4:8]:
        return WRONG_USERNAME_OR_PASSWORD_ERROR

    username_numbers_sum = 0
    for char in username:
        if char.isnumeric():
            username_numbers_sum += int(char)

    if username_numbers_sum % 10 != 0:
        return WRONG_USERNAME_OR_PASSWORD_ERROR

    password_numbers_sum = 0
    for char in password:
        password_numbers_sum += int(char)

    if password_numbers_sum != username_numbers_sum:
        return WRONG_USERNAME_OR_PASSWORD_ERROR

    if employee[5] == 'e':
        return Employee(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5])
    if employee[5] == 'm':
        return Manager(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5])
    if employee[5] == 'h':
        return Head(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5])