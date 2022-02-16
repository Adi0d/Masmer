from abc import abstractmethod


class Task:
    def __init__(self, task_id, status, task_type, employees_id):
        self._task_id = task_id
        self._status = status
        self._task_type = task_type
        self._employees_id = employees_id

    # @abstractmethod
    # def complete_task(self, security_code):
    #     pass

    @abstractmethod
    def get_description(self):
        pass

    def get_task_id(self):
        return self._task_id

    def get_task_type(self):
        return self._task_type

    def get_status(self):
        return self.get_status()