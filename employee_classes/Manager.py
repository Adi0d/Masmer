from employee_classes.Employee import *
from tasks_clases.Task import *


class Manager(Employee):
    def __init__(self, first_name, last_name, id_number, employee_id, manager_id, role):
        super().__init__(first_name, last_name, id_number, employee_id, manager_id, role)