from employee_classes.Manager import *


class Head(Manager):
    def __init__(self, first_name, last_name, id_number, employee_id, manager_id, role):
        super().__init__(first_name, last_name, id_number, employee_id, manager_id, role)

    def add_new_employee(self, first_name, last_name, id_number, manager_id, role):
        if first_name == "" or last_name == "" or id_number == "" or manager_id == "" or role == "":
            return EMPTY_FIELDS_ERROR
        manager = Database.is_manager_by_employees_id(manager_id)
        if not manager:
            return MANAGERS_ID_DOESNT_EXIST_ERROR
        if role != "m" and role != "e":
            return WRONG_FORMAT_ERROR

        employee = Database.add_new_employee_to_database(first_name, last_name, id_number, manager_id, role)
        if employee is None:
            return WRONG_FORMAT_ERROR
        if self.get_employees_id() == manager_id:
            self._list_of_employees.append(employee)
        return "done"