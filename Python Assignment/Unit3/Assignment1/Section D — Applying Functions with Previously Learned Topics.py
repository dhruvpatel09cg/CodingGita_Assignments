# Q14
# def count_digits(number):
#     import math
#     count = 0
#     # length = int(math.log10(number)+1)
#     # print(length)
#     for i in range(0,int(math.log10(number)+1)):
#         count+=1
#         number//10
#     return count

# # count_digits(4354)
# count = count_digits(34253)
# print("Total Digits:",count)

# Q15
# def sum_of_digits(number):
#     import math
#     sum = 0
#     for i in range(0,int(math.log10(number)+1)):
#         digit = number%10
#         sum+=digit
#         number//=10
#     return sum

# result = sum_of_digits(482)
# print("Sum of digits:", result)

# result = sum_of_digits(799)
# print("Sum of digits:", result)

# Q16
# def reverse_number(number):
    # import math
    # reverse = 0
    # for i in range(0,int(math.log10(number))+1):
    #     digit = number%10
    #     reverse = reverse*10+digit
    #     number//=10
    # return reverse

# result = reverse_number(4826)
# print("Reversed number:", result)

# result = reverse_number(78347843)
# print("Reversed number:", result)

# Q17
# def is_palindrome(number):
#     import math
#     original = number
#     reverse = 0
#     for i in range(0,int(math.log10(number))+1):
#         digit = number%10
#         reverse = reverse*10+digit
#         number//=10
#     if original==reverse:
#         return True
#     else:
#         return False
    
# result = is_palindrome(121)
# print(result)

# result = is_palindrome(163478361)
# print(result)

# result = is_palindrome(12321)
# print(result)

# Q18
# def is_prime(number):
#     multiples = 0
#     for i in range(2,number):
#         if number%i==0:
#             return False
#         break
#     return True

# result = is_prime(17)
# print(result)

# result = is_prime(2)
# print(result)

# result = is_prime(33)
# print(result)

# result = is_prime(34)
# print(result)

# Q19
# def display_primes(start, end):
#     primes=""
#     total = 0
#     for i in range(start,end+1):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             primes+=str(i)+" "
#             total+=1
#     print("Prime numbers:",primes)
#     print("Total prime numbers:",total)

# display_primes(10, 30)

# display_primes(20,25)

# Q20
# def display_student_report(name, mark_1, mark_2, mark_3):
#     total=mark_1+mark_2+mark_3
#     avg=total/3
#     if avg>=40:
#         result = "PASS"
#     else:
#         result = "FAIL"
#     print(f"==============================\n        STUDENT REPORT        \n==============================")
#     print(f"Name       : {name}\nSubject 1  : {mark_1}\nSubject 2  : {mark_2}\nSubject 3  : {mark_3}\n------------------------------")
#     print(f"Total      : {total} / 300\nPercentage : {avg:.2f}%\nResult     : {result}\n==============================")

# display_student_report("Rahul", 75, 80, 65)
# display_student_report("Priya", 84, 34, 54)