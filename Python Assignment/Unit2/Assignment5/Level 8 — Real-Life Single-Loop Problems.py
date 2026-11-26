# Q62
# days = int(input("No. of Days:"))
# expense = input("Expense per day:").split(" ")
# total = 0
# high = 0
# low = 100000
# for i in expense:
#     if int(i) > high:
#         high = int(i)
#     if int(i) < low:
#         low = int(i)
#     total = total + int(i)
# print("Total:",total)
# print("High:",high)
# print("Low:",low)

# ======================================================================

# days = int(input("No. of Days: "))

# total = 0
# high = 0
# low = 100000

# for i in range(days):
#     expense = int(input("Expense: "))

#     total = total + expense

#     if expense > high:
#         high = expense

#     if expense < low:
#         low = expense

# print("Total:", total)
# print("High:", high)
# print("Low:", low)

# Q63
# sub = int(input("No. of Subjects:"))

# total = 0
# high = 0
# low = 100

# for i in range(sub):
#     marks = int(input("Marks:"))
#     total = total + marks
#     if marks > high:
#         high = marks
#     if marks < low:
#         low = marks
# avg = total / sub
# print("Total:",total)
# print("Average:",avg)
# print("Highest:",high)
# print("Lowest:",low)

# Q64
# wd = int(input("No. of Working Days:"))
# total = 0
# present = 0
# absent = 0
# for i in range(wd):
#     status = input("P or A:")
#     total = total + 1
#     if status in "pP":
#         present = present + 1
#     else:
#         absent = absent + 1
# attend = (present/total)*100
# print("Present:",present)
# print("Absent:",absent)
# print("Attendance:",attend)

# Q65
# days = int(input("No. of days:"))
# total = 0
# above10 = 0

# for i in range(days):
#     unit = int(input("electricity units used:"))
#     total = total + unit
#     if unit > 10:
#         above10 = above10 + 1
# print("Total units:",total)
# print("Days Above 10:",above10)

# Q66
# num = int(input("No. of products:"))
# total = 0
# costly = 0

# for i in range(num):
#     price = int(input("Price of item:"))
#     total = total + price
#     if price > 1000:
#         costly = costly + 1
# print("Total:",total)
# print("Products Above 1000:",costly)

# Q67
# N = int(input("N:"))
# success = 0
# fail = 0

# for i in range(N):
#     status = input("S or F:")
#     if status in "sS":
#         success = success + 1
#     else:
#         fail = fail + 1
# print("Successful:",success)
# print("Failed:",fail)