# Q71
# marks = 85

# if marks >= 40:
#     print("Pass")
# elif marks >= 75:
#     print("Very Good")
# else:
#     print("Fail")

# Output: Pass
#This doesn't print Very Good as the first condition is 40 or more which is satisfied by 85 so debugger doesn't read the code after that and directly give the output.

# Q72
# marks = 85

# if marks >= 90:
#     print("A")
# elif marks >= 75:
#     print("B")
# elif marks >= 40:
#     print("Pass")
# else:
#     print("Fail")

# Output: B
# Changing order of conditions will help in producing better output like in 1st case condition 40 or more is not letting the debugger read the code further. We should put the biggest no. at top and so on...

# Q73
# age = 20
# has_id = True


# if age >= 18:
#     if has_id:
#         print("Entry Allowed")
#     else:
#         print("ID Required")
# else:
#     print("Underage")

# Output: Entry Allowed

# age = 20
# has_id = False
# Output: ID Required

# age = 16
# has_id = True
# Output: Underage

# Q74
# choice = 5

# match choice:
#     case 1:
#         print("Add")
#     case 2:
#         print("View")
#     case 3:
#         print("Delete")
#     case _:
#         print("Invalid Choice")

# Output: Invalid Choice
# case _ is default case generally include all the remaining possible inputs except given cases generally used to give output like invalid or try again or any other declining message.

# Q75
# marks = 82
# attendance = 80

# if attendance >= 75:
#     if marks >= 90:
#         print("Grade A")
#     elif marks >= 75:
#         print("Grade B")
#     elif marks >= 40:
#         print("Pass")
#     else:
#         print("Fail")
# else:
#     print("Not Eligible")

# Output: Grade B
# First the debugger checked whether attendance is more than equal to 75 or not as it is the top most condition we decided to keep for our output.