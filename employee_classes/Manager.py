from employee_classes.Employee import *
from tasks_clases.Task import *


class Manager(Employee):
    def __init__(self, first_name, last_name, id_number, employee_id, manager_id, role):
        super().__init__(first_name, last_name, id_number, employee_id, manager_id, role)
        self._list_of_employees = Database.get_list_of_employees(employee_id)

    def add_new_employee_task(self, employee_id, task_type, description):
        if task_type == "" or description == "":
            return EMPTY_FIELDS_ERROR
        if task_type not in ["o", "f"]:
            return TASK_TYPE_DOESNT_FIT_ERROR
        if employee_id == "":
            if self.get_role() == "h" and task_type == "f":
                return TASK_TYPE_DOESNT_FIT_ERROR
            employee_id = self.get_employees_id()
        else:
            add = False
            for employee in self._list_of_employees:
                if self.get_employees_id() == employee_id:
                    add = True
                    break
            if not add:
                return EMPLOYEES_ID_DOESNT_EXIST_ERROR
            if task_type == "o":
                return TASK_TYPE_DOESNT_FIT_ERROR
        ans = Database.add_new_task_to_database(employee_id, task_type, description)
        if ans != "":
            if self.get_employees_id() == employee_id:
                self._list_of_tasks.append([ans])
            return "done"
        else:
            return WRONG_FORMAT_ERROR



    def delete_employees_task(self, employees_id, task_id):
        if task_id == "":
            return EMPTY_FIELDS_ERROR
        if employees_id == "":
            employees_id = self.get_employees_id()
            ans = Database.delete_task_from_database(employees_id, task_id)
            if ans:
                tasks = Database.get_list_of_tasks_from_database(employees_id)
                for task in tasks:
                    if task.get_task_id() == task_id:
                        tasks.remove(task)
                        break
                return "done"
            else:
                return TASK_DOESNT_EXIST_ERROR
        for employee in self._list_of_employees:
            if employee.get_employees_id() == employees_id:
                ans = Database.get_list_of_tasks_from_database(employees_id)
                if ans:
                    return "done"
                return TASK_DOESNT_EXIST_ERROR
