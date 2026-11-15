# Q33
# N = int(input("N:"))
# for r in range(1,N+1):
#     for s in range(1,N+1):
#         if r==1 or r==N or s==1 or s==N:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# Q34
# row = int(input("Rows:"))
# col = int(input("Columns:"))
# for t in range(1,row+1):
#     for u in range(1,col+1):
#         if t==row or t==1 or u==1 or u==col:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# Q35
# N = int(input("N:"))
# for v in range(1,N+1):
#     for w in range(1,N+1):
#         if v==1 or w==1 or v==N or w==N:
#             print(1,end="")
#         else:
#             print(0,end="")
#     print()

# Q36
# N = int(input("N:"))
# for x in range(1,N+1):
#     for y in range(1,x+1):
#         if x==y or x==N or y==1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# Q37
# N = int(input("N:"))
# for z in range(1,N+1):
#     for a in range(N,0,-1):
#         if z==1 or a==z or a==N:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# Q38
# N = int(input("N:"))
# for b in range(1,N+1):
#     for c in range(N,b,-1):
#         print(" ",end="")
#     for k in range(1,2*b):
#         if k==1 or k==2*b-1 or b==N:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# Q39
N = int(input("N:"))
for