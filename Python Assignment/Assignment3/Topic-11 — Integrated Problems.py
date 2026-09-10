#Q60
# info = input("Your name and three subject marks:").split(",")
# name = info[0]
# sub1, sub2, sub3 = info[1:]
# total = int(sub1)+int(sub2)+int(sub3)
# avg = total / 3
# print(f"Name:\t{name}\nTotal:\t{total}\nAverage:\t{avg:.2f}")

#Q61
# student_id = input("ID:").upper().split("-")
# degree, batch, branch, roll_no = student_id
# print(roll_no[-4:])
# roll = int(roll_no)
# print("Degree:",degree)
# print("Batch:",batch)
# print("Branch:",branch)
# print("Roll no.:",roll)

#Q62
# name = input("Full name:").split()
# first,middle,last = name
# print(name[0]+"."+name[-1])

#Q63
# sentence = input("Write a sentence:").split()
# print(f"First word: {sentence[0]}\nLast word: {sentence[-1]}\nTotal no. of words: {len(sentence)}")

#Q64
# email = input("Email ID:")
# email_id = email.split("@")
# print(f"@ Present: {"@" in email}\nUsername: {email_id[0]}\nDomain: {email_id[-1]}")

# user, domain = email_id
# print(f"@ Present: {"@" in email}\nUsername: {user}\nDomain: {domain}")

#Q65
# character = input("Type any character:")
# print("Character:",character)
# code = int(ord(character))
# print("Unicode:",code)
# code -= 1
# print("Previous character:",chr(code))
# code += 2
# print("Next character:",chr(code))

#Q66
# product_info = input("type Product name, Price, Quantity, Discount:").split(",")
# name, price, qun, discount = product_info
# subtotal = int(price)*int(qun)
# discount_amount = subtotal*int(discount)/100
# final = subtotal-discount_amount

# print(f"Product: {name}\nPrice: {float(price):.2f}\nQuantity: {qun}\nSubtotal: {float(subtotal):.2f}\nDiscount: {float(discount_amount):.2f}\nFinal Total: {float(final):.2f}")

#Q67
# date = input("dd-mm-yyyy:").split("-")
# day, month, year = date

# print(f"Day: {day}\nMonth: {month}\nYear: {year}")
# print(date[-1])

#Q68
# inp = input("Two words:").split()
# first, second = inp
# print(f"First word: {first}\nSecond word: {second}\nFirst word reversed: {first[-1::-1]}\nSecond word reversed: {second[-1::-1]}")

#Q69
# student_id = input("degree-batch-branch-roll_no:").split("-")
# print(f"Degree: {student_id[0]}\nBatch: {student_id[1]}\nBranch: {student_id[2]}\nRoll: {student_id[3]}\nCode: {student_id[0]+"/"+student_id[2]+"/"+student_id[3]}")

#Q70
# full_name = input("Full name:")
# name = full_name.split()

# print("Original:",name)
# print(f"First name: {name[0]}\nLast name: {name[-1]}\nFirst name(upper): {name[0].upper()}\nLast name(lower): {name[-1].lower()}\nFull Name Reversed: {full_name[::-1]}")
