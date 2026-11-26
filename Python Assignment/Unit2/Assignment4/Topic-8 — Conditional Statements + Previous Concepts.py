# Q58
# student_id = input("Enter your ID:").split("-")
# degree, batch, branch, roll_no = student_id
# if branch == "CSE":
#     print("CSE Student")
# else:
#     print("Non CSE student")

# Q59
# email = input("Enter Your Email ID:").split("@")
# user, domain = email
# match domain:
#     case "gmail.com":
#         print("Gmail User")
#     case _:
#         print("Other Email Provider")

# Q60
# name = input("Full name(3 word):").split()
# first, middle, last = name
# user = first + last
# print(user)
# if "." in user:
#     print("Valid Username Format")
# else:
#     print("Invalid Username Format")

# name = input("Full name(3 word):").split()
# first, middle, last = name
# user = first + "." + last
# print(user)
# if "." in user:
#     print("Valid Username Format")
# else:
#     print("Invalid Username Format")

# Q61
# num = int(input("Enter a positive no.:"))
# if num < 10:
#     print("One Digit")
# elif num < 100:
#     print("Two Digit")
# elif num < 1000:
#     print("Three Digit")
# else:
#     print("Four or more digit")

# Q62
# price = int(input("Enter price:"))
# qun = int(input("Enter Quantity:"))
# subtotal = price * qun
# if subtotal >= 5000:
#     discount = (subtotal*20)/100
#     final = subtotal - discount
#     print(f"Subtotal: {subtotal}, Discount: 20%, Final: {final}")
# elif subtotal >= 2000:
#     discount = (subtotal*10)/100
#     final = subtotal - discount
#     print(f"Subtotal: {subtotal}, Discount: 10%, Final: {final}")
# else:
#     print(f"Subtotal: {subtotal}, Discount: No Discount, Final: {subtotal}")

# Q63
# unit = int(input("Enter electricity units consumed:"))
# if unit <= 100:
#     print("Units:",unit)
#     rate = 5
#     print("Rate: ₹",rate,"per unit")
#     bill = unit * rate
#     print("Bill: ₹",bill)
# elif unit <= 300:
#     print("Units:",unit)
#     rate = 7
#     print("Rate: ₹",rate,"per unit")
#     bill = unit * rate
#     print("Bill: ₹",bill)
# elif unit > 300:
#     print("Units:",unit)
#     rate = 10
#     print("Rate: ₹",rate,"per unit")
#     bill = unit * rate
#     print("Bill: ₹",bill)

# Q64
# print('''1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit''')

# balance = 10000

# choice = int(input("Your choice:"))
# match choice:
#     case 1:
#         print("Check Balance")
#     case 2:
#         print("Deposit")
#     case 3:
#         print("Withdraw")
#         withdraw_amt = int(input("Enter withdraw amount:"))
#         if withdraw_amt <= balance:
#             print("Rs.",withdraw_amt,"Withdrawn")
#             bal = balance - withdraw_amt
#             print("Remaining Balance:",bal)
#         else:
#             print("Insufficient Balance")
#     case 4:
#         print("Exit")
#     case _:
#         print("Invalid Choice")

# Q65
# print('''1 → Pizza → ₹250
# 2 → Burger → ₹150
# 3 → Pasta → ₹200
# 4 → Sandwich → ₹120''')
# meal_no = int(input("Enter meal no. you want:"))
# qun = int(input("Enter quantity:"))

# match meal_no:
#     case 1:
#         total = 250 * qun
#         if total >= 500:
#             dis = (total * 10)/100
#             final = total - dis
#             print(f"Total: {total}, Discount: {dis}, Final: {final}")
#         else:
#             print(f"Total: {total}, Discount: 0.00, Final: {total}")
#     case 2:
#         total = 250 * qun
#         if total >= 500:
#             dis = (total * 10)/100
#             final = total - dis
#             print(f"Total: {total}, Discount: {dis}, Final: {final}")
#         else:
#             print(f"Total: {total}, Discount: 0.00, Final: {total}")
#     case 3:
#         total = 250 * qun
#         if total >= 500:
#             dis = (total * 10)/100
#             final = total - dis
#             print(f"Total: {total}, Discount: {dis}, Final: {final}")
#         else:
#             print(f"Total: {total}, Discount: 0.00, Final: {total}")
#     case 4:
#         total = 250 * qun
#         if total >= 500:
#             dis = (total * 10)/100
#             final = total - dis
#             print(f"Total: {total}, Discount: {dis}, Final: {final}")
#         else:
#             print(f"Total: {total}, Discount: 0.00, Final: {total}")
#     case _:
#         print("Not Available")

# Q66
# py = int(input("Marks of Python:"))
# git = int(input("Marks of Git & Github:"))
# js = int(input("Marks of JavaScript:"))

# attend = int(input("Enter your attendance:"))

# total = py + git + js
# avg = total / 3

# if attend >= 75:
#     if avg >= 90:
#         print("Outstanding")
#     elif avg >= 75:
#         print("Very Good")
#     elif avg >= 60:
#         print("Good")
#     elif avg >= 40:
#         print("Pass")
#     else:
#         print("Fail")
# else:
#     print("Not Eligible")

# Q67
# dist = int(input("Distance:"))
# ride = input("Ride type:")

# match ride:
#     case "normal":
#         fare = dist * 15
#         if dist >= 20:
#             sur = (fare * 10)/100
#             total = fare + sur
#             print("Fare:",total)
#         else:
#             print("Fare:",fare)
#     case "premium":
#         fare = dist * 25
#         if dist >= 20:
#             sur = (fare * 10)/100
#             total = fare + sur
#             print("Fare:",total)
#         else:
#             print("Fare:",fare)
#     case _:
#         print("Invalid Type")

# Q68
# ent = int(input("Entrance Score:"))
# hsc = int(input("12th percentage:"))
# cat = input("Caste:")

# match cat:
#     case "general":
#         if ent >= 80 and hsc >= 75:
#             print("Admission Eligible")
#         else:
#             print("Admission Not Eligible")
#     case "obc":
#         if ent >= 70 and hsc >= 70:
#             print("Admission Eligible")
#         else:
#             print("Admission Not Eligible")
#     case "sc":
#         if ent >= 60 and hsc >= 60:
#             print("Admission Eligible")
#         else:
#             print("Admission Not Eligible")