from tasks_clases.Task import *
import Database


class OfficeTask(Task):
    def __init__(self, task_id, status, task_type, employees_id, folder, file, involvement):
        super().__init__(task_id, status, task_type, employees_id)
        self.__folder = folder
        self.__file = file
        self.__involvement = involvement

    def complete_task(self, security_code):
        flag = False
        if len(security_code) != 3:
            return False

        if security_code[0] == self.__folder[0] and security_code[1] == self.__file[0]:
            if security_code[2].isnumeric():
                if security_code[2] % 2 == 0 and self.__involvement == "yes":
                    flag = True
                elif security_code[2] % 2 == 1 and self.__involvement == "no":
                    flag = True

        if flag:
            Database.update_tasks_status(self._task_id)
            self._status = "v"
            return True
        return False

    def get_description(self):
        return f"{self.__folder} -> {self.__file} ({self.__involvement})"
