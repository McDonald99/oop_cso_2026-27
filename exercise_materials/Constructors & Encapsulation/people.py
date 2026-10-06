class Person:
    def display(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Left-handed: {self.is_left}")

    def __init__(self, first_name, last_name, age, is_left):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.is_left = is_left


class Employee:
    def __init__(self, em_id, first_name="", last_name="", salary=0, job_title=""):
        self.first_name = first_name
        self.last_name = last_name
        self.em_id = em_id
        self._salary = salary
        self.job_title = job_title

    def get_salary(self):
        return self._salary

    def display(self):
        print(f"Employee [id: {self.em_id}, first name: {self.first_name}, last name: {self.last_name}, salary: {self._salary}")

    def calc_net_pay(self):
        tax = self._salary*0.42
        take_home = self._salary-tax
        monthly = take_home/12
        return monthly

    def calc_bonus(self):
        if "manager" in self.job_title.lower():
            bonus = self._salary*0.15
        elif "intern" in self.job_title.lower():
            bonus = self._salary*0.02
        else:
            bonus = self._salary*0.06
        return bonus



if __name__ == "__main__":

    # f_name = input("Please enter your first name: ")
    # l_name = input("Please enter your last name: ")
    # age = input("Please enter your age: ")
    # is_left = input("If you are left handed, enter 'True', otherwise enter 'False': ")
    #
    # p1 = Person(f_name, l_name, age, is_left)
    # p1.display()

    emp_id = input("Please enter your id: ")
    f_name = input("Please enter your first name: ")
    l_name = input("Please enter your last name: ")
    emp_salary = int(input("Please enter your salary: "))
    title = input("Please enter your job title: ")

    emp = Employee(emp_id, f_name, l_name, emp_salary, title)
    emp.display()
