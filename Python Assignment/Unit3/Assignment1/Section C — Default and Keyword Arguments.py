# Q11
# def greet_user(name, message="Welcome to Python!"):
#     print("Hello",name+"!")
#     print(message)

# greet_user("Rahul", "Good Morning!")
# greet_user("Aman", message="Keep Learning!")
# greet_user("Priya")

# Q12
# def calculate_electricity_bill(units, rate=7):
#     bill = units*rate
#     return bill

# bill_1 = calculate_electricity_bill(100)
# bill_2 = calculate_electricity_bill(100, 8)
# bill_3 = calculate_electricity_bill(rate=6, units=100)

# print(bill_1)
# print(bill_2)
# print(bill_3)

# Q13
def calculate_salary(basic_salary, bonus=2000, deduction=500):
    final_salary = basic_salary + bonus - deduction
    print(final_salary)

calculate_salary(25000)
calculate_salary(25000, 3000)
calculate_salary(25000, 3000, 1000)
calculate_salary(basic_salary=25000, deduction=800, bonus=4000)
calculate_salary(basic_salary=90000,deduction=4200)