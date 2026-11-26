# Q36
# user = input("Enter Username:")
# password = input("Enter Password:")
# if user == "admin":
#     if password == "admin123":
#         print("Login Successful")
#     else:
#         print("Wrong Password")
# else:
#     print("Invalid Username")

# Q37
# age = int(input("Enter Age:"))
# test = input("Test status:")
# if age >= 18:
#     if test == "pass":
#         print("License Approved")
#     else:
#         print("Test not passed")
# else:
#     print("Age Not Eligible")

# Q38
# amt = int(input("Enter Balance:"))
# wd = int(input("Enter Withdrawal Amount:"))
# if amt >= wd:
#     if wd % 100 == 0:
#         print("Withdrawal Successful")
#     else:
#         print("Enter Amount in Multiples of 100")
# else:
#     print("Insufficient Balance")

# Q39
# marks = int(input("Enter your marks:"))
# attend = int(input("Enter attendance:"))
# if attend >= 75:
#     if marks >= 40:
#         print("Pass")
#     else:
#         print("Fail")
# else:
#     print("Not Eligible Due to Attendance")

# Q40
# acc = input("Enter account type:")
# bal = int(input("Enter your Balance:"))
# if acc == "savings":
#     if bal >= 1000:
#         print("Minimum Balance Maintained")
#     else:
#         print("Minimum Balance Not Maintained")
# else:
#     print("Unsupported Account")

# Q41
# ord_amt = int(input("Order Amount:"))
# method = input("Payment Method:")
# if ord_amt >= 500:
#     if method == "upi" or method == "card":
#         print(method, "payment accepted")
#     else:
#         print("Unsupported Payment Method")
# else:
#     print("Minimum Order Amount Not Reached")

# Q42
# year = int(input("Year:"))
# attend = int(input("Attendance:"))
# if 2<= year <=4:
#     if attend >= 75:
#         print("Room Eligible")
#     else:
#         print("Attendance Too Low")
# else:
#     print("Not Eligible by Year")

# Q43
# plan = input("Current plan:")
# use = int(input("Monthly Data Usage:"))
# if plan == "basic":
#     if use >= 100:
#         print("Upgrade plan")
#     else:
#         print("Basic Plan Is Sufficient")
# else:
#     print("Already on Higher Plan")