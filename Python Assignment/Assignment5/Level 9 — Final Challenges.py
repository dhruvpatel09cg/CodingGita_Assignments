# Q68
# import math
# inte = int(input("Integer:"))
# num = 0
# sum = 0
# large = 0
# small = 10
# even = 0
# odd = 0

# for i in range(int(math.log10(inte))+1):
#     digit = inte % 10
#     num = num + 1
#     sum = sum + digit
#     if digit > large:
#         large = digit
#     if digit < small:
#         small = digit
#     if digit % 2 == 0:
#         even = even + 1
#     else:
#         odd = odd + 1
#     inte = inte // 10
# print("Digits:",num)
# print("Sum:",sum)
# print("Largest:",large)
# print("Smallest:",small)
# print("Even Digits:",even)
# print("Odd Digits:",odd)

# Q69
# string = input("String:")
# total = 0
# vowel = 0
# consonant = 0
# upper = 0
# lower = 0
# even = 0

# for i in range(len(string)):
#     total = total + 1
#     if string[i] in "aeiouAEIOU":
#         vowel = vowel + 1
#     if string[i].isalpha() and string[i] not in "aeiouAEIOU":
#         consonant = consonant + 1
#     if string[i].isupper():
#         upper = upper + 1
#     if string[i].islower():
#         lower = lower + 1
#     if i % 2 == 0:
#         even = even + 1
# print("Total characters:",total)
# print("Vowels:",vowel)
# print("Consonants:",consonant)
# print("Uppercase:",upper)
# print("Lowercase:",lower)
# print("Even Index Characters:",even)