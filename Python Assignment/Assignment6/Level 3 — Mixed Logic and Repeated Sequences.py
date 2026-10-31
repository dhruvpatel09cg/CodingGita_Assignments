# Q24
# N = int(input("N:"))
# for r in range(1,N+1):
#     for s in range(1,r+1):
#         print("*",end="")
#     print()
# for t in range(1,N):
#     for u in range(1,N-t+1):
#         print("*",end="")
#     print()

# Q25
# N = int(input("N:"))
# for v in range(1,N+1):
#     for w in range(1,N-v+2):
#         print(w,end="")
#     print()
# for x in range(2,N+1):
#     for y in range(1,x+1):
#         print(y,end="")
#     print()

# Q26
# N = int(input("N:"))
# for v in range(1,N+1):
#     for w in range(1,N-v+2):
#         print(chr(64+w),end="")
#     print()
# for x in range(2,N+1):
#     for y in range(1,x+1):
#         print(chr(64+y),end="")
#     print()

# Q27
# N = int(input("N:"))
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         if i%2==1 and j%2==1:
#             print("*",end="")
#         elif i%2==1 and j%2==0:
#             print("#",end="")
#         elif i%2==0 and j%2==1:
#             print("#",end="")
#         else:
#             print("*",end="")
#     print()

# Q28
# N = int(input("N:"))
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         if i%2==1:
#             print(j%2,end="")
#         else:
#             print((j+1)%2,end="")
#     print()

# Q29
# N = int(input("N:"))
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         print(i*j,end=" ")
#     print()

# Q30
N = int(input("N:"))
