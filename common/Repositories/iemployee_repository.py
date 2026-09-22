from abc import ABC, abstractmethod
from common.Entities.employee import Employee


class IEmployeeRepository(ABC):
    @abstractmethod
    def get_employee_by_username_password(self, username: str, password: str) -> Employee:
        pass

    @abstractmethod
    def inset(self, employee: Employee):
        pass
