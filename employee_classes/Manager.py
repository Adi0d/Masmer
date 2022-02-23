from employee_classes.Employee import *
from tasks_clases.Task import *


class Manager(Employee):
    def __init__(self, first_name, last_name, id_number, employee_id, manager_id, role):
        super().__init__(first_name, last_name, id_number, employee_id, manager_id, role)
        self._list_of_employees = Database.get_list_of_employees(employee_id)

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
