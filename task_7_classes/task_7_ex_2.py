class Employee:
    def __init__(self, name: str, salary: int):
        self._name = name
        self._salary = salary
        self._bonus = 0

    @property
    def name(self):
        """name`s property"""
        return self.name

    @property
    def salary(self):
        """salary`s property"""
        return self.salary

    @property
    def bonus(self):
        return self.bonus

    @name.setter
    def name(self, name: str):
        self._name = name

    @salary.setter
    def salary(self, salary: int):
        self._salary = salary

    @bonus.setter
    def bonus(self, bonus: int):
        self._bonus = bonus

    @name.getter
    def name(self):
        return self._name

    @salary.getter
    def salary(self):
        return self._salary

    @bonus.getter
    def bonus(self):
        return self._bonus

    def to_pay(self):
        """
        Method returning the value of summarized salary and bonus
        :return: the value of summarized salary and bonus
        """
        return self.salary + self.bonus


class SalesPerson(Employee):
    def __init__(self, name: str, salary: int, percent: int):
        super().__init__(name, salary)
        self._percent = percent

    @property
    def bonus(self):
        """bonus`s property"""
        return self.bonus

    @bonus.setter
    def bonus(self, bonus: int):
        self._bonus = bonus

    @bonus.getter
    def bonus(self):
        if 100 <= self._percent < 200:
            return self._bonus * 2
        if self._percent >= 200:
            return self._bonus * 3


class Manager(Employee):
    def __init__(self, name: str, salary: int, client_number: int):
        super().__init__(name, salary)
        self._client_number = client_number

    @property
    def bonus(self):
        """bonus`s property"""
        return self.bonus

    @bonus.setter
    def bonus(self, bonus: int):
        self._bonus = bonus

    @bonus.getter
    def bonus(self):
        if self._client_number >= 100:
            return self._bonus + 500
        if self._client_number >= 150:
            return self._bonus + 1000


class Company:
    __employees = []

    def __init__(self, *args, n=0):
        """
        Initializes an instance of Company
        :param args: the list of employees
        :param n: length of the list
        """
        self.__employees = [*args]

    def give_everybody_bonus(self, company_bonus: int):
        """
        Method setting the amount of basic bonus for each employee.
        :param company_bonus: bonus to add to all employees
        :return: None
        """
        for member in self.__employees:
            member._bonus = company_bonus

    def total_to_pay(self):
        """
        Method returning total amount of salary of all employees including awarded bonus
        :return: total
        """
        total = 0
        for member in self.__employees:
            total += member.to_pay()
        return total

    def name_max_salary(self) -> str:
        """
        Method returning name of the employee, who received maximum salary including bonus.
        :return: member.name 
        """
        max_salary = 0
        for member in self.__employees:
            if max_salary < member.to_pay():
                max_salary = member.to_pay()
        for member in self.__employees:
            if max_salary == member.to_pay():
                return member.name


Sam = Employee('Sam', 1000)
Jim = SalesPerson('Jim', 4000, 200)
Mai = Manager('May', 3000, 104)
apple = Company(Sam, Jim, Mai)
apple.give_everybody_bonus(100)
print(Sam.to_pay(), Jim.to_pay(), Mai.to_pay())
print(apple.name_max_salary())
print(apple.total_to_pay())
