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
#     for g in range(1,2*b):
#         if g==1 or g==2*b-1 or b==N:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# Q39
# N = int(input("N:"))
# for d in range(1,N+1):
#     for e in range(N,d,-1):
#         print(" ",end="")
#     for f in range(1,2*d):
#         if f==1 or f==2*d-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# for h in range(1,N):
#     for i in range(1,h+1):
#         print(" ",end="")
#     for j in range(1,2*N+1):
#         if j==1 or j==2*N-2*h-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# Q40
# N = int(input("N:"))
# for k in range(1,N+1):
#     for m in range(1,k):
#         print(" ",end="")
#     for l in range((N-k)*2+1,0,-1):
#         if l==1 or l==(N-k)*2+1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# for n in range(2,N+1):
#     for p in range(N-n,0,-1):
#         print(" ",end="")
#     for o in range(1,2*n):
#         if o==1 or o==2*n-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# Q41
# N = int(input("N:"))
# for k in range(1,N+1):
#     if k==N:
#         for q in range(1,2*N+1):
#             print("*",end="")
#         print()
#         break
#     for m in range(1,k):
#         print(" ",end="")
#     for l in range((N-k)*2+1,0,-1):
#         if l==1 or l==(N-k)*2+1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# for n in range(2,N+1):
#     for p in range(N-n,0,-1):
#         print(" ",end="")
#     for o in range(1,2*n):
#         if o==1 or o==2*n-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()