from tasks_clases.Task import *
import Database


class FieldTask(Task):
    def __init__(self, task_id, status, task_type, employees_id, country, city, target):
        super().__init__(task_id, status, task_type, employees_id)
        self.__country = country
        self.__city = city
        self.__target = target

    def complete_task(self, security_code):
        pass

    def get_description(self):
        return f"{self.__country}: {self.__city} [{self.__target}]"