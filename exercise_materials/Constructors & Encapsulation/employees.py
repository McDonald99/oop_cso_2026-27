from people import Employee


def highest_bonus(dictionary):
    max_bonus = 0
    for value in dictionary.values():
        bonus = value.calc_bonus()
        if bonus < max_bonus:
            max_bonus = bonus
    return max_bonus

employees = {}

for emp in range(2):
    emp_id = input("Please enter your id: ")
    while True:
        if emp_id in employees:
            emp_id = input("Please enter another id: ")

        else:
            f_name = input("Please enter your first name: ")
            l_name = input("Please enter your last name: ")
            emp_salary = int(input("Please enter your salary: "))
            title = input("Please enter your job title: ")

            employee = Employee(emp_id, f_name, l_name, emp_salary, title)
            # emp = employee.display()
            employees[emp_id] = employee
            break

max_bonus = highest_bonus(employees)
print(max_bonus)