# Q6
# def find_largest(number_1, number_2):
#     if number_1>number_2:
#         return number_1
#     else:
#         return number_2

# result1 = find_largest(25, 40)
# print("Largest number:", result1)

# result2 = find_largest(63, 13)
# print("Largest number:", result2)

# Q7
# def celsius_to_fahrenheit(celsius):
#     F = (9/5)*celsius + 32
#     return F

# def fahrenheit_to_celsius(fahrenheit):
#     C = (5/9)*(fahrenheit - 32)
#     return C

# fahrenheit = celsius_to_fahrenheit(0)
# print(fahrenheit)

# celsius = fahrenheit_to_celsius(98.6)
# print(celsius)

# fahrenheit = celsius_to_fahrenheit(100)
# print(fahrenheit)

# celsius = fahrenheit_to_celsius(68)
# print(celsius)

# Q8
# def calculate_sum_1(a, b):
#     print(a + b)


# def calculate_sum_2(a, b):
#     return a + b

# calculate_sum_1(10, 20)
# calculate_sum_2(10, 20)
# res1 = calculate_sum_1(10, 20)
# res2 = calculate_sum_2(10, 20)
# print("Result from 1st function:",res1)
# print("Result from 2nd function:",res2)

# 2nd function returns a value

# As function does not have a return value so python automatically returns None

# No this is not possible in python the print() does not directly stores any return value.

# Q9
# def calculate_result(mark_1, mark_2, mark_3, mark_4, mark_5):
#     total = mark_1+mark_2+mark_3+mark_4+mark_5
#     avg = total/5
#     return total, avg

# total, percentage = calculate_result(75, 80, 65, 90, 70)
# print("Total marks:", total)
# print(f"Average Marks: {percentage}%")

# total, percentage = calculate_result(76, 83, 75, 30, 50)
# print("Total marks:", total)
# print(f"Average Marks: {percentage}%")

# Q10
# def rectangle_details(length, breadth):
#     area = length*breadth
#     perimeter = 2*(length+breadth)
#     return area, perimeter

# area, perimeter = rectangle_details(10, 5)
# print("Area:",area)
# print("Perimeter:",perimeter)

# area, perimeter = rectangle_details(6, 50)
# print("Area:",area)
# print("Perimeter:",perimeter)