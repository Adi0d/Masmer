import Database
from constants import *


class Employee:
    def __init__(self, first_name, last_name, id_number, employee_id, manager_id, role):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__id_number = id_number
        self._employee_id = employee_id
        self._manager_id = manager_id
        self._role = role
        self._list_of_tasks = Database.get_list_of_tasks_from_database(employee_id)

    # Getters
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_id_number(self):
        return self.__id_number

    def get_employees_id(self):
        return self._employee_id

    def get_manager_id(self):
        return self._manager_id

    def get_role(self):
        return self._role

    def get_list_of_tasks(self):
        return self._list_of_tasks

    def complete_employees_task(self, task_id, security_id):
        if task_id == "" or security_id == "":
            return EMPTY_FIELDS_ERROR
        is_one_correct = False
        for task in self._list_of_tasks:
            if task.get_task_id() == task_id:
                is_one_correct = True
                if task.complete_task():
                    return "done"
        if not is_one_correct:
            return INCORRECT_SECURITY_KEY_ERROR
        return TASK_DOESNT_EXIST_ERROR