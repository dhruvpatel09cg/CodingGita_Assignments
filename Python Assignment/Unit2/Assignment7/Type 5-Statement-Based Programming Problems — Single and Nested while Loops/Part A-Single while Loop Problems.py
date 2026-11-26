# Q79
# N = int(input("N:"))
# i = 1
# count = 0
# while i<=N:
#     if N%i==0:
#         count+=1
#     i+=1
# if count>2:
#     print("Not Prime")
# else:
#     print("Prime")

# Q80
# A = int(input("A:"))
# B = int(input("B:"))
# if A<B:
#     lower = A
# else:
#     lower = B
# i=lower
# while i>0:
#     if A%i==0 and B%i==0:
#         print("LCM:",i)
#         break
#     i-=1

# Q81
# A = int(input("A:"))
# B = int(input("B:"))
# if A>B:
#     greater=A
# else:
#     greater=B
# i=greater
# while i>=greater:
#     if i%A==0 and i%B==0:
#         print("LCM:",i)
#         break
#     i+=1

# Q82
# num = int(input("Number:"))
# sum=0
# i = 1
# while i<num:
#     if num%i==0:
#         sum+=i
#     i+=1
# if sum==num:
#     print("Perfect Number")
# else:
#     print("Not Perfect")

# Q83
# num = int(input("Number:"))
# original = num
# fact_sum = 0
# while num>0:
#     digit=num%10
#     if digit == 0:
#         fact = 1
#     elif digit == 1:
#         fact = 1
#     elif digit == 2:
#         fact = 2
#     elif digit == 3:
#         fact = 6
#     elif digit == 4:
#         fact = 24
#     elif digit == 5:
#         fact = 120
#     elif digit == 6:
#         fact = 720
#     elif digit == 7:
#         fact = 5040
#     elif digit == 8:
#         fact = 40320
#     else:
#         fact = 362880

#     fact_sum+=fact
#     num//=10

# if fact_sum == original:
#     print("Strong")
# else:
#     print("Not Strong")

# Q84
# import math
# num = int(input("Number:"))
# original = num
# len = int(math.log10(num))+1
# sum=0
# while num>0:
#     digit=num%10
#     sum+=digit**len
#     num//=10
# if sum==original:
#     print("Armstrong")
# else:
#     print("Not Armstrong")

# Q85
# N = int(input("N:"))
# binary = 0
# place = 1

# while N > 0:
#     digit = N % 2
#     binary = binary + digit * place
#     place = place * 10
#     N //= 2

# print(binary)

# Q86
# N = int(input("N:"))
# i=1
# sum=0
# while i<=N:
#     if N%i==0:
#         sum+=i
#     i+=1
# print(sum)