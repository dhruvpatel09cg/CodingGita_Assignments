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
# for z in range(1,N+1):
#     for a in range(1,N+1):
#         if z%2==1 and a%2==1:
#             print("*",end="")
#         elif z%2==1 and a%2==0:
#             print("#",end="")
#         elif z%2==0 and a%2==1:
#             print("#",end="")
#         else:
#             print("*",end="")
#     print()

# Q28
# N = int(input("N:"))
# for b in range(1,N+1):
#     for c in range(1,N+1):
#         if b%2==1:
#             print(c%2,end="")
#         else:
#             print((c+1)%2,end="")
#     print()

# Q29
# N = int(input("N:"))
# for d in range(1,N+1):
#     for e in range(1,N+1):
#         print(d*e,end=" ")
#     print()

# Q30
# N = int(input("N:"))
# for f in range(1,N+1):
#     if f%2==1:
#         for g in range(1,f+1):
#             print(g,end="")
#     else:
#         for g in range(f,0,-1):
#             print(g,end="")
#     print()

# Q31
# N = int(input("N:"))
# for h in range(1,N+1):
#     for i in range(1,N-h+1):
#         print(" ",end="")
#     for j in range(1,h+1):
#         print(j,end="")
#     for k in range(h-1,0,-1):
#         print(k,end="")
#     print()
# for l in range(1,N):
#     for m in range(1,l+1):
#         print(" ",end="")
#     for n in range(1,N-l+1):
#         print(n,end="")
#     for o in range(N-l-1,0,-1):
#         print(o,end="")
#     print()

# Q32
# N = int(input("N:"))

# for p in range(2*N-1):
#     for q in range(2*N-1):
#         if p <= q and p <= 2*N-2-p and p <= 2*N-2-q:
#             print(N-p, end=" ")
#         elif q <= p and q <= 2*N-2-p and q <= 2*N-2-q:
#             print(N-q, end=" ")
#         elif 2*N-2-p <= p and 2*N-2-p <= q and 2*N-2-p <= 2*N-2-q:
#             print(N-(2*N-2-p), end=" ")
#         else:
#             print(N-(2*N-2-q), end=" ")
#     print()