Optional

# Q63
# unit = int(input("Enter electricity units consumed:"))
# if unit <= 100:
#     rate = 5
#     bill = unit * rate
#     print(f"Units: {unit}\nRate: ₹{rate} per unit\nBill: {bill}")
# elif unit <= 300:
#     rate = 7
#     bill = unit * rate
#     print(f"Units: {unit}\nRate: ₹{rate} per unit\nBill: {bill}")
# elif unit <= 400:
#     rate = 10
#     bill = unit * rate
#     print(f"Units: {unit}\nRate: ₹{rate} per unit\nBill: {bill}")
# elif unit <= 500:
#     rate = 15
#     bill = unit * rate
#     print(f"Units: {unit}\nRate: ₹{rate} per unit\nBill: {bill}")
# elif unit <= 600:
#     rate = 18
#     bill = unit * rate
#     print(f"Units: {unit}\nRate: ₹{rate} per unit\nBill: {bill}")
# else:
#     rate = 20
#     bill = unit * rate
#     print(f"Units: {unit}\nRate: ₹{rate} per unit\nBill: {bill}")

# Q65
# print(f"1 → Pizza → ₹250\n2 → Burger → ₹150\n3 → Pasta → ₹200\n4 → Sandwich → ₹120\n5 → Noodles → ₹230\n6 → Momo → ₹90\n7 → Fries → ₹170")
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
#     case 5:
#             total = 230 * qun
#             if total >= 500:
#                 dis = (total * 10)/100
#                 final = total - dis
#                 print(f"Total: {total}, Discount: {dis}, Final: {final}")
#             else:
#                 print(f"Total: {total}, Discount: 0.00, Final: {total}")
#     case 6:
#             total = 90 * qun
#             if total >= 500:
#                 dis = (total * 10)/100
#                 final = total - dis
#                 print(f"Total: {total}, Discount: {dis}, Final: {final}")
#             else:
#                 print(f"Total: {total}, Discount: 0.00, Final: {total}")
#     case 7:
#             total = 170 * qun
#             if total >= 500:
#                 dis = (total * 10)/100
#                 final = total - dis
#                 print(f"Total: {total}, Discount: {dis}, Final: {final}")
#             else:
#                 print(f"Total: {total}, Discount: 0.00, Final: {total}")
#     case _:
#         print("Not Available")

#Q64
# print(f"1. Check Balance\n2. Deposit\n3. Withdraw\n4. Apply for Loan\n5. Request ATM Card\n6. Deactivate Account\n7. Exit")

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
#         print("Apply for Loan")
#     case 5:
#         print("Request ATM Card")
#     case 6:
#         print("Deactivate Account")
#     case 7:
#         print("Exit")
#     case _:
#         print("Invalid Choice")
