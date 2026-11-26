# Q52
# N = int(input("N:"))
# old = N
# reverse = 0
# while N>0:
#     digit = N % 10
#     reverse = reverse*10+digit
#     N//=10
# print(reverse)
# if old==reverse:
#     print("Palindrome")
# else:
#     print("Non-Palindrome")

# Q53
# N = int(input("N:"))
# D = int(input("D:"))
# count = 0
# while N>0:
#     digit = N % 10
#     if digit==D:
#         count+=1
#     N//=10
# print(count)

# Q54
# N = int(input("N:"))
# reference = N%10
# same = True
# while N>0:
#     current = N%10
#     if current!=reference:
#         same = False
#         break
#     N//=10
# if same:
#     print("Yes")
# else:
#     print("No")

# Q55
# N = int(input("N:"))
# last = N%10
# mid_sum = 0
# while N>=1:
#     mid = N%10
#     if mid==last:
#         pass
#     elif N>10:
#         mid_sum = mid_sum+mid
#     else:
#         first = mid
#     N//=10
# print("Sum of middle no.:",mid_sum)
# print("Sum of first & last digit:",last+first)