from tasks_clases.Task import *
import Database

def OfficeTask(Task):
    def __init__(self, task_id, status, task_type, employees_id, folder, file, involvement):
        super().__init__(task_id, status, task_type, employees_id)
        self.__folder = folder
        self.__file = file
        self.__involvement = involvement

        def complete_task(self, security_code):
            pass

        def get_description(self):
            return f"{self.__folder} -> {self.__file} ({self.__involvement})"
