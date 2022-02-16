from tasks_clases.Task import *
import Database


class FieldTask(Task):
    def __init__(self, task_id, status, task_type, employees_id, country, city, target):
        super().__init__(task_id, status, task_type, employees_id)
        self.__country = country
        self.__city = city
        self.__target = target

    def complete_task(self, security_code):
        ans = False
        if len(security_code) != 5:
            return ans
        if security_code[0] != self.__country[0] or security_code[1] != self.__country(len(self.__country) - 1):
            return ans
        if security_code[2] != self.__city[0] or security_code[3] != self.__city[len(self.__city) - 1]:
            return ans
        if security_code[4] == 1 and self.__target == "enemy":
            ans = True
        elif security_code[5] == 2 and self.__target == "mossad member":
            ans = True

        if ans:
            Database.update_tasks_status(self._task_id)
            self._status = "v"
            return True
        return False


    def get_description(self):
        return f"{self.__country}: {self.__city} [{self.__target}]"