list_of_employee_happiness = [int(element) for element in input().split(" ")]
happiness_improvement_factor = int(input())
list_of_employee_happiness_after_factoring = [el * happiness_improvement_factor for el in list_of_employee_happiness]
happy_employees = [happy_level for happy_level in list_of_employee_happiness if happy_level > sum(list_of_employee_happiness)\
                   / len(list_of_employee_happiness)]
print(f"Score: {len(happy_employees)}/{len(list_of_employee_happiness)}.", end=" ")
print("".join(["Employees are happy!" if len(happy_employees) > \
           len(list_of_employee_happiness)/2 else "Employees are not happy!"]))