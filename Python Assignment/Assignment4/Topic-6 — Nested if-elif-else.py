# Q44
# A = int(input("No. 1:"))
# B = int(input("No. 2:"))
# C = int(input("No. 3:"))
# if A < B and B >= C:
#     if B == C:
#         print("B and C are equal and Greatest")
#     else:
#         print("B is Greatest")
# elif B <= A and A > C:
#     if A == B:
#         print("A and B are equal and Greatest")
#     else:
#         print("A is Greatest")
# elif A <= C and C > B:
#     if A == C:
#         print("A and C are equal and Greatest")
#     else:
#         print("C is Greatest")
# else:
#     print("All are equal")

''' Alernate '''
# if A >= B:
#     if A >= C:
#         if A == B and A == C:
#             print("All are equal")
#         elif A == B:
#             print("A and B are equal and Greatest")
#         elif A == C:
#             print("A and C are equal and Greatest")
#         else:
#             print("A is Greatest")
#     else:
#         print("C is Greatest")
# else:
#     if B >= C:
#         if B == C:
#             print("B and C are equal and Greatest")
#         else:
#             print("B is Greatest")
#     else:
#         print("C is greatest")

# Q45
# marks = int(input("Enter marks:"))
# attend = int(input("Enter Attendance:"))
# if attend >= 75:
#     if marks >= 90:
#         print("Grade A")
#     elif marks >= 75:
#         print("Grade B")
#     elif marks >= 60:
#         print("Grade C")
#     elif marks >= 40:
#         print("Grade D")
#     else:
#         print("Grade F")
# else:
#     print("Not Eligible")

# Q46
# salary = int(input("Enter your salary:"))
# rate = int(input("Your performance rating:"))
# if salary >= 30000:
#     if rate == 5:
#         print("Bonus: 20%")
#     elif rate == 4:
#         print("Bonus: 15%")
#     elif rate == 3:
#         print("Bonus: 10%")
#     else:
#         print("Bonus: 5%")
# else:
#     print("Not Eligible for Bonus")

# Q47
# age = int(input("Enter your age:"))
# dist = int(input("Enter distance:"))
# if age < 5:
#     print("Free")
# elif 5 <= age <= 59:
#     if dist < 10:
#         print("Regular - Short Distance")
#     else:
#         print("Regular - Long Distance")
# else:
#     print("Senior")

# Q48
# stock = int(input("Stock status:"))
# pay = input("Payment status:")
# if stock >= 0:
#     if pay == "paid":
#         print("Order confirmed")
#     elif pay == "pending":
#         print("Payment Pending")
#     else:
#         print("Invalid Payment Status")
# else:
#     print("Out of Stock")

# Q49
# age = int(input("Enter age:"))
# tkt = input("Ticket type:")
# if age < 5:
#     print("Free Travel")
# elif 5 <= age <=59:
#     if tkt == "AC":
#         print("AC Ticket")
#     elif tkt == "Sleeper":
#         print("Sleeper Ticket")
#     else:
#         print("Invalid Ticket Type")
# else:
#     print("Senior Passenger")
