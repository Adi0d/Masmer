from employee_classes.Manager import *


class Head(Manager):
    def __init__(self, first_name, last_name, id_number, employee_id, manager_id, role):
        super().__init__(self, first_name, last_name, id_number, employee_id, manager_id, role)